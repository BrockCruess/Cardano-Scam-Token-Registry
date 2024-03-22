import requests
import asyncio
import aiohttp
import json
import time
import base64
import hashlib
import binascii
import bech32

# Function to read API key from file
def read_cardanoscan_api_key():
    try:
        with open('cardanoscan.api', 'r') as file:
            return file.read().strip()
    except Exception as e:
        log_error(f"Error reading cardanoscan.api file: {str(e)}")
        return None

# Function to read GitHub API token from file
def read_github_api_token():
    try:
        with open('github.api', 'r') as file:
            return file.read().strip()
    except Exception as e:
        log_error(f"Error reading github.api file: {str(e)}")
        return None

# Function to read wallet address from file
def read_wallet_address():
    try:
        with open('wallet.addr', 'r') as file:
            return file.read().strip()
    except Exception as e:
        log_error(f"Error reading wallet.addr file: {str(e)}")
        return None

# Function to log errors
def log_error(error_message):
    # errors.log file path
    try:
        with open('errors.log', 'a') as file:
            file.write(f"\n{time.strftime('%Y-%m-%d %H:%M:%S')} - {error_message}")
    except Exception as e:
        print(f"Error logging to errors.log: {str(e)}")

# Function to log transactions
def log_transaction(transaction_hash):
    # tx.list file path
    try:
        with open('tx.list', 'a') as file:
            file.write(f"\n{transaction_hash}")
    except Exception as e:
        log_error(f"Error logging transaction to tx.list: {str(e)}")

# tx.list file path
transaction_list = "tx.list"

#########################################################################################################
# The above file paths are relative to this script's location.
# If running the script with a different working directory you may replace them with absolute file paths.
#########################################################################################################

# Function to start the transaction checking loop
async def start_transaction_check():
    while True:
        await check_transactions()
        await asyncio.sleep(20) # Check for new transactions every 20 seconds (every block)

async def check_transactions():
    try:
        api_key = read_cardanoscan_api_key()
        wallet_address = read_wallet_address()

        url = f"https://api.cardanoscan.io/api/v1/transaction/list?address={wallet_address}&pageNo=1&limit=20&order=desc"
        headers = {'apiKey': api_key}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                data = await response.json()

        if 'transactions' in data:
            for transaction in data['transactions']:
                transaction_hash = transaction['hash']
                if transaction_hash not in open(transaction_list).read():
                    log_transaction(transaction_hash)
                    await process_transaction(transaction, wallet_address)

    except aiohttp.ClientError as e:
        log_error(f"HTTP request error: {str(e)}")
    except Exception as e:
        log_error(f"Error checking transactions: {str(e)}")

async def process_transaction(transaction, wallet_address):
    try:
        wallet_involved = any(inp['address'] == wallet_address for inp in transaction['inputs'])
        if not wallet_involved:
            for output in transaction['outputs']:
                if output['address'] == wallet_address:
                    github_api_token = read_github_api_token()
                    if github_api_token:
                        for token in output.get('tokens', []):
                            policy_id = token.get('policyId')
                            asset_name = token.get('assetName')
                            if policy_id and asset_name:
                                asset_fingerprint = create_asset_fingerprint(policy_id, asset_name)
                                await append_asset_fingerprint_to_github(asset_fingerprint, github_api_token)
                            else:
                                print("No policyId or assetName detected.")  # Debug print

    except Exception as e:
        log_error(f"Error processing transaction: {str(e)}")

def create_asset_fingerprint(policy_id, asset_name):
    # Concatenate policy_id and asset_name
    message = policy_id + asset_name
    # Hash the concatenated string using blake2b algorithm
    hashed_message = hashlib.blake2b(binascii.unhexlify(message), digest_size=20).digest()
    # Encode the hashed message using Bech32 encoding with 'asset' as human-readable part
    converted_bits = bech32.convertbits(hashed_message, 8, 5)
    asset_fingerprint = bech32.bech32_encode("asset", converted_bits)
    print(f"New token received: {asset_fingerprint}")
    return asset_fingerprint

async def append_asset_fingerprint_to_github(asset_fingerprint, github_api_token):
    try:
        print(f"Appending {asset_fingerprint} to GitHub registry...")  # Debug print

        # Construct the request headers with the GitHub API token
        headers = {'Authorization': f'token {github_api_token}'}

        # Construct the request URL
        url = f'https://api.github.com/repos/BrockCruess/Cardano-Scam-Token-Registry/contents/scam-token-list'

        # Get the existing contents of the file
        response = requests.get(url, headers=headers)
        response_data = response.json()

        # Decode the content from base64
        content = base64.b64decode(response_data['content']).decode('utf-8')

        # Check if the asset fingerprint already exists in the content
        if asset_fingerprint not in content:
            # If content is not empty and last character is not newline, add newline
            if content and content[-1] != '\n':
                content += '\n'
            # Append the new asset fingerprint to the content
            content += f"#{asset_fingerprint}"

            # Encode the content to base64
            encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')

            # Prepare the payload for the request
            payload = {
                "message": "The community has submitted a new token",
                "content": encoded_content,
                "sha": response_data['sha']
            }

            # Make a PUT request to update the GitHub registry file
            response = requests.put(url, headers=headers, data=json.dumps(payload))

            # Check the response status code
            if response.status_code == 200:
                print(f"Asset fingerprint {asset_fingerprint} appended to GitHub registry successfully.")
            else:
                print(f"Failed to append asset fingerprint {asset_fingerprint} to GitHub registry.")
        else:
            print(f"Asset fingerprint {asset_fingerprint} already exists in GitHub registry.")

    except Exception as e:
        log_error(f"Error appending asset fingerprint to GitHub registry: {str(e)}")

# Schedule the transaction checking loop to start
async def main():
    asyncio.create_task(check_transactions())

# Run the main function
asyncio.run(main())
