"""
HsinHui Lin  28464176  start date: 18 May 2018   lsat modifed date: 1 June 2018

Task 3: Building a class for analysing words
Considering Pandas as the appropriate for keeping track of the number of occurrences
for each word. Create a stopwords.txt to contribute in counting the stop-words frequency.

"""
#import panadas library
import pandas as pd
import os
#name the class WordAnalyser
class WordAnalyser:
    # build a constructor
    def __init__(self):
        # for storing each word frequency
        self.word_frequency=pd.DataFrame([], columns=['frequency'])
        # open stopwords.txt file
        with open(os.getcwd()+"/stopwords.txt", 'r') as file:
            self.stopwords = file.read().split("\n")
        # use while to action
        while "" in  self.stopwords:
            # remove the space
             self.stopwords.remove("")
    def __str__(self):
        # return the string
        return str(self.word_frequency)

    # performs the frequency analysis on a given tokenised list
    def analyse_words(self,tokenised_list):
        # accept the tokenised list as the argument
        for word in tokenised_list:
            # to count the occurrences for each of the words
            if word.isalpha():
                if word not in self.word_frequency.index:
                    self.word_frequency.loc[word]=1
                else:
                    self.word_frequency["frequency"].loc[word]+=1
        # The word frequencies updated in the data structure defined in the constructor
        self.word_frequency["word_length"]=self.word_frequency.index
        self.word_frequency["word_length"]=self.word_frequency["word_length"].apply(len)
    def get_word_length_frequency(self):
        # defined to return the number of occurrences for words that are of the same length
        return self.word_frequency.groupby("word_length").sum()
    def get_stopword_frequency(self):
        # defined to return only the frequency of stopwords
        df=pd.DataFrame([], columns=['frequency'])
        # panadas dataframe to return the method
        # in that index to choose i
        for i in self.word_frequency.index:
            # from self.stopwords to find i
            if i in self.stopwords:
                # put i in the dataframe
                df.loc[i]=[self.word_frequency["frequency"].loc[i]]
        # return dataframe
        return df