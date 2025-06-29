import pandas as pd
import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time
import reddit_configs as reddit_configs
import prawcore
from datetime import datetime
import requests
from zoneinfo import ZoneInfo

def run():
    # Initialize Reddit API
    reddit = praw.Reddit(
        client_id='AVVkqH25zWRKhsTricgssQ',
        client_secret='tKn4imj1R0-1c8AvAknPRnEcQ0zDMQ',
        user_agent="WavesApp/0.1 by u/Select_Classroom4435"
    )

    configs = {
        'BTC': {'subreddits': reddit_configs.btc_subreddits, 'keywords': reddit_configs.btc_keywords},
        'ETH': {'subreddits': reddit_configs.eth_subreddits, 'keywords': reddit_configs.eth_keywords},
        'XRP': {'subreddits': reddit_configs.xrp_subreddits, 'keywords': reddit_configs.xrp_keywords},
        'SOL': {'subreddits': reddit_configs.sol_subreddits, 'keywords': reddit_configs.sol_keywords},
    }

    est_hour = datetime.now(ZoneInfo("America/New_York")).replace(minute=0, second=0, microsecond=0)
    time_filter = 'hour'
    limit_posts = 50
    analyzer = SentimentIntensityAnalyzer()
    bulk_payload = []

    for coin, cfg in configs.items():
        rows = []
        used_post_count = 0

        for sr in cfg['subreddits']:
            try:
                for post in reddit.subreddit(sr).top(time_filter=time_filter, limit=limit_posts):
                    text = post.title + "\n\n" + (post.selftext or "")
                    if any(kw.lower() in text.lower() for kw in cfg['keywords']):
                        vs = analyzer.polarity_scores(text)
                        used_post_count += 1
                        rows.append({
                            'subreddit': sr,
                            'compound':  vs['compound'],
                            'positive':  vs['pos'],
                            'neutral':   vs['neu'],
                            'negative':  vs['neg'],
                        })
            except prawcore.exceptions.Redirect:
                print(f"[!] r/{sr} not found, skipping.")
                continue

        if rows:
            df = pd.DataFrame(rows)
            id = datetime.now().strftime("%Y%m%d%H%M%S") + coin
            pos = df.positive.mean()
            neu = df.neutral.mean()
            neg = df.negative.mean()

            payload = {
                "id": id,
                "Symbol": coin,
                "Date": est_hour.isoformat(),
                "PositiveReddit": pos,
                "NeutralReddit": neu,
                "NegativeReddit": neg,
                "PostCountReddit": used_post_count
            }

            bulk_payload.append(payload)

        else:
            print(f"{coin}: no valid posts found.")
        time.sleep(5)

    if bulk_payload:
        url = "https://cryptocurrency.azurewebsites.net/api/Sentiment/bulk"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=bulk_payload, headers=headers, timeout=10)
        print(f"Bulk Sentiment POST Status: {response.status_code}")
    else:
        print("No sentiment data to send.")
