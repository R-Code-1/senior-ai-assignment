from collections import defaultdict
import pandas as pd
def update_trend(trend, topic, date):
    trend[topic][date] += 1
def save_trend_report(trend, path="output/trend_report.csv"):
    df = pd.DataFrame(trend).T.fillna(0).astype(int)
    df.index.name = "Topic"
    df.to_csv(path)