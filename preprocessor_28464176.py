"""
HsinHui Lin  28464176  start date: 18 May 2018   lsat modifed date: 1 June 2018

Task 1: Setting up the preprocessor

"""
#use class to set up the preprocessor
class Preprocessor:
    def __init__(self):
        #define a Python list to hold the individual tokens of a given input text
        self.tokens=[]
    #use string build in split to tokenise the tokens and sum them as a whole list
    def tokenise(self,input_sequence):
        #split the input_sequence
        tokens=input_sequence.split("\n")
        #creat a empty list
        tokenList=[]
        #loop
        for token in tokens:
            #tokenList and append
            tokenList.append(token.split(" "))
            #sum the strings as a whole list
        self.tokens=sum(tokenList,[])
    #use space to join each token to get the return string
    def __str__(self):
        #to present the total number of tokens for the tokenised input text
        return  " ".join(self.tokens)
    def get_tokenised_list(self):
        #get self.tokens
        return self.tokens