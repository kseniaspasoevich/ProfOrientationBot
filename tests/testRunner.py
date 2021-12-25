import unittest

from other.testFileIntegrity import FileIntegrityTests

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromTestCase(FileIntegrityTests)

testResult = unittest.TestResult()

runner = unittest.TextTestRunner(verbosity=2)
testResult = runner.run(suites)

if len(testResult.errors) == 0 and len(testResult.failures) == 0 and testResult.testsRun > 0:
    from unit.testAnswers import TestAnswers
    from unit.testFirstTestLogic import TestFirstTest

    testLoad2 = unittest.TestLoader()
    suites2 = testLoad2.loadTestsFromTestCase(TestFirstTest)

    suites3 = testLoad2.loadTestsFromTestCase(TestAnswers)



    testResult = unittest.TestResult()

    runner2 = unittest.TextTestRunner(verbosity=2)
    testResult = runner2.run(suites2)
    testResult2 = runner2.run(suites3)
    if len(testResult.errors) != 0 or len(testResult.failures) != 0 or testResult.testsRun <= 0 or len(testResult2.errors) != 0 or len(testResult2.failures) != 0 or testResult2.testsRun <= 0:
        raise RuntimeError()
else:
    print("First part failed")
    raise RuntimeError()
