# 2) Configuration
btc_subreddits = [
    'BitcoinMarkets',        # Trading strategies & market discussion :contentReference[oaicite:0]{index=0}
    'BTC',                   # Free speech Bitcoin fork community :contentReference[oaicite:1]{index=1}
    'BitcoinBeginners',      # Newbie Q&A including how/where to buy :contentReference[oaicite:2]{index=2}
    'CryptoMarkets',         # Crypto finance discussion, incl. BTC :contentReference[oaicite:3]{index=3}
    'LocalBitcoins',         # P2P Bitcoin marketplace :contentReference[oaicite:4]{index=4}
    'bitcointrading',        # Peer-to-peer crypto trading discussion :contentReference[oaicite:5]{index=5}
    'CryptoCurrencyTrading', # Trading strategies for all cryptos, incl. BTC :contentReference[oaicite:6]{index=6}
    'CryptoCurrency',        # General crypto discussion, heavy BTC coverage :contentReference[oaicite:7]{index=7}
    'BitcoinUK',             # UK-focused BTC buy/sell discussion :contentReference[oaicite:8]{index=8}
    'BitcoinCA',             # Canada-focused BTC discussion & P2P options :contentReference[oaicite:9]{index=9}
    'BitcoinAUS',            # Australia-focused Bitcoin community :contentReference[oaicite:10]{index=10}
    'Bitcoin_News',          # News-only Bitcoin updates :contentReference[oaicite:11]{index=11}
    'Paxful',                # Peer-to-peer Bitcoin marketplace community :contentReference[oaicite:12]{index=12}
    'BitMarket',             # Marketplace for crypto assets including BTC :contentReference[oaicite:13]{index=13}
    'NZBitcoin',             # New Zealand Bitcoin buy/sell & payments :contentReference[oaicite:14]{index=14}
    'BitcoinDiscussion',     # Off-topic BTC chat, incl. trading experiences :contentReference[oaicite:15]{index=15}
    'BitcoinTradingSignals', # Signal calls for BTC trading :contentReference[oaicite:16]{index=16}
    'binance',               # Exchange community (BTC pairs, fees, tips) :contentReference[oaicite:17]{index=17}
    'Coinbase',              # Coinbase support/community (how to buy BTC) :contentReference[oaicite:18]{index=18}
    'kucoin',                # KuCoin exchange community (BTC orders/tips) :contentReference[oaicite:19]{index=19}
    'Jobs4Bitcoins',         # Earn BTC through work, exposes P2P options :contentReference[oaicite:20]{index=20}
    'CryptoIndia',           # Indian crypto P2P & exchange talk, includes BTC :contentReference[oaicite:21]{index=21}
    'altcoin',               # Broad crypto trading talk (often covers BTC) :contentReference[oaicite:22]{index=22}
    'TheLightningNetwork',   # BTC off-chain payments network & discussions :contentReference[oaicite:23]{index=23}
]
   
btc_keywords   = keywords = [
    'buy', 'sell', 'hold', 'bearish', 'bullish', 'BTC', 'Bitcoin',
    # Slang & memes
    'hodl', 'moon', 'pump', 'dump', 'fomo', 'fud', 'rekt',
    # Technical‐analysis terms
    'long', 'short', 'breakout', 'breakdown', 'resistance',
    'support', 'volume', 'rsi', 'macd', 'atr',
    # Market phases & events
    'rally', 'correction', 'dump', 'sell-off', 'bounce',
    'whale', 'ath', 'all-time high', 'slump'
] # words to filter on

eth_subreddits = [
   'EthTrader',             # ✅ Highly active ETH trading community :contentReference[oaicite:1]{index=1}
    'Ethereum',              # ✅ Official ETH subreddit, price & news :contentReference[oaicite:2]{index=2}
    'CryptoMarkets',         # ✅ General crypto market discussion :contentReference[oaicite:3]{index=3}
    'CryptoCurrencyTrading', # ✅ Crypto trading strategies (includes ETH)
    'CryptoCurrency',        # ✅ Large crypto community, ETH included
    'altcoin',               # ✅ Altcoin trading, frequently covers ETH
    'defi',                  # ✅ DeFi conversation, heavily ETH-based :contentReference[oaicite:4]{index=4}
    'EthFinance',            # ✅ Active (merged) ETH investment community :contentReference[oaicite:5]{index=5}
    'ethstaker'              # ✅ ETH staking discussion community :contentReference[oaicite:6]{index=6}
]

