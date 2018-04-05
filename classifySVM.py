from __future__ import print_function

import sys
from pprint import pprint
from time import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics




if __name__ == "__main__":
    
    print("Loading movie reviews dataset :")
    movie_reviews_data_folder = sys.argv[1]
    dataset = load_files(movie_reviews_data_folder, shuffle=True)
    print("%d documents" % len(dataset.filenames))
    print("%d categories" % len(dataset.target_names))
    print()

    docs_train, docs_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.10, random_state=True)


    pipeline = Pipeline([
        ('vect', TfidfVectorizer()),
        ('clf', LinearSVC()),
    ])

    
    parameters = {
        'clf__C': (1, 1000)
        'vect__min_df': (1,2,3),
        'vect__max_df': (0.9, 1.0),
        'vect__ngram_range': [(1, 1), (1, 2)],
    }
    
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1)
    
    print("Performing grid search ...")
    print("pipeline:", [name for name, _ in pipeline.steps])
    print("parameters:")
    pprint(parameters)
    t0=time()
    grid_search.fit(docs_train, y_train)
    print("done in %0.3fs" % (time() - t0))
    print()


    print("Best score: %0.3fs" % grid_search.best_score_)
    print("Best parameters set:")
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))

    print()
    
    y_predicted = grid_search.predict(docs_test)

    
    print(metrics.classification_report(y_test, y_predicted, target_names=dataset.target_names))

    
    cm = metrics.confusion_matrix(y_test, y_predicted)
    print(cm)   
    