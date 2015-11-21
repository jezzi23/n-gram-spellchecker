import sys
import csv
import pickle
import time


class nGram:
	#Data for the n-gram language model



	def __init__(self, N):
		self.n = N
		self.totalWords = 0
		self.counterDict = dict()
		self.alreadyOccuredSequenceCounter = 0 #for debugging reasons
		self.newSequenceCounter = 0 # should be the same as len(counterDict).
		self.dictionaryCountsCounter = 0

	def train(self, csvFilename):
		csvFile = open(csvFilename, encoding="utf-8")
		data = csv.reader(csvFile)
		next(data, None) # skip header
		

		startTime = time.time()
		lastTime = startTime
		currentTime = startTime

		CORRECTWORD = 3 #index
		#and now to train on the data - count the occurrences of words

		#iteration counter, i
		currentHistoryLength = 0 #will never be more than the n, of n-gram
		wordSequenceBuffer = [""]*self.n
		
		print()
		print("Training on " + csvFilename + " started") #print status every second

		i=0
		for word in data:
			i+=1
			self.totalWords+=1
			currentTime = time.time()
			if (currentTime-lastTime > 0.5):
				print("Training process: " + str(i)+ " words read") #print status every second
				lastTime = currentTime

			

			if (word[CORRECTWORD] == "," or word[CORRECTWORD] == "." or word[CORRECTWORD] == ""):
				currentHistoryLength = 0
				continue

			if (currentHistoryLength < self.n):
				currentHistoryLength+=1
			
			for k in range(0, self.n-1):
				wordSequenceBuffer[k] = wordSequenceBuffer[k+1]
			wordSequenceBuffer[self.n-1] = word[CORRECTWORD]

			
			for historyLength in range(0, currentHistoryLength):
				
				wordSequence = [""]*(historyLength+1)
				for j in range(0 , len(wordSequence)):
					wordSequence[j] = wordSequenceBuffer[self.n-historyLength-1+j]
				
				self.updateCounter(wordSequence)

			

		totalTime = currentTime-startTime

		csvFile.close()

	


	def updateCounter(self, wordArray):
		if (len(wordArray) == 0):
			return
		combinedWord = wordArray[0]

		for i in range(1, len(wordArray)):
			combinedWord += " " + wordArray[i]  #seperated by spaces
		self.dictionaryCountsCounter += 1
		if (combinedWord in self.counterDict): #entry already exists
			self.counterDict[combinedWord] += 1
			self.alreadyOccuredSequenceCounter += 1
		else:  # does not exists so we create it
			self.counterDict[combinedWord] = 1




	def printInfo(self):
		print("Information about the " + str(self.n) +"-gram model.")
		print("Total words read: " + str(self.totalWords) + " (not including \",\" and \".\")")
		print("Total parameters of the model: " + str(len(self.counterDict)))
		if (self.dictionaryCountsCounter != 0):
			print("Occurrences of 'already seen' word sequences: " + str(int(100*self.alreadyOccuredSequenceCounter/self.dictionaryCountsCounter)) + "%")
			print("Occurrences of 'new' word sequences: " + str(int(100*len(self.counterDict)/self.dictionaryCountsCounter)) +"%")
		print()


		



	
def loadObject(filename):
	with open(filename, 'rb') as inp:
		print("N-gram module loaded from: " + filename)
		return pickle.load(inp);

def saveObject(obj, filename):
	with open(filename, 'wb') as outp:
		print("N-gram module dumped into: " + filename)
		pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)






