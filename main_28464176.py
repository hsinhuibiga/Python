"""
HsinHui Lin  28464176  start date: 18 May 2018   lsat modifed date: 1 June 2018
Task 5: Putting all the classes together

There are 6 files in the tokenList and to use the variable “data” to combine it .
( data=read_input(token)) The read_input() function is for reading in each of the
six input texts. In that function, the variable “data ”( data = file.read()) returned
from the read_input function. Hence, the main() function should be able to invoke any
of that retrieved from read_input().

"""
import matplotlib.pyplot as plt
import pandas as pd
from preprocessor_28464176 import Preprocessor
from character_28464176 import CharacterAnalyser
from word_28464176 import WordAnalyser
from visualiser_28464176 import AnalysisVisualiser
#drive the flow of execution of the program
def read_input(input_file):
    # use try and except
    try:
        # open file
        with open(input_file, 'r') as file:
            # data
            data = file.read()
        return data
    # except then pass
    except:
        pass
#main function
def main():
    # tokenlist and files
    tokenList=["Edward_II_Marlowe.tok","Hamlet_Shakespeare.tok",
               "Henry_VI_Part1_Shakespeare.tok",
               "Henry_VI_Part2_Shakespeare.tok","Jew_of_Malta_Marlowe.tok",
              "Richard_II_Shakespeare.tok"]
    # demostrate the tasks
    for token in tokenList:
        #data
        data=read_input(token)
        #variable p as Preprocessor
        p=Preprocessor()
        #import data to tokenise function
        p.tokenise(data)
        #preprocessed variable
        preprocessed=p.get_tokenised_list()
        #c as CharacterAnalyser
        c=CharacterAnalyser()
        #put preprocessed into analyse_character methond
        c.analyse_characters(preprocessed)
        #w as WordAnalyser
        w=WordAnalyser()
        #put preprocessed into analyse_word methond
        w.analyse_words(preprocessed)
        #a as AnalysisVisualiser
        a=AnalysisVisualiser([c.character_frequency,c.get_punctuation_frequency(),w.get_word_length_frequency(),w.get_stopword_frequency()])
        #invoke visualise_character_frequency methond
        a.visualise_character_frequency()
        #invoke visualise_punctuation_frequency methond
        a.visualise_punctuation_frequency()
        #invoke visualise_word_length_frequency methond
        a.visualise_word_length_frequency()
        #invoke visualise_stopword_frequency
        a.visualise_stopword_frequency()
#invoke main function
if __name__ == "__main__":
    main()