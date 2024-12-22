
pragma solidity ^0.8.0;

contract VulnerableContract3 {
    function riskyFunction() public {
        tx.origin.call{value: 1}("");
    }
}
