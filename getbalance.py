from pycoingecko import CoinGeckoAPI
from web3 import Web3, middleware
from pycoingecko import CoinGeckoAPI
import time
from colorama import init, Fore, Style
init()
# Replace 'https://bsc-dataseed.binance.org/' with the BSC node endpoint you want to connect to
bsc_node_url = 'https://bsc-dataseed.binance.org/'

# Create a Web3 instance and add the geth_poa_middleware
web3 = Web3(Web3.HTTPProvider(bsc_node_url))
cg = CoinGeckoAPI()
# Replace this with the ERC20 ABI for your specific token
ERC20_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

def get_bnb_balance(wallet_address):
    try:
        bnb_balance = web3.eth.get_balance(wallet_address)
        return bnb_balance / 1e18  # Convert from Wei to BNB
    except Exception as e:
        print(f"Error retrieving BNB balance for address {wallet_address}: {e}")
        return None

def get_bnb_price():
    try:
        bnb_data = cg.get_price(ids='binancecoin', vs_currencies='usd')
        bnb_price = bnb_data['binancecoin']['usd']
        return bnb_price
    except Exception as e:
        print("Error retrieving BNB price:", e)
        return None

def get_token_balance(token_address, wallet_address):
    # Load the contract for the token using the address
    contract = web3.eth.contract(address=token_address, abi=ERC20_ABI)

    # Get the balance of the wallet address for the specified token
    balance = contract.functions.balanceOf(wallet_address).call()

    # Convert the balance from the token's decimals to the actual balance
    decimals = contract.functions.decimals().call()
    actual_balance = balance / (10 ** decimals)

    return actual_balance

if __name__ == "__main__":
    token_address = ""  # Replace this with the token's contract address
    wallet_addresses = [
"",# Replace this with the address
"",
"",
"",
"",
"",
"",
""
    ]

    token_name = ""
    token_symbol = ""
    try:
        # Get the token name and symbol if possible
        contract = web3.eth.contract(address=token_address, abi=ERC20_ABI)
        token_name = contract.functions.name().call()
        token_symbol = contract.functions.symbol().call()
    except Exception as e:
        print("Error retrieving token details:", e)
    print(f"{Fore.WHITE}-------------------------------------------------------{Style.BRIGHT}")
    print(f"Token Information:{Fore.BLUE}{Style.BRIGHT}")
    print(f"Name: {token_name}{Fore.GREEN}{Style.BRIGHT}")
    print(f"Symbol: {token_symbol}{Fore.CYAN}{Style.BRIGHT}")
    print(f"Contract Address: {token_address}\n")
    print(f"{Fore.WHITE}-------------------------------------------------------{Style.BRIGHT}")

    bnb_price = get_bnb_price()
    if bnb_price:
        print(f"BNB Price in USD: ${bnb_price:.2f}\n")


    # Get the total value in USD for each wallet address
    for address in wallet_addresses:
        token_balance = get_token_balance(token_address, address)
        print(f"Address: {Fore.YELLOW}{address}{Style.BRIGHT}")
        print(f"Token Balance: {Fore.GREEN}{token_balance}{Style.BRIGHT} {Fore.YELLOW}{token_symbol}{Style.BRIGHT}")


        # Convert to Ether (18 decimals)
        ether_balance = token_balance / (10 ** 18)
        print(f"Balance in Ether (18 decimals): {Fore.YELLOW}{ether_balance:.18f} ETH{Style.BRIGHT}")


        # Convert to Wei (0 decimals)
        wei_balance = int(token_balance * (10 ** 18))
        print(f"Balance in Wei (0 decimals): {Fore.YELLOW}{wei_balance} Wei{Style.BRIGHT}")

        bnb_balance = get_bnb_balance(address)
        if bnb_balance is not None:
            value_in_usd = bnb_balance * bnb_price

            print(f"BNB Balance: {Fore.GREEN}{bnb_balance:.6f} BNB{Style.BRIGHT}")
            print(f"Value in USD: {Fore.YELLOW}${value_in_usd:.2f}{Style.BRIGHT}")

            print(f"{Fore.WHITE}-------------------------------------------------------{Style.BRIGHT}")

            # Calculate the total value by adding the token value and BNB value
            total_value_in_usd = value_in_usd + (token_balance * bnb_price)
            print(f"Total Value in USD: {Fore.GREEN}${total_value_in_usd:.2f}{Style.BRIGHT}\n")
        else:
            print(f"{Fore.RED}Error retrieving BNB balance.{Style.RESET_ALL}\n")

        start_time = time.time()
        for countdown in range(3, 0, -1):
            print(f"\rCountdown: {countdown} seconds", end='', flush=True)
            time.sleep(1)
        print("\rCountdown: 0 seconds")
        elapsed_time = round(time.time() - start_time, 2)
        print(f"Elapsed Time: {elapsed_time} seconds")
        time.sleep(1)

        # Add box lines for total value information display
        print(f"{Fore.WHITE}-------------------------------------------------------{Style.BRIGHT}")
        print(f"Total Value in USD: {Fore.GREEN}${total_value_in_usd:.2f}{Style.BRIGHT}\n")
