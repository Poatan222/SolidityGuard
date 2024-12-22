# SolidityGuard
SolidityGuard is a Python-based security scanner designed to identify vulnerabilities in Solidity smart contracts. This tool is essential for developers and auditors to enhance the security posture of their decentralized applications (dApps).

SolidityGuard provides a quick and efficient way to detect common vulnerabilities in Solidity code, making it a valuable tool for developers, auditors, and organizations working in the Web3 ecosystem

# Current Features
SolidityGuard scans Solidity smart contracts for the following vulnerabilities:

1. Reentrancy Attacks
2. Integer Overflow and Underflow
3. Hardcoded Secrets
4. Unrestricted Access Control
5. Unchecked External Calls
6. DoS with Gas Limit
7. Timestamp Dependency
8. Delegatecall Misuse
9. Uninitialized Storage Variables
10. Floating Pragma Version
11. Selfdestruct Usage
12. Missing Fallback Functions
and much more incoming....


SolidityGuard supports CI/CD integration using GitHub Actions. See the .github/workflows/solidityguard.yml file for configuration details. This ensures your smart contracts are scanned automatically during code pushes and pull requests.

# Use Cases
Smart Contract Development:
Validate your contract code during development to identify potential security flaws before deployment.

Security Audits:
Provide a preliminary security assessment for auditors to quickly identify common vulnerabilities.

Learning Tool:
Help new Solidity developers understand and recognize common security issues in smart contracts.

Bug Bounties:
Assist researchers in identifying code level vulnerabilities in bug bounty programs.

Pre-Deployment Checks:
Use SolidityGuard to ensure your contract adheres to basic security standards before deploying to a live blockchain


# Installation
1. Clone the Repository:
2. git clone https://github.com/Poatan222/SolidityGuard.git
3. cd SolidityGuard
4. Set Up Python Environment: Ensure Python 3.10 or above is installed on your system.
   
# Install Dependencies:
pip install -r requirements.txt
Optional: Run tests to validate the installation:
python -m unittest discover tests
# Usage
Run the scanner on a Solidity contract:
python scanner/scanner.py scanner/examples/vulnerable_contract.sol
You can also test additional vulnerable contracts included in the examples/ directory.


