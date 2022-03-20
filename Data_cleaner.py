import re
import string
import nltk
from nltk.corpus import wordnet,stopwords, words
from pandas import DataFrame
import spacy
import demoji
from spellchecker import SpellChecker
import pandas as pd

class Data_cleaner():
    nlp = spacy.load('en_core_web_sm')  # English pipeline optimized for CPU. Components: tok2vec, tagger, parser, senter, ner, attribute_ruler, lemmatizer.
    stop_words = set(stopwords.words('english'))
    words = set(nltk.corpus.words.words())
    spell = SpellChecker()
    table = str.maketrans('', '', string.punctuation) # table to delete the punctuation from the texts by using string library
    #def __inint__():
    def clean(data):
        return data

    def cleaning(self,text):
        # Replacing emojis with their describtion
        no_emoji=demoji.replace_with_desc(text," ") 
        no_at = re.sub("@[A-Za-z0-9]+","",no_emoji) #Remove @ sign
        no_link = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", no_at) #Remove http links
        no_hashtag = no_link.replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
        no_asci=re.sub(r'[^\x00-\x7f]',r' ',no_hashtag) #non asci
        no_punc=no_asci.translate(self.table)

        #tweet = " ".join(w for w in nltk.wordpunct_tokenize(no_punc) # splitting the tweet into tokens
        #     if w.lower() in words and w.isalpha())
        return no_punc

    def spell_checking(self,text):
        # Fixing Word Lengthening, which occurs when characters are wrongly repeated. 
        # English words have a max of two repeated characters. Additional characters need to ripped off, 
        pattern = re.compile(r"(.)\1{2,}")
        length_fixed= pattern.sub(r"\1\1", text)
        tweet = " ".join(w if (w[0].isupper()) else self.spell.correction(w) for w in nltk.wordpunct_tokenize(length_fixed) )
        return(tweet)

    def nlp_analyzing(self,text):    
        doc = self.nlp(text)
        lemmas = []
        for token in doc:
            if token.lang_ == 'en' and token.pos_ != 'SPACE' and token.text not in self.stop_words:
                if token.ent_type_!="":  # if the token is recognized as a Name Entity
                    lemmas.append(token.text)
                elif token.text.lower() in words: #Checking if the word is in the dictionary (meaningful english world)
                    lemmas.append(token.lemma_)
        return ' '.join(lemmas)

    def clean(self,data):
        cleaned_df=pd.DataFrame()
        for doc in data:
            cleaned_df.append(self.nlp_analyzing(self.spell_checking(self.cleaning(doc))))

# cleaner=Data_cleaner()
# collected_data = pd.read_csv('#iPhone13.csv')
# tweets=collected_data["tweet"]
# cleaned=cleaner.clean(tweets)
