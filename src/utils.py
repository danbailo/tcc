import json
import random

import numpy as np
import pandas as pd
from sklearn.metrics import classification_report

from .core.models import Answer

random.seed(42)


def gen_randomic_answers(number_of_answers: int) -> None:
    """Gera 'n' respostas sintéticas e armazena no banco de dados

    Args:
        number_of_answers (int): número de respostas para serem
            adicionadas no banco de dados.
    """
    for _ in range(number_of_answers):
        answer = Answer(
            answer_1=random.choice([True, False]),
            answer_2=random.choice([True, False]),
            answer_3=random.choice([True, False]),
            answer_4=random.choice([True, False]),
            answer_5=random.choice([True, False]),
            answer_6=random.choice([True, False]),
            answer_7=random.choice([True, False]),
            answer_8=random.choice([True, False]),
            answer_9=random.choice([True, False]),
            answer_10=random.choice([True, False]),
            answer_11=random.choice([True, False]),
            evaded=random.choice([True, False]),
        )
        answer.save()
    print(f'Gerado {number_of_answers} respostas sintéticas!')


def mongo_to_df() -> pd.DataFrame:
    """Pega os dados da coleção de respostas do banco de dados e converte num
    json, então, é criado uma lista de dicionários para a criação de um
    dataframe.

    Returns:
        pd.DataFrame: dataframe contendo os dados da base de dados do projeto.
    """
    temp_data = []
    for answer in Answer.objects:
        temp_data.append(json.loads(answer.to_json()))
    return pd.DataFrame(temp_data)


def classification_report_as_df(
            y_test: np.array, y_pred: np.array
        ) -> pd.DataFrame:
    """Transforma o relatório dos modelos de classificação num dataframe.

    Args:
        y_test (np.array): dados de teste do modelo de classificação.
        y_pred (np.array): dados preditos do modelo de classificação.

    Returns:
        pd.DataFrame: relatório do modelo de classificação.
    """
    return pd.DataFrame(classification_report(
        y_test, y_pred, output_dict=True)
    ).T


def data_augmentation(df: pd.DataFrame, len_of_answers: int) -> pd.DataFrame:
    """Duplica a quantidade de colunas do banco de dados de forma sintética.

    Args:
        df (pd.DataFrame): dataframe contendo os dados iniciais.
        len_of_answers (int): número de colunas do dataframe.

    Returns:
        pd.DataFrame: relatório do modelo de classificação.
    """
    evaded = df['evaded'].copy()
    df = df[df.columns.drop('evaded')]
    temp = []
    for i in range(len_of_answers, (len_of_answers*2)):
        for _ in range(len(df)):
            temp.append(random.choice([True, False]))
        df['answer_'+str(i)] = temp.copy()
        temp.clear()
    df['evaded'] = evaded
    return df


def expand_rows(df: pd.DataFrame, size: int = 1) -> pd.DataFrame:
    """Duplica a quantidade de colunas do banco de dados de forma sintética.

    Args:
        df (pd.DataFrame): dataframe contendo os dados iniciais.
        size (int): número de linhas que serão adicionadas, onde
            cada unidade é multiplicada pelo tamanho atual do dataframe.

    Returns:
        pd.DataFrame: novo dataframe com linhas sintéticas adicionadas.
    """
    for i in range(len(df), len(df)+(len(df)*size)):
        df.loc[i] = [random.choice([True, False]) for _ in range(len(
            df.columns))
        ]
    return df
