from brownie import SOMMToken, accounts

def main():
    acct = accounts.load("deployer_account")
    SOMMToken.deploy("Sommelier", "SOMM", {"from":acct})