import random
from nGramModel import *
import os

class UnigramModel(NGramModel):

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the UnigramModel object)
        Effects:  this is the UnigramModel constructor, which is done
                  for you. It allows UnigramModel to access the data
                  in the NGramModel class by calling the NGramModel
                  constructor.
        """
        super(UnigramModel, self).__init__()

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts
        Effects:  this function populates the self.nGramCounts dictionary,
                  which is a dictionary of {string: integer} pairs.
                  For further explanation of UnigramModel's version of
                  self.nGramCounts, see the spec.

                  Note: make sure to use the return value of prepData to
                  populate the dictionary, which will allow the special
                  symbols to be included as their own tokens in
                  self.nGramCounts. For more details, see the spec.
        """
        # adds special characters to lines
        text = self.prepData(text);
        for line in text:
            for word in line:
                # for unigrams we ignore these characters
                if (word != '^::^' and word != '^:::^'):
                    # if the word has not been encountered before, make a new entry in dictionary
                    if word not in self.nGramCounts:
                        self.nGramCounts[word] = 1
                    # if it has been encountered, just add 1 to the count
                    else:
                        self.nGramCounts[word] += 1;

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the UnigramModel, see the spec.
        """
        # function should return true if self.nGramCounts is not empty
        if len(self.nGramCounts) > 0:
            return True

        return False

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNgGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  UnigramModel sees as candidates, see the spec.
        """
        pass

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # Add your test cases here
    text = [ ['the', 'quick', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    sentence = [ 'brown' ]

    song = []
    # this doesn't always work it depends on the directory you're in when running the code idk lol
    dir = os.path.dirname(__file__)
    file = open(dir + '/../data/lyrics/the_beatles/let_it_be.txt', 'r')
    for line in file:
        line = line.strip().split()
        if line != "":
            song.append(line)

    unigramModel = UnigramModel() # make new Unigram object
    unigramModel.trainModel(song) # train model with text list
    print unigramModel.nGramCounts
    print unigramModel.trainingDataHasNGram(sentence)
