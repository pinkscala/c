pragma solidity ^0.8;

contract bank {
    mapping (address=>uint256) private balance;

    function deposit(uint256 money) public payable{
        balance[msg.sender] += money;
    }

    function withdraw(uint256 money) public payable{
        balance[msg.sender] -= money;
    }

    function print() public view returns (uint256){
        return balance[msg.sender];
    }
}