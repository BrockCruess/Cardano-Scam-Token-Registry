# The $sendscams Bot
### `$sendscams` wallet watcher and new token submission handler of the Cardano Scam Token Registry

## What does the bot do?
This bot monitors every incoming token to the `$sendscams` wallet address. The [CIP-14](https://github.com/cardano-foundation/CIPs/tree/master/CIP-0014) asset fingerprint of each new token is appended hashed-out to the `scam-token-list` file in the **Cardano Scam Token Registry** GitHub repo. Already existing token asset fingerprints are ignored. Contributors to the GitHub repo can then review newly appended token asset fingerprints to determine whether they're malicious or valid. Malicious tokens are committed (hash mark removed). Valid tokens are left hashed-out to prevent future duplicate reviews.

An instance of the bot is always running on a BROCK Pool node, however having instances of the bot running elsewhere helps prevent any notable outages. The bot looks back 20 transactions (increasable in the bot's code) each time it checks the wallet's incoming transactions (every 20 seconds), so even if all instances of the bot go down at once, upon restart it's most likely that any tokens that were received during that down time will be picked up by the bot upon restart. Bots will not double-submit token fingerprints, as they always check if the fingerprint exists in the list already before submitting, and one bot is almost always sure to process a new transaction before the others. Worst case, they submit the exact same update a few milliseconds apart - not a real issue.

## Who can run the bot?
Any GitHub users who have been added as a contributor to this repo may run the bot with their [GitHub API Token](https://github.com/settings/tokens/new) and a [CardanoScan API Key](https://cardanoscan.io/api#pricingSection) (free tier works fine).

## Bot setup:

1. Download all of the files in this folder

2. Update `cardanoscan.api` and `github.api` with your own key and token.

3. Install Python 3 or newer
  
4. Install the required Python packages:
```
pip install requests aiohttp bech32
```

5. Run the Python script with whichever of these commands applies to your system:
```
python sendscams-bot.py
```
```
python3 sendscams-bot.py
```

It's recommended to put the start command in an executable script (.bat on Windows or .sh on Linux etc.) then make that script run on system startup (add a shortcut to startup apps on Windows or a make a systemd service on Linux etc.)
