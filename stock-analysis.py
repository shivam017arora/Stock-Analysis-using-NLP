import argparse
import csv

from transformers import pipeline
from helper import Modules

modules = Modules()

parser = argparse.ArgumentParser(
    description="Stock Analysis using NLP",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

parser.add_argument(
    "--tickers",
    type=str,
    nargs="+",
    help="Tickers to monitor",
    default=["AAPL", "MSFT", "AMZN", "FB", "GOOGL", "TSLA"],
)

args = parser.parse_args()
config = vars(args)

monitored_tickers = args.tickers

print("TICKERS TO MONITOR: ", monitored_tickers)

raw_urls = {
    ticker: modules.search_for_stock_news_urls(ticker) for ticker in monitored_tickers
}

exclude_list = ["maps", "policies", "preferences", "accounts", "support"]

cleaned_urls = {
    ticker: modules.strip_unwanted_urls(raw_urls[ticker], exclude_list)
    for ticker in monitored_tickers
}

articles = {
    ticker: modules.scrape_and_process(cleaned_urls[ticker])
    for ticker in monitored_tickers
}

print("SUMMARIZING ARTICLES")
summaries = {
    ticker: modules.summarize(articles[ticker]) for ticker in monitored_tickers
}

print("COMPUTING SENTIMENT")
sentiment = pipeline("sentiment-analysis")
scores = {ticker: sentiment(summaries[ticker]) for ticker in monitored_tickers}


final_output = modules.create_output_array(
    summaries, scores, cleaned_urls, monitored_tickers
)
with open("summary.csv", mode="w", newline="") as f:
    csv_writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerows(final_output)

print("DONE; Check summary.csv")
