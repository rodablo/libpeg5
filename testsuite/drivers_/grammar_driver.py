#from typing import AnyStr, Generic, List, Optional, Pattern, Tuple, Union
from typing import Tuple

from e3.testsuite.driver.diff import DiffTestDriver
#from e3.testsuite.result import TestResult, TestStatus
from e3.testsuite.result import FailureReason, Log, binary_repr, truncated


class GrammarDriver(DiffTestDriver):
    """
    """
    def set_up(self) -> None:
        super(GrammarDriver, self).set_up()
        #print('grammar.set_up---->',self.test_name)

    #@property
    #def baseline_file(self) -> Tuple[str, bool]:
    #    return ('a.out', False)

    # @property
    # def baseline(self):  # -> Tuple[Optional[str], Union[str, bytes], bool]:
    #    return ('toto.peg','Done!', False)

    #def run(self) -> None:
    #    #print('grammar.run------->',self.test_name)
    #    self.result.out = Log('Done.')
    #    diff_log = (
    #        self.Style.RESET_ALL
    #        + self.Style.BRIGHT
    #        + "Diff failure: \n"
    #        + "\n"
    #    )
    #    self.result.diff = Log(diff_log)
    #    #self.result.expected = Log('Done.'  #.set_status(TestStatus.PASS)
    #    #self.result.set_status(TestStatus.PASS)

    def tear_down(self) -> None:
        #print('grammar.tear_down->',self.test_name)
        super().tear_down()
