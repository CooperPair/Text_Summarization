from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

#removing stop words and making frequency table.
text = 'I think back to how got here and remember was assigned this case as per usual.I show up for work and the Captain tells me there has been murder.He gives me the details and then I begin my investigation.I cannot tell you how I know where to start.I just do  Sometimes I start with the family sometimes the place of employment.Sometimes I start by interviewing friends of the deceased but all that is always after I examine the crime scene.I am constantly looking for motives a place to start something to sink my teeth into'

stopWords = set(stopwords.words("english"))
words = word_tokenize(text)
print(words)

#creating the dictionary for the frequency table,

freqTable = dict()

for word in words:
	word = word.lower()
	if word in stopWords:
		continue
	
	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

print(freqTable)
#now we use the freq table dictionary over every sentence to know which sentence have the  most relevant insight to the overall
#purpose of the text.
#ASSIGNING THE SCORE TO EVERY SENTENCE
#since we already have the sent_tokenize() method to create the array of sentence, this way we can later go through the
#dictionary to generate the summary

sentences = sent_tokenize(text)
print(sentences)
sentenceValue = dict()

#moving through every sentence and give it the score depending upon the word it has, there many algorithm which can do this
#but for now i am using the simple algorithm of adding the frequency of every non-stop words in a sentence

for sentence in sentences:
    for wordValue in freqTable:
        if wordValue[0] in sentence.lower():
            if sentence[:12] in sentenceValue:
                sentenceValue[sentence[:12]] += wordValue[1]
            else:
                sentenceValue[sentence[:12]] = wordValue[1]
	#sentence[:12] is a simple way to hash each sentence into the dictionary.potential issue with our algorithm is that
	#long sentences have the advantage over the short sentences.To solve this we are dividing every sentence score by the
	#number of words in the sentence.


sumValues = 0
for sentence in sentenceValue:
    sumValues += int(sentenceValue[sentence])

# Average value of a sentence from original text
average = int(sumValues/ len(sentenceValue))
#Average value of a sentence from  original text
#average = int(sumValues/ len(sentenceValue))

#applying the threshold and store our sentences in order into our summary.

summary = ''
for sentence in sentences:
		if sentence[:12] in sentenceValue and sentenceValue[sentence[:12]] > (1.5 * average):
			summary +=  " " + sentence

# now we will print the summary and we will see how good is our summary 

#optional enhancement Make smarter word frequency tables 
print(summary)