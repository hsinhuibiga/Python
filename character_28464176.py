"""
HsinHui Lin  28464176  start date: 18 May 2018   lsat modifed date: 1 June 2018

Task 2: Building a class for analysing characters
This method should accept the tokenised list as the argument, and
attempt to count the occurrences for each of the characters encountered in the
given tokenised list. The loop methond is to assume that if there is the character
 , just plus one character; if not the condition, then set the value.

"""
#import pandas library
import pandas as pd
#set up class
class CharacterAnalyser:
    def __init__(self):
        #build a contructor
        self.character_frequency = pd.DataFrame([], columns=['frequency'])
    # to store in the data structure(i.e.instance variable) defined in the constructor
    def analyse_characters(self,tokenised_list):
        #tokenised_list as the argument
        for word in tokenised_list:
            #to count the occurrences for each of the characters
            for character in word:
                # if there is the character, just plus one
                if character not in self.character_frequency.index:
                    self.character_frequency.loc[character]=1
                #not the condition then set the value to one
                else:
                    self.character_frequency["frequency"].loc[character]+=1
    #build a string to return
    def __str__(self):
        return str(self.character_frequency)
    # return only the frequency of all different punctuations
    def get_punctuation_frequency(self):
        #use dataframe
        df=pd.DataFrame([], columns=['frequency'])
        # if a character is a digit or alpha,do nothing
        for i in self.character_frequency.index:
            if i.isalpha() or i.isdigit():
                continue
            #otherwise add it into punctuation_frequency dataframe
            df.loc[i]=self.character_frequency["frequency"].loc[i]
        return df