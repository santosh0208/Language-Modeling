"""
Language Modeling Project
Name:
Roll No:
"""

import language_tests as test

project = "Language" # don't edit this

### WEEK 1 ###

'''
loadBook(filename)
#1 [Check6-1]
Parameters: str
Returns: 2D list of strs
'''
def loadBook(filename):
    l=[]
    o=open(filename,"r").read()
    slines=o.split("\n")
    for i in slines:
        splitword=i.split(" ")
        if splitword !=[""]:
            l.append(splitword)
    return l 


'''
getCorpusLength(corpus)
#2 [Check6-1]
Parameters: 2D list of strs
Returns: int
'''
def getCorpusLength(corpus): 
    total_length = sum(len(row) for row in corpus) 
    return total_length 


'''
buildVocabulary(corpus)
#3 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def buildVocabulary(corpus):
    list=[]
    for i in corpus:
        for j in i:
            if j not in list:
                list.append(j)
    return list


'''
countUnigrams(corpus)
#4 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countUnigrams(corpus):
    count_unigrams={}
    list=[]
    for i in corpus:
        for j in i:
            list.append(j)
    for k in list:
        if k not in count_unigrams:
            count_unigrams[k]=list.count(k)
    return count_unigrams 


'''
getStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def getStartWords(corpus):
    l=[]
    for i in corpus:
        if i[0] not in l:
            l.append(i[0]) 
    return l
 


'''
countStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countStartWords(corpus):
    count_startword={}
    l=[]
    for i in corpus:
        l.append(i[0])
    for k in l:
        if k not in count_startword:
             count_startword[k]=l.count(k)
    return count_startword 


'''
countBigrams(corpus)
#6 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def countBigrams(corpus):
    d={}
    for p in range (len(corpus)):
        for j in range (len(corpus[p])-1):
            v = corpus[p][j]
            v2 = corpus[p][j+1]
            if v not in d:
                d[v]={}
            if v2 not in d[v]:
                d[v][v2]=0
            d[v][v2]+=1
    return d


### WEEK 2 ###

'''
buildUniformProbs(unigrams)
#1 [Check6-2]
Parameters: list of strs
Returns: list of floats
'''
def buildUniformProbs(unigrams):
    l=[]
    length=len(unigrams)
    for i in unigrams:
        s=1/length
        l.append(s)
    return l


'''
buildUnigramProbs(unigrams, unigramCounts, totalCount)
#2 [Check6-2]
Parameters: list of strs ; dict mapping strs to ints ; int
Returns: list of floats
'''
def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    l=[]
    for i in unigrams:
        for j in unigramCounts:
            if i==j:
                c=unigramCounts[j]/totalCount
                l.append(c)
    return l


'''
buildBigramProbs(unigramCounts, bigramCounts)
#3 [Check6-2]
Parameters: dict mapping strs to ints ; dict mapping strs to (dicts mapping strs to ints)
Returns: dict mapping strs to (dicts mapping strs to (lists of values))
'''
def buildBigramProbs(unigramCounts, bigramCounts):
    d={}     
    for i in bigramCounts:
        l=unigramCounts[i]
        l2=[]
        l3=[]
        for j in bigramCounts[i]:
            l2.append(j)
            l3.append(bigramCounts[i][j]/l)
        d1={}
        d1["words"]=l2
        d1["probs"]=l3
        d[i]=d1
    return d


'''
getTopWords(count, words, probs, ignoreList)
#4 [Check6-2]
Parameters: int ; list of strs ; list of floats ; list of strs
Returns: dict mapping strs to floats
'''
def getTopWords(count, words, probs, ignoreList):
    d1=dict(zip(words,probs))                   #[("hi",0.4),("there",0.4),("hello",0.2)]
    l=dict(sorted(d1.items(),key=lambda x:x[1],reverse=True))
    d2={}
    for key,values in l.items():
        if key not in ignoreList and len(d2)<count:
            d2[key]=values
    return d2


'''
generateTextFromUnigrams(count, words, probs)
#5 [Check6-2]
Parameters: int ; list of strs ; list of floats
Returns: str
'''
from random import choices
def generateTextFromUnigrams(count, words, probs):
    l=[]
    for i in range (count):
        l.append(choices(words, weights=probs)) #"hello world hello"
    s="" 
    for i in l:
        for j in i:
            s=s+" " +j 
    return s


'''
generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs)
#6 [Check6-2]
Parameters: int ; list of strs ; list of floats ; dict mapping strs to (dicts mapping strs to (lists of values))
Returns: str
'''
def generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs):
    s=""
    l=[]   
    for i in range (count):
        if len(l)==0 or l[-1]==".":
            j=choices(startWords,startWordProbs) #["dear"]
            l=l+j
        else:
            last_word=l[-1]
            word=bigramProbs[last_word]["words"]  #[ "sir", "madam" ]
            prob=bigramProbs[last_word]["probs"]   #[0.5, 0.5] 
            l=l+choices(word,prob)
    for i in l:
        s=s+" "+i
    return s


### WEEK 3 ###

ignore = [ ",", ".", "?", "'", '"', "-", "!", ":", ";", "by", "around", "over",
           "a", "on", "be", "in", "the", "is", "on", "and", "to", "of", "it",
           "as", "an", "but", "at", "if", "so", "was", "were", "for", "this",
           "that", "onto", "from", "not", "into" ]

'''
graphTop50Words(corpus)
#3 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTop50Words(corpus):
    return


