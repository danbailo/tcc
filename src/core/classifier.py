import os
import random
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.model_selection as ms
from pandas.core.frame import DataFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, confusion_matrix, log_loss,
                             plot_roc_curve)
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from src.utils import classification_report_as_df, mongo_to_df

np.random.seed(21)
random.seed(21)


class Classifier:
    def __init__(self, df: DataFrame) -> None:
        self.df = df.drop(columns=["_id", "user_id"])

    def prepare_data(self):
        X = self.df.iloc[:, :-1].values
        y = self.df.iloc[:, -1].values
        self.X_train, self.X_test, self.y_train, self.y_test = \
            ms.train_test_split(
                X, y, 
                test_size=0.2,
                shuffle=True,
                random_state=0
            )

    def _logistic_regression(self) -> tuple: 
        classifier = LogisticRegression(n_jobs=-1)
        classifier.fit(self.X_train, self.y_train)
        y_pred = classifier.predict(self.X_test)
        logistic_roc = plot_roc_curve(classifier, self.X_test, self.y_test)
        return accuracy_score(self.y_test, y_pred),\
               logistic_roc,\
               classification_report_as_df(self.y_test, y_pred)

    def _decision_tree(self) -> tuple: 
        classifier = DecisionTreeClassifier()
        classifier.fit(self.X_train, self.y_train)
        y_pred = classifier.predict(self.X_test)
        decision_tree_roc = plot_roc_curve(classifier, self.X_test, self.y_test)
        return accuracy_score(self.y_test, y_pred),\
               decision_tree_roc,\
               classification_report_as_df(self.y_test, y_pred)        
    
    def _random_forest(self) -> tuple:         
        estimators = 10
        classifier = RandomForestClassifier(n_estimators=estimators, n_jobs=-1)
        classifier = classifier.fit(self.X_train, self.y_train)
        y_pred = classifier.predict(self.X_test)
        random_forest_roc = plot_roc_curve(classifier, self.X_test, self.y_test)
        return accuracy_score(self.y_test, y_pred),\
               random_forest_roc,\
               classification_report_as_df(self.y_test, y_pred)

    def _svm(self) -> tuple:         
        classifier = SVC(random_state=42)
        classifier = classifier.fit(self.X_train, self.y_train)
        y_pred = classifier.predict(self.X_test)
        svm_roc = plot_roc_curve(classifier, self.X_test, self.y_test)
        return accuracy_score(self.y_test, y_pred),\
               svm_roc,\
               classification_report_as_df(self.y_test, y_pred)
