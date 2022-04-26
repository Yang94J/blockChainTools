from web3 import Web3
n,n_suffix = [int(_) for _ in input("generating X accounts with Y same suffix : ").split()]
count = 0
w3 = Web3()
while count < n:
    acc = w3.eth.account.create()
    addr = acc.address
    if addr[-n_suffix:] == addr[-1]*n_suffix:
        print("The address is {} with private key {}".format(addr,acc.key.hex())) 
        count += 1
print("Generation Finished")
