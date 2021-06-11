// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.7.0;

contract Greeter{
    string public greeting;
    
    constructor(string memory _greeting) {
        greeting = _greeting;
    }

    function setGreeting(string memory _greeting) public{
        greeting = _greeting;
    }
    
    function say() public view returns(string memory){
        return greeting;
    }
}