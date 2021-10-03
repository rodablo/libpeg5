#! /usr/bin/env python

"""
Usage::

    testsuite.py [OPTIONS]

Run the libpeg5lang testsuite.
"""
import sys

from e3.testsuite import Testsuite

# import drivers_.p5_base_driver
import drivers.python_driver

class P5_Testsuite(Testsuite):
    """ The Peg5Testsuite """
    test_subdir = 'tests'
    test_driver_map = {
        'python': drivers.python_driver.PythonDriver,
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

    def set_up(self):
        super().set_up()
        #self.env.rewrite_baselines = self.env.options.rewrite
        self.env.control_condition_env = {
            'restricted_env': self.env.options.restricted_env,
        }

    def tear_down(self):
        super().tear_down()

if __name__ == '__main__':
    sys.exit(P5_Testsuite().testsuite_main())
