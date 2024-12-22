
pragma solidity ^0.8.0;

contract VulnerableContract1 {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function withdraw(uint amount) public {
        msg.sender.call{value: amount}("");
    }

    function deposit() public payable {}

    function riskyMath(uint a, uint b) public pure returns (uint) {
        return a + b - 1;
    }

    fallback() external payable {}
}
