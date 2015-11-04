import string
import random

def ProcessFile(filename):
    histogram = dict()
    file = open(filename)
    
    for line in file:
        ProcessLine(line, histogram)
    
    return histogram

def ProcessLine(line, histogram):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        histogram[word] = histogram.get(word, 0) + 1

def MostCommonWords(histogram):
    myTupla = []

    for key, value in histogram.items():
        myTupla.append((value, key))

    myTupla.sort(reverse = True)
    return myTupla


def TotalWords(histogram):
    return sum(histogram.values())

def TotalDifferentWords(histogram):
    return len(histogram)

def RandomWord(histogram):
    myTupla = []
    
    for word, frequency in histogram.items():
        myTupla.extend([word] * frequence)

    return random.choice(myTupla)

if __name__ == '__main__':
    histogram = ProcessFile('emma.txt')

    print "Total words: %s" %str(TotalWords(histogram))
    print "Total different words: %s" %str(TotalDifferentWords(histogram))

    #Most Common Words
    myTupla = MostCommonWords(histogram)
    print "The most common words are: "
    for frequence, word in myTupla[:10]:
        print "%s - %s" %(word, frequence)

    #Random Words
    print "\n\nHere are some random words from the book"
    for i in range(5):
        print RandomWord(histogram)