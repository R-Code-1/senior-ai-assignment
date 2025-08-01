from google_play_scraper import reviews, Sort
import json, os
def fetch_daily_reviews(app_id, date_str, count=200):
    rvws, _ = reviews(app_id, lang='en', country='in', sort=Sort.NEWEST, count=count)
    os.makedirs('data/raw_reviews', exist_ok=True)
    with open(f"data/raw_reviews/{date_str}.json", "w") as f:
        json.dump(rvws, f, indent=2)
    return rvws