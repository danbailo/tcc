import random

import numpy as np
import sklearn.model_selection as ms
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

np.random.seed(21)
random.seed(21)


class Classifier:
    def __init__(self, df) -> None:
        self.df = df
        if "_id" in self.df:
            del df["_id"]

    def prepare_data(self) -> None:
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
        return accuracy_score(self.y_test, y_pred), classifier

    def _decision_tree(self) -> tuple: 
        classifier = DecisionTreeClassifier()
        classifier.fit(self.X_train, self.y_train)
        y_pred = classifier.predict(self.X_test)
        return accuracy_score(self.y_test, y_pred), classifier
    
    def _random_forest(self) -> tuple:         
        estimators = 10
        classifier = RandomForestClassifier(n_estimators=estimators, n_jobs=-1)
        classifier = classifier.fit(self.X_train, self.y_train)
        y_pred = classifier.predict(self.X_test)
        return accuracy_score(self.y_test, y_pred), classifier

    def _svm(self) -> tuple:         
        classifier = SVC(random_state=42)
        classifier = classifier.fit(self.X_train, self.y_train)
        y_pred = classifier.predict(self.X_test)
        return accuracy_score(self.y_test, y_pred), classifier
