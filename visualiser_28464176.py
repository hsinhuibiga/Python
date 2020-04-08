"""
HsinHui Lin  28464176  start date: 18 May 2018   lsat modifed date: 1 June 2018

2.4 Task 4: Building a class for visualising the analysis

The Pandas data structure could be able to represent all the different stylistic
features extracted for each of the six input texts. Using the bar chart to present
the data. Set the condition to shape the loop which is the character is not alpha,
do nothing, otherwise add it to the plot data-frame.
The next step is to set the value of “kind”, “title”, “figsize”,”legend”,and “fontsize”.


"""
#import library
import matplotlib.pyplot as plt
import pandas as pd
#define AnalysisVisualiser class for visualising the stylometric analysis
class AnalysisVisualiser:
    def __init__(self,all_text_stats):
        #instance varible
        #the input value is a list of dataframes
        self.all_text_stats=all_text_stats
    def visualise_character_frequency(self):
        #the relative frequency of each different character
        character_frequency=self.all_text_stats[0]
        #pandas dataframe
        character_frequency_without_punctuation=pd.DataFrame([], columns=['frequency'])
        for i in character_frequency.index:
            # if the character is not alpha, do nothing,otherwise add it to the plot dataframe
            if i.isalpha()==False:
                continue
            #disregard the frequencies of punctuations
            character_frequency_without_punctuation.loc[i]=character_frequency["frequency"].loc[i]
        #the frequency of each character based on the length of a given text
        character_frequency_without_punctuation["frequency"].plot(kind='bar', title ="character frequency without punctuation",figsize=(15,10),legend=True, fontsize=12)
    def visualise_punctuation_frequency(self):
        #plots a suitable graph to present the relative frequencies of each different punctuation
        punctuation_frequency=self.all_text_stats[1]
        #visualise and set kind, title, figsize,legend,fontsize
        punctuation_frequency["frequency"].plot(kind='bar', title ="punctuation frequency without punctuation",figsize=(15,10),legend=True, fontsize=12)
    def visualise_word_length_frequency(self):
        #plots a suitable graph to present the relative frequencies of each different word length
        word_length_frequency=self.all_text_stats[2]
        #visualise and set kind, title, figsize,legend,fontsize
        word_length_frequency["frequency"].plot(kind='bar', title ="word length frequency without punctuation",figsize=(15,10),legend=True, fontsize=12)
    def visualise_stopword_frequency(self):
        #plots a suitable graph to present the relative frequencies of each different stopword
        stopword_frequency=self.all_text_stats[3]
        #visualise and set kind, title, figsize,legend,fontsize
        stopword_frequency["frequency"].plot(kind='bar', title ="stopword frequency without punctuation",figsize=(15,10),legend=True, fontsize=12)
