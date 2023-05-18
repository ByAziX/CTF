from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

web3 = Web3(HTTPProvider('http://62.171.185.249:8502/'))
web3.middleware_onion.inject(geth_poa_middleware, layer=0) 

addresses = ['0xA4dEcDE5c65D94B2A984346dAa5FA37A77F04c2a', '0x7D61eB01524570DfE5763393F8c1231058130c92', '0x71693bD81C023374c43D4564a1435f1a1b431C5d', '0xF725679450D89f8b00e5Bb998B6aDBF3c2e0f1AD', '0x3fe60a1Ed7165b9f1319Ddc5EA12d1A01353a717', '0x4f750BD555755Ab66e87B24A2DD28310e37c465c', '0x25540369aE41F5B1a71ddA1dEff53311CDaB3b1B', '0x8c98DDf14543cC791bA2434b4981B429bF3132c4', '0xBEe1C37253095EDFb677D9DFae301293D9d4F18a', '0xf8C7c772F13c75BE6B9f854Bd12C99c8cE19D2d2', '0x290B7365F8D771d76Cc8ff8aae1C7DF858bf9AEc', '0x46bACe73B5e743a83ea20dE05C4CE8191aae8c05', '0xbDF024D8504C630106d18acD6d470C96B326a7aB']

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