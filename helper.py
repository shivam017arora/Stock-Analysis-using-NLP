from transformers import PegasusTokenizer, PegasusForConditionalGeneration
from bs4 import BeautifulSoup
import requests
import re


class Modules:
    def __init__(self):
        self.model_name = "human-centered-summarization/financial-summarization-pegasus"
        self.tokenizer = PegasusTokenizer.from_pretrained(self.model_name)
        self.model = PegasusForConditionalGeneration.from_pretrained(self.model_name)

    def search_for_stock_news_urls(self, ticker):
        search_url = "https://www.google.com/search?q=yahoo+finance+{}&tbm=nws".format(
            ticker
        )
        r = requests.get(search_url)
        soup = BeautifulSoup(r.text, "html.parser")
        atags = soup.find_all("a")
        hrefs = [link["href"] for link in atags]
        return hrefs

    def strip_unwanted_urls(self, urls, exclude_list):
        val = []
        for url in urls:
            if "https://" in url and not any(
                exclude_word in url for exclude_word in exclude_list
            ):
                res = re.findall(r"(https?://\S+)", url)[0].split("&")[0]
                val.append(res)
        return list(set(val))

    def scrape_and_process(self, URLs):
        ARTICLES = []
        for url in URLs:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            paragraphs = soup.find_all("p")
            text = [paragraph.text for paragraph in paragraphs]
            words = " ".join(text).split(" ")[:300]
            ARTICLE = " ".join(words)
            ARTICLES.append(ARTICLE)
        return ARTICLES

    def summarize(self, articles):
        summaries = []
        for article in articles:
            input_ids = self.tokenizer.encode(article, return_tensors="pt")
            output = self.model.generate(
                input_ids, max_length=55, num_beams=5, early_stopping=True
            )
            summary = self.tokenizer.decode(output[0], skip_special_tokens=True)
            summaries.append(summary)
        return summaries

    def create_output_array(self, summaries, scores, urls, monitored_tickers):
        output = []
        for ticker in monitored_tickers:
            for counter in range(len(summaries[ticker])):
                output_this = [
                    ticker,
                    summaries[ticker][counter],
                    scores[ticker][counter]["label"],
                    scores[ticker][counter]["score"],
                    urls[ticker][counter],
                ]
                output.append(output_this)
        return output
