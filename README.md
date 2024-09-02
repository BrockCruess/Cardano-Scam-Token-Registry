# The Cardano Scam Token Registry

<img align="right" src="https://i.imgur.com/wnXIsuX.jpeg" width="300">

The Cardano Community has been contributing scam tokens to `$sendscams` since the start of their appearances on the network to create a central point where all scam tokens are sent to and kept track of. This community-driven effort is far more efficient than private, proprietary registries that some wallets have opted to create for themselves. Their private registries are typically missing many of the tokens that the community has already discovered and submitted to `sendscams`.

To ensure the community has a complete registry that is moderated by the community themselves, the **Cardano Scam Token Registry** has been created. Any active community members (that could be you!) may reach out to become a GitHub contributor and help moderate the submitted tokens.

Most importantly, any Cardano user can now contribute to the community-run **Scam Token Registry** simply by sending scam tokens from their wallet to `$sendscams` - no GitHub login or permissions required.

## How Does It Work?
A bot monitors every incoming token to the `$sendscams` wallet address. The CIP-14 Asset Fingerprint of each token is appended hashed-out to the `scam-token-list` file in the GitHub repo. Already existing token asset fingerprints are ignored. Contributors to the GitHub repo can then review newly appended token asset fingerprints to determine whether they're malicious or valid. Malicious tokens are committed (hash mark removed). Valid tokens are left hashed-out to prevent future duplicate reviews. Scam tokens that were sent to the the wallet before the bot was created were manually added so the list is up-to-date.

## Community Helps Community
Anyone in the community can use this registry to create their own scam token detection tool. Wallets can use it to create a warning feature for scam tokens. Marketplaces can use it to filter out scam tokens entirely from their platform. The formatting of the registry is intentionally very simple, line-separated and ignorable lines hashed out, so that it can easily be handled by any backend.

> [!TIP]
> Example Scam Token parsing using Python:
> ```
>import aiohttp
>
>url = "https://raw.githubusercontent.com/BrockCruess/Cardano-Scam-Token-Registry/main/scam-token-list"
>
>async def check_token(assetid):
>    async with aiohttp.ClientSession() as session:
>        async with session.get(url) as response:
>            if response.status == 200:
>                data = await response.text()
>                scam_tokens = [line.strip() for line in data.split("\n") if line.strip() and not line.startswith("#")]
>                if assetid in scam_tokens:
>                    print(f"{assetid} is flagged as a known malicious token.")
>                else:
>                    print(f"{assetid} is not flagged as a known malicious token.")
>            else:
>                print("Failed to retrieve the Cardano Scam Token Registry list.")
>
># Example usage
>token = "asset12345example"
>await check_token(assetid)
>```

## Become a Contributor
If anyone would like to contribute please join the [Community Review Discord server](https://discord.gg/hqwvvR6KpM), if you're an active community member you can help moderate token submissions.
