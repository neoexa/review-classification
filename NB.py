import sys
from pprint import pprint
from time import time
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
import itertools
from itertools import cycle
from sklearn.metrics import roc_curve, auc
from scipy import interp



TRAIN_DATA = "dataset/"


if __name__ == "__main__":
    
    print("Chargement des donnees d'entrainement  :")
    dataset = load_files(TRAIN_DATA, shuffle=True)
    print("%d Documents trainData" % len(dataset.filenames))
    print("%d catégories" % len(dataset.target_names))
    print()

    docs_train, docs_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.10, random_state=True)


    pipeline = Pipeline([
        ('vect', TfidfVectorizer(stop_words="english", ngram_range=(1,2), max_df=0.7)),
        ('clf', MultinomialNB(alpha=1.0, fit_prior=True, class_prior=None)),
    ])

    
    parameters = {
    }
        
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1)
    
    print("Calcul grid search ...")
    print("Pipeline:", [name for name, _ in pipeline.steps])
    
    print("Parametres:")
    pprint(parameters)
    
    t0=time()
    grid_search.fit(docs_train, y_train)
    print("done in %0.3fs" % (time() - t0))
    print()


    print("Best parameters set :")
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))

    print("Précision Cross Validation: %0.3fs" % grid_search.best_score_)
    
    
    
    print("Precision test:")
    y_predicted = grid_search.predict(docs_test)  
    print(metrics.classification_report(y_test, y_predicted, target_names=dataset.target_names))


    ##Confusion matrix
    def plot_confusion_matrix(cm, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')
        
        print(cm)
        
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        plt.xticks(np.arange(2), ('Pos', 'Neg'))
        plt.yticks(np.arange(2), ('Pos', 'Neg'))
        
        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                 	horizontalalignment="center",
                 	color="white" if cm[i, j] > thresh else "black")
        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
	
    
    cnf_matrix = confusion_matrix(y_test, y_predicted)
    np.set_printoptions(precision=2)
    
    plt.figure()
    plot_confusion_matrix(cnf_matrix, normalize=True, title='Normalized confusion matrix')
    plt.show()
    
    ##ROC curve
    y_pred_proba = grid_search.predict_proba(docs_test)[::,1]
    fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
    auc = metrics.roc_auc_score(y_test, y_pred_proba)
    plt.plot(fpr,tpr,label="Tagged, AUC="+str(auc))
    plt.legend(loc=4)
    plt.ylabel('True positive rate')
    plt.xlabel('False positive rate')
    plt.show()
    
 
