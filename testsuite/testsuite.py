#! /usr/bin/env python

"""
Usage::

    testsuite.py [OPTIONS]

Run the libpeg5lang testsuite.
"""
import sys
import os
from typing import List  # , Union, Optional
from e3.testsuite import (Testsuite, TestFinder, YAMLTestFinder)  # , ParsedTest)
# from e3.testsuite.testcase_finder import TestFinderResult

import drivers.python_driver
# import drivers_.peg5_
# import drivers_.grammar_driver
from drivers_.peg5_ import Peg5Driver
# from drivers_.grammar_driver import GrammarDriver
from drivers_.parser_driver import ParserDriver


# class GrammarTestFinder(TestFinder):
#     @property
#     def test_dedicated_directory(self):
#         return True
#
#     def probe(self, testsuite, dirpath, dirnames, filenames) -> TestFinderResult:
#         return [
#             ParsedTest(
#                 # Strip the ".txt" extension for the test name
#                 test_name=testsuite.test_name(
#                     os.path.join(dirpath, f[:-4])
#                 ),
#                 driver_cls=GrammarDriver,  # testsuite.test_driver_map[driver_name]
#                 test_env={},
#                 test_dir=dirpath,
#                 # Preserve the ".txt" extension so that it matches "a.txt"
#                 test_matcher=os.path.join(dirpath, f),
#             )
#             for f in filenames if f.endswith(".peg")
#         ]


class P5_Testsuite(Testsuite):
    """ The Peg5Testsuite """
    test_subdir = 'tests'
    test_driver_map = {
        'python': drivers.python_driver.PythonDriver,
        'peg5_': Peg5Driver,
        # 'grammar': GrammarDriver,
        'parser': ParserDriver
    }

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
        # next line makes the grammar available to import
        sys.path.insert(1, os.path.abspath(os.path.join(self.root_dir, '..', 'peg5')))
        if self.env.options.local_build:
            peg5_build_dir = os.path.join(self.working_dir, 'build')
            from helpers import run_make
            run_make(['--build-dir={}'.format(peg5_build_dir)])

    # def tear_down(self):
    #     super().tear_down()

    @property
    def test_finders(self) -> List[TestFinder]:
        # return [YAMLTestFinder()]
        # return [GrammarTestFinder()]
        return [YAMLTestFinder()]  # , GrammarTestFinder()]
        #return Union[Optional[TestFinder], List[YAMLTestFinder, GrammarTestFinder]]


if __name__ == '__main__':
    sys.exit(P5_Testsuite().testsuite_main())
