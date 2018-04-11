import treetaggerwrapper
import pandas as pd
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

TREETAGGER_DIR = ROOT_DIR + "/../treetagger"

DATA_DIR = ROOT_DIR + "/../data"
DATA_FILE = DATA_DIR + "/dataset.csv"

NEO_DATA_FILE = DATA_DIR + "/lemmatised_dataset.csv"

if os.path.isdir(TREETAGGER_DIR):
	if os.path.isfile(DATA_FILE):
		
		if not os.path.isdir(NEO_DATA_DIR):
			os.makedirs(NEO_DATA_DIR)

		df = pd.read_csv(DATA_FILE,sep='\t', names=['message'])
		tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR=TREETAGGER_DIR)
		dfMessage = df['message'].map(lambda x:  tagger.tag_text(unicode(x,"utf-8")))
		lemmas = []

		for messageLemmatised in dfMessage:
			s = ""
			for word in messageLemmatised:
				temp = word.split('\t')
				if(len(temp) == 3):
					s += temp[2] + " "
			lemmas.append(s)

		dfLemmatised = pd.DataFrame({"message":lemmas})
		dfLemmatised.to_csv(NEO_DATA_FILE, sep='\t', encoding='utf-8', index=False, header=False)

	else:
		print "NO DATA FILE /dataset.csv"
else:
	print "NO TREETAGGER DIR /treetagger/"

print("\r" + "DONE. \n")