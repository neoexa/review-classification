import sys
from pprint import pprint
from time import time
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics



TRAIN_DATA = "dataset/"
CHALLENGE_DATA = "data/challenge_data.csv"


if __name__ == "__main__":
    
    print("Chargement des donnees d'entrainement  :")
    dataset = load_files(TRAIN_DATA, shuffle=True)
    print("%d Documents trainData" % len(dataset.filenames))
    print("%d Categories" % len(dataset.target_names))

    
    challenge_pd = pd.read_csv(CHALLENGE_DATA, names=['x'], sep='\t', header=None)
    print("%d Documents de challenge" % len(challenge_pd))
    #print(challenge_pd)

    print()

    docs_train, docs_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.10, random_state=True)


    pipeline = Pipeline([
        ('vect', TfidfVectorizer(stop_words='english', ngram_range=(1,2), min_df=1, max_df=0.9)),
        ('clf', LinearSVC(C = 1000)),
    ])

    
    parameters = {
        
    }
        
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1)
    
    print("Calcul grid search ...")
    print("Pipeline:", [name for name, _ in pipeline.steps])
    
    ##print("Paramètres:")
    ##pprint(parameters)
    
    t0=time()
    grid_search.fit(docs_train, y_train)
    print("Fini en %0.3fs" % (time() - t0))
    print()

    '''
    print("Best parameters set :")
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))'''

    print("Precision Cross Validation: %0.3fs" % grid_search.best_score_)
    
    print("Precision test :")
    y_predicted = grid_search.predict(docs_test)  
    print(metrics.classification_report(y_test, y_predicted, target_names=dataset.target_names))
    cm = metrics.confusion_matrix(y_test, y_predicted)
    print(cm)   

    print("Prediction donnees challenge :")
    challenge_predictions = grid_search.best_estimator_.predict(challenge_pd.x)
    output = pd.DataFrame(challenge_predictions)
    output.to_csv('GROUPEK.csv', header =None, index = False)
    print("FIN")