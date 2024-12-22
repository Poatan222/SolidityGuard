# SolidityGuard
SolidityGuard is a Python-based security scanner designed to identify vulnerabilities in Solidity smart contracts. This tool is essential for developers and auditors to enhance the security posture of their decentralized applications (dApps).

SolidityGuard provides a quick and efficient way to detect common vulnerabilities in Solidity code, making it a valuable tool for developers, auditors, and organizations working in the Web3 ecosystem

# Current Features
SolidityGuard scans Solidity smart contracts for the following vulnerabilities:

Reentrancy Attacks
Integer Overflow and Underflow
Hardcoded Secrets
Unrestricted Access Control
Unchecked External Calls
DoS with Gas Limit
Timestamp Dependency
Delegatecall Misuse
Uninitialized Storage Variables
Floating Pragma Version
Selfdestruct Usage
Missing Fallback Functions

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


