import pandas as pd
import unicodedata
import pprint 
import numpy
import csv
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA = ROOT_DIR + "/../data"
DATA_REVIEW = DATA + "/dataset.csv"
DATA_LABEL = DATA + "/labels.csv"

if os.path.isdir(DATA):
	if os.path.isfile(DATA_REVIEW):
		if os.path.isfile(DATA_LABEL):

			NEO_DATASET = ROOT_DIR + "/../dataset"
			NEO_DATASET_NEG = NEO_DATASET + "/neg"
			NEO_DATASET_POS = NEO_DATASET + "/pos"

			df1_colnames = ['review']
			df1 = pd.read_csv(DATA_REVIEW, names=df1_colnames, sep='\n', header=None)
			df2_colnames = ['label']
			df2 = pd.read_csv(DATA_LABEL, names=df2_colnames, sep='\n', header=None)
			df = df1.join(df2)


			if not os.path.exists(NEO_DATASET):
			    os.makedirs(NEO_DATASET)

			if not os.path.exists(NEO_DATASET_NEG):
			    os.makedirs(NEO_DATASET_NEG)

			if not os.path.exists(NEO_DATASET_POS):
			    os.makedirs(NEO_DATASET_POS)

			i = 0
			while(i < len(df)):
					if (df.iloc[i][1] < 0):
						file_title = NEO_DATASET_NEG+"/"+ str(i) + ".txt"
						file=open(file_title, "w+") 
						file.write(''.join(df.iloc[i][0]))
						file.close()
						i+=1
					else:
						file_title = NEO_DATASET_POS + "/"+ str(i) + ".txt"
						file=open(file_title, "w+") 
						file.write(''.join(df.iloc[i][0]))
						file.close()
						i+=1
		else:
			print "NO FILE /labels.csv"
	else:
		print "NO FILE /dataset.csv"
else:
	print "NO DIRECTORY /data/"

print("\r" + "DONE. \n")