
pragma solidity ^0.8.0;

contract VulnerableContract2 {
    function transfer(address recipient, uint256 amount) public {
        recipient.call{value: amount}("");
    }

    function randomNumber() public view returns (uint) {
        return uint(blockhash(block.number - 1)) % 100;
    }
}
