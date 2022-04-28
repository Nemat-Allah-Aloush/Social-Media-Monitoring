# Social-Media-Monitoring
Social Media Monitoring /Twitter/ in python language.

--- 

## Index
1. [About the project](#about-the-project)
2. [Requirements](#requirements)
3. [Social Media Monitoring Steps](#semantic-search-engine-steps)
4. [Data Processing](#data-processing)
5. [Sentiment Analysis with RNN](#sentiment-analysis-with-rnn)

---

## About the project 
The main goal of this project is to scrape data from Twitter for a specific brand or product and try to classify the tweets sentimatically as negative or positive tweets.


---

## Requirements
Here is a list of some of  the used libraries:
1.	d2l: for building the sentiment analysis model.
2.	demoji: for replacing the emojis in tweets with their description.
3.	snscrape: a library to scrap tweets.
4.	Nltk: for natural language processing.

---
## Social Media Monitoring Steps
In the following figure we can see the main steps of the project:
First of all we should select a string to search for, then we need to scrape Twitter for posts containing that string.
After that, the data will be cleaned, analyzed and presented in a way to show what sentiments are included in the tweets.

![alt text](https://github.com/Nemat-Allah-Aloush/Social-Media-Monitoring/blob/main/imgs/prototype.png "Social Media Monitoring Steps")


---

## Data Processing
After scrapping data from Twitter. The following preprocessing pipeline will be apllied :
1. Cleaning signs:
  - Replacing emojis with their description. 
  - Data collected the web and specially from social media platform contain links and signs like (#) and (@)., we remove those signs.
  - It is important to delete the links, since no sentiments can be discovered from the link text.
  - Deleting punctuation marks and any non-Asci chars.
2. NLP cleaning: 
  - We keep only English texts. 
  - Remove all the occurrences of the word that we have searched for. 
  - The names will be kept and other tokens will be transformed to their lemmas.
The Data processing pipeline is shown in the following figure:

![image](https://github.com/Nemat-Allah-Aloush/Social-Media-Monitoring/blob/main/imgs/data_processing.png)

---

## Sentiment Analysis with RNN
The idea is to represent each token using the pretrained GloVe model, and feed these token representations into a multilayer bidirectional RNN to obtain the 
text sequence representation, which will be transformed into sentiment analysis outputs. 

The sentiment analysis model is inspired from: https://d2l.ai/chapter_natural-language-processing-applications/sentiment-analysis-rnn.html

