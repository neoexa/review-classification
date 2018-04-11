#import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd
 


print("Loading movie reviews dataset :")

X = pd.read_csv('./data/dataset.csv', sep='\n')
y = pd.read_csv('./data/labels.csv', sep='\n')

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

clf = NearestNeighbors()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)


#dataset = load_files(movie_reviews_data_folder, shuffle=True)
#print("%d documents" % len(dataset.filenames))
#print("%d categories" % len(dataset.target_names))
#print()

#docs_train, docs_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.10)
#clf = NearestNeighbors()
#clf.fit(docs_train, y_train)

#accuracy = clf.score(docs_test, y_test)

#print(accuracy)