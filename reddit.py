import praw
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time
import reddit_configs
import prawcore
from datetime import datetime

# Create Reddit API instance using your app credentials
reddit = praw.Reddit(
    client_id='AVVkqH25zWRKhsTricgssQ',
    client_secret='tKn4imj1R0-1c8AvAknPRnEcQ0zDMQ',
    user_agent="WavesApp/0.1 by u/Select_Classroom4435"
)

# 2) Configuration per coin
configs = {
    'BTC': {
        'subreddits': reddit_configs.btc_subreddits,
        'keywords':   reddit_configs.btc_keywords,
    },
    'ETH': {
        'subreddits': reddit_configs.eth_subreddits,
        'keywords':   reddit_configs.eth_keywords,
    },
    'XRP': {
        'subreddits': reddit_configs.xrp_subreddits,
        'keywords':   reddit_configs.xrp_keywords,
    },
    'SOL': {
        'subreddits': reddit_configs.sol_subreddits,
        'keywords':   reddit_configs.sol_keywords,
    },
}


time_filter = 'hour'
limit_posts = 50
analyzer = SentimentIntensityAnalyzer()

used_post_count = 0
# 3) Loop through each coin
for coin, cfg in configs.items():
    rows = []
    for sr in cfg['subreddits']:
        try:
            # both the call *and* the iteration live inside the try
            for post in reddit.subreddit(sr).top(time_filter=time_filter, limit=limit_posts):
                text = post.title + "\n\n" + (post.selftext or "")
                if any(kw.lower() in text.lower() for kw in cfg['keywords']):
                    vs = analyzer.polarity_scores(text)
                    rows.append(vs)
                    used_post_count += 1
                    rows.append({
                        'subreddit': sr,
                        'compound':  vs['compound'],
                        'positive':  vs['pos'],
                        'neutral':   vs['neu'],
                        'negative':  vs['neg'],
                    })
        except prawcore.exceptions.Redirect:
            print(f"[!] r/{sr} not found (Redirect), skipping.")
            continue

    df = pd.DataFrame(rows)
    if not df.empty:
        id = str(datetime.now().strftime("%Y%m%d%H%M%S")) + coin
        print(id)
        print(f"{coin} sentiment (from {used_post_count} matching posts):")
        print(f"{coin}: pos={df.positive.mean():.3f}, "
              f"neu={df.neutral.mean():.3f}, "
              f"neg={df.negative.mean():.3f}")
    else:
        print(f"{coin}: no valid posts found.")
    time.sleep(5)