import ngram
import sys
import pickle


if (len(sys.argv) < 3):
	print("Error: Expected arguments: ModuleFilename,  N")
	sys.exit()

moduleFilename = sys.argv[1]
n = int(sys.argv[2])

model = ngram.nGram(n)

open(moduleFilename, 'w')

model.printInfo()

ngram.saveObject(model, moduleFilename)

