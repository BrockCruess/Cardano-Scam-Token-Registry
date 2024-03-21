# Cardano Scam Token Registry

Some closed-source wallets are building their own privately-managed and incomplete scam token registries of their own. They didn't bother reaching out to partner with the community-built `$sendscams` quarantine wallet that the community has been contributing to in order to track scam tokens since the start of their appearances.

Their private registries lack many of the scam tokens that the community has already quarantined in `$sendscams`. To ensure the community has a complete registry that is moderated by the community themselves, the **Cardano Scam Token Registry** has been created. Any active community members (that could be you!) may reach out to become a github contributor and help moderate the submitted tokens.

Most importantly, any Cardano user can now contribute to the community-run **Scam Token Registry** simply by sending scam tokens from their wallet to `$sendscams` - no GitHub login or permissions required.

## How Does It Work?
A bot is monitoring every incoming token to the `$sendscams` wallet address. The Asset ID of each token is appended hashed-out to the `scam-token-list` file in the GitHub repo. Already existing token Asset IDs are ignored. Contributors to the GitHub repo will review newly appended token Asset IDs to determine whether they're malicious or valid. Malicious tokens will be committed (hash mark removed). Pre-existing scam tokens in the wallet have been manually added.

## Community Helps Community
Anyone in the community can use this registry to create their own scam token detection tool. Wallets can use it to create a warning feature for scam tokens. Marketplaces can use it to filter out scam tokens entirely from their platform.

## Become a Contributor
If anyone would like to contribute please reach out to @BrockCardano on Twitter, if you're an active community member you can help moderate token submissions.
