from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

web3 = Web3(HTTPProvider('http://62.171.185.249:8502/'))
web3.middleware_onion.inject(geth_poa_middleware, layer=0) 

addresses = ['0x2626e2C853b1F94c012DF03b595BDfb212914b0f', '0x2626e2C853b1F94c012DF03b595BDfb212914b0f', '0x2626e2C853b1F94c012DF03b595BDfb212914b0f', '0x2626e2C853b1F94c012DF03b595BDfb212914b0f', '0xFfb0c469144D9F187E77C6089B1a882A1E6e832C', '0xFfb0c469144D9F187E77C6089B1a882A1E6e832C', '0xe08384432816c029CC8365Df4B2d09fdFaC8640f', '0xe08384432816c029CC8365Df4B2d09fdFaC8640f', '0xe08384432816c029CC8365Df4B2d09fdFaC8640f', '0xe9fD7987d94596E70450e184a30176FEef440EbE', '0xe9fD7987d94596E70450e184a30176FEef440EbE', '0xe9fD7987d94596E70450e184a30176FEef440EbE', '0xe9fD7987d94596E70450e184a30176FEef440EbE']


funded_by = []

for block in range(860,1000):
    print(block)
    txns = web3.eth.get_block(block).transactions
    #print(txns)
    for txn in txns:
        txn = txn.hex()
        txn_data = web3.eth.get_transaction(txn)
        #print(txn_data['to'])
        if txn_data['to'] in addresses:
            print(txn_data)
            funded_by.append(txn_data['from'])
print("Addresses that funded those addresses :", funded_by)