import sys
import os.path
import ngram
import predict


if (len(sys.argv) < 2):
	print("Error: Expected arguments: ModuleFilename,  Directory for .csv files")
	sys.exit()

moduleFilename = sys.argv[1]
directoryName = sys.argv[2]

#In the althingi_errors with corrections
csvFilenames = ["079.csv", "080.csv", "081.csv", "082.csv", "084.csv", "085.csv", "089.csv", "090.csv", "091.csv", "092.csv", "093.csv", "094.csv", "095.csv", "096.csv", "097.csv", "099.csv", "100.csv", "101.csv", "102.csv", "103.csv", "105.csv", "106.csv", "107.csv", "108.csv", "110.csv"]

ngramModel = ngram.loadObject(moduleFilename)
for filename in csvFilenames:
	path = directoryName + filename
	if (os.path.isfile(path)):
		ngramModel.train(path) #train on the correct words
		ngramModel.printInfo()


ngram.saveObject(ngramModel, moduleFilename)


