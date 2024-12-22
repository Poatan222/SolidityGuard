
import unittest
from scanner.scanner import SmartContractScanner

class TestSmartContractScanner(unittest.TestCase):
    def setUp(self):
        self.code = """
        pragma solidity ^0.8.0;

        contract Test {
            function riskyFunction() public {
                tx.origin.call{value: 1}("");
            }
        }
        """

    def test_front_running_detection(self):
        scanner = SmartContractScanner(self.code)
        issues = scanner.scan_for_vulnerabilities()
        self.assertIn("Potential front-running attack vector detected.", issues)

if __name__ == "__main__":
    unittest.main()
