import random
from typing import Tuple

import pandas as pd
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
    """Classe que realiza a manipulação inicial dos dados,
    para que os mesmos possam ser separados, treinados e
    avaliados por cada modelo.

    Args:
        df (pd.DataFrame): dataframe contendo os dados que
        serão manipulados pela classe.
    """
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        if "_id" in self.df:
            del df["_id"]

    def prepare_data(self) -> None:
        """Realiza a preparação dos dados, separando os dados de
        treino e teste.
        """
        X = self.df.iloc[:, :-1].values
        y = self.df.iloc[:, -1].values
        self.X_train, self.X_test, self.y_train, self.y_test = \
            ms.train_test_split(
                X, y,
                test_size=0.2,
                shuffle=True,
                random_state=0
            )

    def _logistic_regression(self) -> Tuple[float, LogisticRegression]:
        """Realiza o treinamento de um modelo de regressão logística.

        Returns:
            Tuple[float, LogisticRegression]: tupla contendo a acurácia
            do modelo e o modelo em si.
        """
        classifier = LogisticRegression(n_jobs=-1)
        classifier.fit(self.X_train, self.y_train)
        y_pred = classifier.predict(self.X_test)
        return accuracy_score(self.y_test, y_pred), classifier

    def _decision_tree(self) -> Tuple[float, DecisionTreeClassifier]:
        """Realiza o treinamento de um modelo de árvore de decisão.

        Returns:
            Tuple[float, DecisionTreeClassifier]: tupla contendo a acurácia
            do modelo e o modelo em si.
        """
        classifier = DecisionTreeClassifier()
        classifier.fit(self.X_train, self.y_train)
        y_pred = classifier.predict(self.X_test)
        return accuracy_score(self.y_test, y_pred), classifier

    def _random_forest(self) -> Tuple[float, RandomForestClassifier]:
        """Realiza o treinamento de um modelo de floresta aleatória.

        Returns:
            Tuple[float, RandomForestClassifier]: tupla contendo a acurácia
            do modelo e o modelo em si.
        """
        estimators = 10
        classifier = RandomForestClassifier(n_estimators=estimators, n_jobs=-1)
        classifier = classifier.fit(self.X_train, self.y_train)
        y_pred = classifier.predict(self.X_test)
        return accuracy_score(self.y_test, y_pred), classifier

    def _svm(self) -> Tuple[float, SVC]:
        """Realiza o treinamento de um modelo de máquina de vetores de suporte.

        Returns:
            Tuple[float, SVC]: tupla contendo a acurácia
            do modelo e o modelo em si.
        """
        classifier = SVC(random_state=42)
        classifier = classifier.fit(self.X_train, self.y_train)
        y_pred = classifier.predict(self.X_test)
        return accuracy_score(self.y_test, y_pred), classifier
