from django.shortcuts import render
from web3 import Web3
def get_wallet_balance(wallet_address):
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/ddbbf46d32a340729806c0de8f417d09'))
    checksum_address = w3.to_checksum_address(wallet_address)
    balance_wei = w3.eth.get_balance(checksum_address)
    balance_eth = w3.from_wei(balance_wei, 'ether')
    return balance_eth
import requests
def get_recent_transactions(wallet_address):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={wallet_address}&sort=desc&apikey=NHJBTC97R9N7Y9YJYPMAPQ1WPKG8PINMAP"
    
    response = requests.get(url)
    tx_list = []
    if response.status_code == 200:
        tx_data = response.json()['result']
        for i in range(min(len(tx_data), 3)):
            tx_dict = {}
            tx_dict['hash'] = tx_data[i]['hash']
            tx_dict['from'] = tx_data[i]['from']
            tx_dict['to'] = tx_data[i]['to']
            tx_dict['value'] = int(tx_data[i]['value']) / pow(10,18)
            tx_list.append(tx_dict)

    return tx_list

def fetch_wallet(request):
    if request.method == 'POST':
        wallet_address = request.POST.get('wallet_address')
        balance = get_wallet_balance(wallet_address)
        transactions = get_recent_transactions(wallet_address)
        return render(request, 'wallet.html', {'balance': balance, 'transactions': transactions, 'wallet_address': wallet_address})
    return render(request, 'fetch.html')