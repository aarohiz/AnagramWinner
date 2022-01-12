import itertools as it
import nltk
nltk.download('words')
from nltk.corpus import words

#TYPE THE WORD IN HERE AND CLICK RUN
word = 'aarohi'


def permutate(word):
  CrudewordList = []
  x = len(word)
  while x > 2:
    xPerm = it.permutations(word, x) 
    CrudewordList.append(list(xPerm)) 
    x = x - 1
  return CrudewordList

def flatten_list(twoDlist):
    flat_list = []
    for element in twoDlist:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

def tupIntoString(decStringTups):
  wordList = []
  for tup in decStringTups:
    string = ''
    for item in tup:
        string = string + str(item)
    wordList.append(string)
  return wordList

def isWordReal(wordMasterList):
  word_list = words.words()
  realWords = []
  for x in wordMasterList:
    if x in word_list:
      realWords.append(x)
  return realWords



twoDlist = permutate(word)
masterList = flatten_list(twoDlist)


wordMasterList = tupIntoString(masterList)

print(isWordReal(wordMasterList))

  

  