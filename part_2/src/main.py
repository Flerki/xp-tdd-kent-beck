class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()

        method = getattr(self, self.name)
        method()
        # another approach for dynamic call of method
        # exec("self." + self.name + "()")

        self.tearDown()

    def tearDown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log += "testMethod "

    def tearDown(self):
        self.log += "tearDown "


class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown " == test.log


TestCaseTest("testTemplateMethod").run()