eth_keywords = keywords = keywords = [
    # Core trading signals
    'buy', 'sell', 'hold', 'bullish', 'bearish',

    # Ethereum identifiers
    'ETH', 'Ethereum',

    # Protocol upgrades & forks
    'Merge', 'EIP-1559', 'London', 'Shapella', 'Sharding', '2.0',

    # Staking & yield
    'stake', 'staked', 'unstake', 'staking', 'yield', 'APR',

    # DeFi & liquidity
    'DeFi', 'liquidity', 'LP', 'yield farming', 'staking pool',

    # Smart contract & network
    'smart contract', 'gas', 'fees',

    # Slang & hype
    'moon', 'pump', 'dump', 'rekt', 'fomo', 'fud', 'whale',

    # Technical analysis terms
    'long', 'short', 'breakout', 'breakdown', 'support', 'resistance',
    'volume', 'RSI', 'MACD', 'ATR',

    # Milestones & extremes
    'ATH', 'all-time high', 'floor'
]

xrp_subreddits = [
    'XRP',                       # ✅ Main XRP community, public and active :contentReference[oaicite:1]{index=1}
    'Ripple',                    # ✅ Ripple ecosystem community :contentReference[oaicite:2]{index=2}
    'xrptrading',                # ✅ XRP trading-focused subreddit :contentReference[oaicite:3]{index=3}
    'XRPLedger',                 # ✅ XRP Ledger protocol discussions :contentReference[oaicite:4]{index=4}
    'Ripplexrp',                 # ✅ XRP community (developer-focused) :contentReference[oaicite:5]{index=5}
    'CryptoCurrency',       # ✅ Broad crypto discussion (includes SOL) :contentReference[oaicite:8]{index=8}
    'CryptoMarkets',        # ✅ Market analysis for all cryptos :contentReference[oaicite:9]{index=9}
]

xrp_keywords = keywords = [
    # Core trading signals
    'buy', 'sell', 'hold', 'bullish', 'bearish',

    # XRP identifiers
    'XRP', 'Ripple',

    # Protocol upgrades & forks
    'XLS-20', 'Hooks', 'Federated Sidechains',

    # Staking & yield
    'stake', 'staked', 'unstake', 'staking', 'yield', 'APR',

    # DeFi & liquidity
    'DeFi', 'liquidity', 'LP', 'yield farming',

    # Slang & hype
    'moon', 'pump', 'dump', 'rekt', 'fomo', 'fud', 'whale',

    # Technical analysis terms
    'long', 'short', 'breakout', 'breakdown', 'support', 'resistance',
    'volume', 'RSI', 'MACD', 'ATR',

    # Milestones & extremes
    'ATH', 'all-time high'
]

sol_subreddits = [
    'solana',               # ✅ Official Solana community :contentReference[oaicite:1]{index=1}
    'SolanaIndia',          # ✅ Public regional Solana community :contentReference[oaicite:2]{index=2}
    'Solana_Memes',         # ✅ Meme culture around Solana :contentReference[oaicite:3]{index=3}
    'SolanaMemeCoins',      # ✅ Public memecoin trading group :contentReference[oaicite:4]{index=4}
    'SolCoins',             # ✅ Larger memecoin community :contentReference[oaicite:5]{index=5}
    'SolanaPresale',        # ✅ Presale-focused community :contentReference[oaicite:6]{index=6}
    'SolanaDeFi',           # ✅ Verified DeFi-focused discussion
    'CryptoCurrency',       # ✅ Broad crypto discussion (includes SOL) :contentReference[oaicite:8]{index=8}
    'CryptoMarkets',        # ✅ Market analysis for all cryptos :contentReference[oaicite:9]{index=9}
]


sol_keywords = keywords = [
    # Core trading signals
    'buy', 'sell', 'hold', 'bullish', 'bearish',

    # Solana identifiers
    'SOL', 'Solana',

    # Protocol upgrades & forks
    'Sealevel', 'Gulfstream', 'Turbine', 'Pipelining',

    # Staking & yield
    'stake', 'staked', 'unstake', 'staking', 'yield', 'APR',

    # DeFi & liquidity
    'DeFi', 'liquidity', 'LP', 'yield farming',

    # Slang & hype
    'moon', 'pump', 'dump', 'rekt', 'fomo', 'fud', 'whale',

    # Technical analysis terms
    'long', 'short', 'breakout', 'breakdown', 'support', 'resistance',
    'volume', 'RSI', 'MACD', 'ATR',

    # Milestones & extremes
    'ATH', 'all-time high'
]