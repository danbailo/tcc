import json
import random

import pandas as pd
from sklearn.metrics import classification_report

from .core.models import Answer

random.seed(42)

def gen_randomic_answers(number_of_answers):
    """ Gera "n" respostas sintéticas e armazena no banco de dados """
    for _ in range(number_of_answers):
        answer = Answer(
            answer_1 = random.choice([True, False]),
            answer_2 = random.choice([True, False]),
            answer_3 = random.choice([True, False]),
            answer_4 = random.choice([True, False]),
            answer_5 = random.choice([True, False]),
            answer_6 = random.choice([True, False]),
            answer_7 = random.choice([True, False]),
            answer_8 = random.choice([True, False]),
            answer_9 = random.choice([True, False]),
            answer_10 = random.choice([True, False]),
            answer_11 = random.choice([True, False]),
            evaded = random.choice([True, False]),
        )
        answer.save()
    print(f"Gerado {number_of_answers} respostas sintéticas!")

def mongo_to_df():
    """ Pega os dados da coleção de respostas do banco de dados e converte num dataframe """
    temp_data = []
    for answer in Answer.objects:
        # Pega cada documento da coleção e converte esse em json, depois cada json
        # é convertido num dicionário e é criado uma lista de dicionarios para
        # a criação de um dataframe
        temp_data.append(json.loads(answer.to_json()))
    return pd.DataFrame(temp_data)

def classification_report_as_df(y_test, y_pred):
    return pd.DataFrame(classification_report(y_test, y_pred, output_dict=True)).T    

def data_augmentation(df, len_of_answers):
    evaded = df['evaded'].copy()
    df = df[df.columns.drop('evaded')]
    temp = []
    for i in range(len_of_answers+1, (len_of_answers*2)+1):
        for _ in range(len(df)):
            temp.append(random.choice([True, False]))
        df['answer_'+str(i)] = temp.copy()
        temp.clear()
    df['evaded'] = evaded
    return df