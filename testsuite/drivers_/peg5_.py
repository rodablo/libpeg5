from drivers.python_driver import PythonDriver


class Peg5Driver(PythonDriver):
    """
    """
    def set_up(self) -> None:
        super().set_up()
        #print('driver.set_up---->',self.test_name)

    def run(self) -> None:
        #print('driver.run------->',self.test_name)
        super().run()

    def tear_down(self) -> None:
        #print('driver.tear_down->',self.test_name)
        super().tear_down()

    pass