'''
graphTopStartWords(corpus)
#4 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTopStartWords(corpus):
    return


'''
graphTopNextWords(corpus, word)
#5 [Hw6]
Parameters: 2D list of strs ; str
Returns: None
'''
def graphTopNextWords(corpus, word):
    return


'''
setupChartData(corpus1, corpus2, topWordCount)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int
Returns: dict mapping strs to (lists of values)
'''
def setupChartData(corpus1, corpus2, topWordCount):
    return


'''
graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; str ; 2D list of strs ; str ; int ; str
Returns: None
'''
def graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title):
    return


'''
graphTopWordsInScatterplot(corpus1, corpus2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int ; str
Returns: None
'''
def graphTopWordsInScatterplot(corpus1, corpus2, numWords, title):
    return


### WEEK 3 PROVIDED CODE ###

"""
Expects a dictionary of words as keys with probabilities as values, and a title
Plots the words on the x axis, probabilities as the y axis and puts a title on top.
"""
def barPlot(dict, title):
    import matplotlib.pyplot as plt

    names = []
    values = []
    for k in dict:
        names.append(k)
        values.append(dict[k])

    plt.bar(names, values)

    plt.xticks(rotation='vertical')
    plt.title(title)

    plt.show()

"""
Expects 3 lists - one of x values, and two of values such that the index of a name
corresponds to a value at the same index in both lists. Category1 and Category2
are the labels for the different colors in the graph. For example, you may use
it to graph two categories of probabilities side by side to look at the differences.
"""
def sideBySideBarPlots(xValues, values1, values2, category1, category2, title):
    import matplotlib.pyplot as plt

    w = 0.35  # the width of the bars

    plt.bar(xValues, values1, width=-w, align='edge', label=category1)
    plt.bar(xValues, values2, width= w, align='edge', label=category2)

    plt.xticks(rotation="vertical")
    plt.legend()
    plt.title(title)

    plt.show()

"""
Expects two lists of probabilities and a list of labels (words) all the same length
and plots the probabilities of x and y, labels each point, and puts a title on top.
Note that this limits the graph to go from 0x0 to 0.02 x 0.02.
"""
def scatterPlot(xs, ys, labels, title):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    plt.scatter(xs, ys)

    # make labels for the points
    for i in range(len(labels)):
        plt.annotate(labels[i], # this is the text
                    (xs[i], ys[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0, 10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.title(title)
    plt.xlim(0, 0.02)
    plt.ylim(0, 0.02)

    # a bit of advanced code to draw a y=x line
    ax.plot([0, 1], [0, 1], color='black', transform=ax.transAxes)

    plt.show()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    test.week1Tests()
    print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    test.runWeek1()

    ## Uncomment these for Week 2 ##
"""
    print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()
    print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    test.runWeek2()
"""

    ## Uncomment these for Week 3 ##
"""
    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    test.runWeek3()
"""