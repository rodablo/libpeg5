#! /usr/bin/env python

"""
Usage::

    testsuite.py [OPTIONS]

Run the libpeg5lang testsuite.
"""
import sys
import os
import collections.abc
from typing import List
from e3.env import Env
import e3.yaml

from e3.testsuite import (
    Testsuite, TestFinder, YAMLTestFinder
)
from e3.testsuite.testcase_finder import (
    ProbingError, TestFinderResult, ParsedTest
)

from drivers.python_driver import PythonDriver

from drivers_.peg5_ import Peg5Driver
# from drivers_.grammar_driver import GrammarDriver
from drivers_.parser_driver import ParserDriver


class MultiTestFinder(TestFinder):
    def probe(self,
              testsuite: Testsuite,
              dirpath: str,
              dirnames: List[str],
              filenames: List[str]) -> TestFinderResult:
        # There is a testcase if there is a "multi_test.yaml" file
        if "multi_test.yaml" not in filenames:
            return None
        yaml_file = os.path.join(dirpath, "multi_test.yaml")
        try:
            test_env = e3.yaml.load_with_config(yaml_file, Env().to_dict())
        except e3.yaml.YamlError:
            raise ProbingError("invalid syntax for test.yaml")
        # Copied from YAMLTestFinder, see the comment there.
        if test_env is None:
            test_env = {}
        elif not isinstance(test_env, collections.abc.Mapping):
            raise ProbingError("invalid format for test.yaml")

        driver_name = test_env.get("driver")
        if driver_name is None:
            driver_cls = None
        else:
            try:
                driver_cls = testsuite.test_driver_map[driver_name]
            except KeyError:
                raise ProbingError("cannot find driver")

        tests = []
        for f in filenames:
            base, extension = os.path.splitext(f)
            if base and extension == '.input':
                test_env_copy = test_env.copy()
                test_env_copy['input_file'] = f
                test_env_copy['output_file'] = base + '.output'
                tests.append(ParsedTest(testsuite.test_name(os.path.join(dirpath, base)),
                                        driver_cls,
                                        test_env_copy,
                                        dirpath
                                        ))
        return tests


class __Testsuite(Testsuite):
    test_subdir = 'tests'
    test_driver_map = {
        'python': PythonDriver,
        'peg5_': Peg5Driver,
        'parser': ParserDriver
    }

    @property
    def test_finders(self) -> List[TestFinder]:
        return [YAMLTestFinder(), MultiTestFinder()]

    def add_options(self, parser):
        parser.add_argument(
            '--with-python',
            help='If provided, use as the Python interpreter in testcases.'
        )

        parser.add_argument(
            '--coverage', '-C', action='store_true',
            help='Enable computation of code coverage for Langkit and'
                 ' Langkit_Support. This requires coverage.py and'
                 ' GNATcoverage.'
        )

        parser.add_argument(
            '--valgrind', action='store_true',
            help='Run tests with Valgrind to check memory issues.'
        )

        parser.add_argument(
            '--no-auto-path', action='store_true',
            help='Do not automatically add Langkit to PYTHONPATH. This is'
                 ' useful to test that Langkit was properly installed in the'
                 ' environment that runs the testsuite.'
        )

        parser.add_argument(
            '--restricted-env', action='store_true',
            help='Skip testcases that cannot run in a restricted environment'
                 ' (need for non-standard Python packages).'
        )

        parser.add_argument(
            '--pretty-print', action='store_true',
            help='Pretty-print generated source code.'
        )

        parser.add_argument(
            '--local-build', action='store_true',
            help='Build generated library instance local to the testsuite.'
        )

    def set_up(self):
        super().set_up()
        # print('set_up()')
        # print(os.getcwd())
        # print(self.root_dir)
        # print(self.test_dir)
        # print(self.test_subdir)
        # print(self.working_dir)
        # print(self.output_dir)
        # make the grammar available for impor
        # self.env.rewrite_baselines = self.env.options.rewrite
        # self.env.options.valgrind = False
        self.env.control_condition_env = {
            'restricted_env': self.env.options.restricted_env,
        }

        if self.env.options.local_build:
            # next line makes the grammar available to import
            sys.path.insert(1, os.path.abspath(os.path.join(self.root_dir, '..', 'peg5')))
            peg5_build_dir = os.path.join(self.working_dir, 'build')
            from helpers import run_make
            run_make(['--build-dir={}'.format(peg5_build_dir)])

    def tear_down(self):
        super().tear_down()


if __name__ == '__main__':
    sys.exit(__Testsuite().testsuite_main())
