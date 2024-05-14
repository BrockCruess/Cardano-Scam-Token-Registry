# The Cardano Scam Token Registry

<img align="right" src="https://i.imgur.com/wnXIsuX.jpeg" width="300">

Some closed-source wallets are building their own privately-managed and incomplete scam token registries of their own. They didn't bother reaching out to partner with the community-built `$sendscams` quarantine wallet that the community has been contributing to in order to track scam tokens since the start of their appearances.

Their private registries lack many of the scam tokens that the community has already quarantined in `$sendscams`. To ensure the community has a complete registry that is moderated by the community themselves, the **Cardano Scam Token Registry** has been created. Any active community members (that could be you!) may reach out to become a github contributor and help moderate the submitted tokens.

Most importantly, any Cardano user can now contribute to the community-run **Scam Token Registry** simply by sending scam tokens from their wallet to `$sendscams` - no GitHub login or permissions required.

## How Does It Work?
A bot monitors every incoming token to the `$sendscams` wallet address. The CIP-14 Asset Fingerprint of each token is appended hashed-out to the `scam-token-list` file in the GitHub repo. Already existing token asset fingerprints are ignored. Contributors to the GitHub repo can then review newly appended token asset fingerprints to determine whether they're malicious or valid. Malicious tokens are committed (hash mark removed). Valid tokens are left hashed-out to prevent future duplicate reviews. Scam tokens that were sent to the the wallet before the bot was created were manually added so the list is up-to-date.

## Community Helps Community
Anyone in the community can use this registry to create their own scam token detection tool. Wallets can use it to create a warning feature for scam tokens. Marketplaces can use it to filter out scam tokens entirely from their platform.

## Become a Contributor
If anyone would like to contribute please join the [Community Review Discord server](https://discord.gg/hqwvvR6KpM), if you're an active community member you can help moderate token submissions.
