solidity
pragma solidity ^0.8.0;

contract Cryptopatent {
    string public patentHash;
    string public licenseTerms;
    string public royaltyPayments;

    constructor(string memory _patentHash, string memory _licenseTerms, string memory _royaltyPayments) {
        patentHash = _patentHash;
        licenseTerms = _licenseTerms;
        royaltyPayments = _royaltyPayments;
    }

    function getPatentHash() public view returns (string memory) {
        return patentHash;
    }

    function getLicenseTerms() public view returns (string memory) {
        return licenseTerms;
    }

    function getRoyaltyPayments() public view returns (string memory) {
        return royaltyPayments;
    }
}
const Web3 = require('web3');
const web3 = new Web3(new Web3.providers.HttpProvider('https://bsc-dataseed.binance.org/'));

const contractAddress = '0x...';
const contractAbi = [...];
const contractBytecode = '0x...';

const deployContract = async () => {
  const accounts = await web3.eth.getAccounts();
  const contract = new web3.eth.Contract(contractAbi);
  const deployedContract = await contract.deploy({
    data: contractBytecode,
  })
    .send({
      from: accounts[0],
      gas: '2000000',
    });
  console.log(deployedContract.options.address);
};

deployContract();
