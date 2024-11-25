#!/usr/bin/env python3

import requests
import json

# QuickNode URL for consensus params endpoint
url = "https://public-celestia-rpc.numia.xyz/consensus_params"

# Function to check if the consensus params have timeout field
def has_timeout(consensus_params):
    # Check if 'timeout' exists inside the consensus params object
    if 'timeout' in consensus_params:
        return True
    return False

# Fetching the last 100k consensus params
def fetch_and_filter_consensus_params(url, num_blocks=100000):
    print(f"Fetching last {num_blocks} consensus parameters...")

    # Initialize the block height (start with latest block and decrement)
    current_block = None

    for i in range(num_blocks):
        # Construct the URL for the current block height
        params_url = f"{url}?height={current_block}" if current_block else url

        try:
            # Make the HTTP GET request to fetch consensus params
            response = requests.get(params_url)
            response.raise_for_status()
            data = response.json()
            # print(data)
            # Extract consensus params from the response
            consensus_params = data.get('result', {}).get('consensus_params', {})

            # Check if consensus_params contains the 'timeout' field
            # if has_timeout(consensus_params):
            #     print(f"Block Height {current_block if current_block else 'latest'} has timeout object: {json.dumps(consensus_params, indent=2)}")

            if data.get('result').get('timeout') is not None:
                print("ORCO")
                print(data.get('result').get('timeout'))

            print(data.get('result'))
            # Decrement block height for next iteration (if needed)
            current_block = int(data.get('result').get('block_height')) - 1  # Decrement to get previous block
            print(current_block)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching block {current_block if current_block else 'latest'}: {e}")
            break

# Call the function to fetch and filter consensus parameters
fetch_and_filter_consensus_params(url)
