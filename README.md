# Social-Media-Monitoring
Social Media Monitoring /Twitter/ in python language.

--- 

## Index
1. [About the project](#About the project)
2. [Requirements](#requirements)
3. [Social Media Monitoring Steps](#semantic-search-engine-steps)
4. [Data Processing](#data-processing)
5. [Sentiment Analysis with RNN](#sentiment-analysis-with-rnn)

---

## Requirements
Here is a list of some of  the used libraries:
a.	d2l: for building the sentiment analysis model.
b.	demoji: for replacing the emojis in tweets with their description.
c.	snscrape: a library to scrap tweets.
d.	Nltk: for natural language processing.

---

## About the project 
The main goal of this project is to scrape data from Twitter for a specific brand or product and try to classify the tweets sentimatically as negative or positive tweets.


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
![image](https://user-images.githubusercontent.com/47036654/165838937-a67ec4e4-4e8e-4a26-b93d-bea2aa05c343.png)

---

## Sentiment Analysis with RNN
The idea is to represent each token using the pretrained GloVe model, and feed these token representations into a multilayer bidirectional RNN to obtain the 
text sequence representation, which will be transformed into sentiment analysis outputs. 
Inspired from: https://d2l.ai/chapter_natural-language-processing-applications/sentiment-analysis-rnn.html

