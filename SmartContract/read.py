import json
from web3 import Web3
from datetime import datetime
from processing.process_query import process_query

def read(ganache_url, path_to_abi, address, server_id, timestamp):
    # ganache_url = 'http://127.0.0.1:7545'
    # path_to_abi = 'abi.json'
    # address = "0x769ec15950f154653F89A3687595df49e6Bea6dD"
    # server_id = 123
    # count = 10

    web3 = Web3(Web3.HTTPProvider(ganache_url))
    web3.eth.defaultAccount = web3.eth.accounts[0]

    abi = json.load(open(path_to_abi))
    address = web3.toChecksumAddress(address)

    contract = web3.eth.contract(address=address,abi=abi)
    
    # Index of data on blockchain
    index = contract.functions.logCount().call()
    latest = timestamp
    assigned = False
    # Reading data from blockchain
    while index:
        output = contract.functions.logs(index).call()
        if output[4] != timestamp:
            if not assigned:
                assigned = True
                latest = output[4]
            process_query(output[2], output[3])
        else:
            break

        print(type(contract.functions.logs(index).call()))
        index -= 1
        # count -= 1
    return latest