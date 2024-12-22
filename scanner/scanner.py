
import re
import sys

class SmartContractScanner:
    def __init__(self, contract_code: str):
        self.contract_code = contract_code
        self.vulnerabilities = []

    def scan_for_vulnerabilities(self):
        self.check_reentrancy_vulnerability()
        self.check_integer_overflow_underflow()
        self.check_hardcoded_secrets()
        self.check_unrestricted_access()
        self.check_unchecked_external_calls()
        self.check_dos_gas_limit()
        self.check_timestamp_dependency()
        self.check_delegatecall_usage()
        self.check_front_running()
        self.check_insecure_randomness()
        self.check_logic_errors()

        return self.vulnerabilities

    def check_reentrancy_vulnerability(self):
        if re.search(r"\.call\.value\(.*?\)\(\)|\.transfer\(.*?\)", self.contract_code):
            self.vulnerabilities.append("Potential reentrancy vulnerability detected.")

    def check_integer_overflow_underflow(self):
        if not re.search(r"SafeMath", self.contract_code):
            if re.search(r"\+|\-|\*|\/", self.contract_code):
                self.vulnerabilities.append("Potential integer overflow/underflow detected.")

    def check_hardcoded_secrets(self):
        if re.search(r"(0x[a-fA-F0-9]{40}|[A-Za-z0-9]{64})", self.contract_code):
            self.vulnerabilities.append("Hardcoded secret detected.")

    def check_unrestricted_access(self):
        public_functions = re.findall(r"function (.*?)\(.*?\) public", self.contract_code)
        for func in public_functions:
            if not re.search(rf"{func}.*?onlyOwner", self.contract_code):
                self.vulnerabilities.append(f"Public function '{func}' lacks access control.")

    def check_unchecked_external_calls(self):
        if re.search(r"\.call\(.*?\)", self.contract_code) and not re.search(r"require\(.*?\)", self.contract_code):
            self.vulnerabilities.append("Unchecked external call detected.")

    def check_dos_gas_limit(self):
        if re.search(r"for \(.*?\) {", self.contract_code):
            self.vulnerabilities.append("Potential DoS vulnerability detected in a loop.")

    def check_timestamp_dependency(self):
        if re.search(r"block\.timestamp|now", self.contract_code):
            self.vulnerabilities.append("Block timestamp dependency detected.")

    def check_delegatecall_usage(self):
        if re.search(r"delegatecall", self.contract_code):
            self.vulnerabilities.append("Delegatecall usage detected.")

    def check_front_running(self):
        if re.search(r"tx\.origin", self.contract_code):
            self.vulnerabilities.append("Potential front-running attack vector detected.")

    def check_insecure_randomness(self):
        if re.search(r"block\.number|block\.timestamp", self.contract_code):
            self.vulnerabilities.append("Insecure randomness detected.")

    def check_logic_errors(self):
        if re.search(r"function .*?\(.*?\) .*? returns \(.*?\)", self.contract_code):
            self.vulnerabilities.append("Potential logic error detected in function definition.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        contract_code = file.read()

    scanner = SmartContractScanner(contract_code)
    issues = scanner.scan_for_vulnerabilities()

    if issues:
        print("Security vulnerabilities detected:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("No security vulnerabilities detected.")
