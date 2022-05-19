# Project Description:

In this project, I built an automated stock-analysis script using Python and Deep-Learning to do the following:

1. Scrape articles for the tickers mentioned in the arguments
2. Generate summaries of the articles using Pegasus's Model
   (reference: https://huggingface.co/human-centered-summarization/financial-summarization-pegasus)
   <i> This model was fine-tuned on a novel financial news dataset, which consists of 2K articles from Bloomberg, on topics such as stock, markets, currencies, rate and cryptocurrencies. <i>
3. Generate sentiment and export in CSV

How we're doing it?

1. Scrape news from google news using Beautiful Soup using Ticker codes
2. Summarise each article using HuggingFace Transfomers
3. Generate sentiment and confidence values and export to CSV
