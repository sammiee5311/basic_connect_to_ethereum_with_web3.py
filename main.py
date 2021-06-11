from web import Web

w = Web()

web3 = w.connect_to_web3()
ABI = w.get_abi()
ADDRESS = '0x7E8351C38B1Df4366D3ED05A3a8C96340e80De25' # smart contract address


try:
    account = web3.eth.accounts[0] # main account
    if ABI:
        contract = web3.eth.contract(address=ADDRESS, abi=ABI)
        print(contract.functions.say().call())
        contract.functions.setGreeting('Hello World').transact({'from': account})

except AttributeError:
    print('web3 is not connected. Please, check your IP address or PORT')


