from utils.fetch_reviews import fetch_daily_reviews
from agents.review_agent import classify_review
from agents.topic_consolidation_agent import TopicManager
from utils.trend_utils import update_trend, save_trend_report
from datetime import date, timedelta
from collections import defaultdict
trend = defaultdict(lambda: defaultdict(int))
tm = TopicManager()
tm.load_seed_topics(["Delivery issue","Food stale","Delivery partner rude", "Maps not working properly"])
start, end = date(2024, 6, 1), date(2024, 6, 5)
app_id = "in.swiggy.android"
for d in (start + timedelta(days=i) for i in range((end-start).days+1)):
    dt = d.isoformat()
    rvws = fetch_daily_reviews(app_id, dt, count=10)
    for r in rvws:
        info = classify_review(r['content'])
        topic = tm.map_topic(info['topic'])
        update_trend(trend, topic, dt)
save_trend_report(trend)