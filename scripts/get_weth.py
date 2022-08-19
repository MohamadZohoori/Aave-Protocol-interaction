from brownie import accounts, config, network, interface

from scripts.helpful_scripts import get_account

def main():
    """
    Runs the get_weth function to get WETH
    """
    get_weth()


def get_weth(account=None):
    """
    Mints WETH by depositing ETH.
    """
    account = get_account()
    weth = interface.Weth(
        config["networks"][network.show_active()]["weth_token"]
    )
    tx = weth.deposit({"from": account, "value": 0.1 * 1e18})
    print("Received 0.1 WETH")
    return tx