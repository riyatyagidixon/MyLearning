# test_calculator.py

import unittest
from calci import add, subtract, multiply, divide
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class TestCalculatorFunctions(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(-10, -2), 5)
        self.assertEqual(divide(10, 0), "Error: Division by zero")


class CustomTestRunner(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        self.success += 1
        print(Fore.GREEN + f"✔️ SUCCESS: {test}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.failed += 1
        print(Fore.RED + f"❌ FAILURE: {test}")

    def addError(self, test, err):
        super().addError(test, err)
        self.failed += 1
        print(Fore.YELLOW + f"⚠️ ERROR: {test}")

    def startTestRun(self):
        self.success = 0
        self.failed = 0

    def stopTestRun(self):
        total_tests = self.success + self.failed
        accuracy = (self.success / total_tests) * 100 if total_tests > 0 else 0
        print("\n" + Fore.CYAN + "Results:")
        print(f"{Style.BRIGHT}Total Tests: {total_tests}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Passed: {self.success} ✔️{Style.RESET_ALL}")
        print(f"{Fore.RED}Failed: {self.failed} ❌{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}Accuracy: {accuracy:.2f}%{Style.RESET_ALL}\n")


class CustomTestRunnerSuite(unittest.TextTestRunner):
    resultclass = CustomTestRunner


suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCalculatorFunctions)
runner = CustomTestRunnerSuite(verbosity=2)
runner.run(suite)