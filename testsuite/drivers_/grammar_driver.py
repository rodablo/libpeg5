
from e3.testsuite.driver.diff import DiffTestDriver
# from e3.testsuite.result import TestResult, TestStatus


class GrammarDriver(DiffTestDriver):
    """
    """
    def set_up(self) -> None:
        super(GrammarDriver, self).set_up()
        #print('grammar.set_up---->',self.test_name)

    #def run(self) -> None:
    #    #print('grammar.run------->',self.test_name)
    #    self.result.out = 'Done'
    #    self.result.set_status(TestStatus.PASS)

    def tear_down(self) -> None:
        #print('grammar.tear_down->',self.test_name)
        super().tear_down()
