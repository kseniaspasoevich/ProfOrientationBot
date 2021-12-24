import unittest

from other.testFileIntegrity import FileIntegrityTests

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromTestCase(FileIntegrityTests)

testResult = unittest.TestResult()

runner = unittest.TextTestRunner(verbosity=2)
testResult = runner.run(suites)
# print("errors")
# print(len(testResult.errors))
# print("failures")
# print(len(testResult.failures))
# print("skipped")
# print(len(testResult.skipped))
# print("testsRun")
# print(testResult.testsRun)
if len(testResult.errors) == 0 and len(testResult.failures) == 0 and testResult.testsRun > 0:
    from unit.testAnswers import TestAnswers
    from unit.testFirstTestLogic import TestFirstTest

    testLoad2 = unittest.TestLoader()
    suites2 = testLoad2.loadTestsFromTestCase(TestFirstTest)

    suites3 = testLoad2.loadTestsFromTestCase(TestAnswers)



    testResult = unittest.TestResult()

    runner2 = unittest.TextTestRunner(verbosity=2)
    testResult2 = runner2.run(suites2)
    runner2.run(suites3)
else:
    print("First part failed")
