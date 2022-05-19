# Project Description:

In this project, I built an automated stock-analysis script using Python and Deep-Learning to do the following:

1. Scrape articles for the tickers mentioned in the arguments
2. Generate summaries of the articles using Pegasus's Model
   (reference: https://huggingface.co/human-centered-summarization/financial-summarization-pegasus)
   <i> This model was fine-tuned on a novel financial news dataset, which consists of 2K articles from Bloomberg, on topics such as stock, markets, currencies, rate and cryptocurrencies. <i>
3. Generate sentiment and export in CSV

How is it done?

1. Scrape news from google news using Beautiful Soup using Ticker codes
2. Summarise each article using HuggingFace Transfomers
3. Generate sentiment and confidence values and export to CSV

# Usage
```
git clone 
python3 stock-analysis.py --tickers <ENTER TICKERS HERE> 
```
   
# Example
```
python3 stock-analysis.py --tickers BTC ETH
```

# Help
```
python3 stock-analysis.py --help
   
usage: stock-analysis.py [-h] [--tickers TICKERS [TICKERS ...]]

Stock Analysis using NLP

options:
  -h, --help            show this help message and exit
  --tickers TICKERS [TICKERS ...]
                        Tickers to monitor (default: ['AAPL', 'MSFT', 'AMZN', 'FB', 'GOOGL', 'TSLA'])
```
   
# Output
   
   <img width="956" alt="Screenshot 2022-05-19 at 12 05 36 PM" src="https://user-images.githubusercontent.com/26146104/169226114-c277556e-9a13-4f4f-887a-6a594f3396fb.png">
