import json
import random
import uuid

import pandas as pd

from core.models import Answer

random.seed(21)

def gen_randomic_answers(number_of_answers):
    """ Gera "n" respostas sintéticas e armazena no banco de dados """
    for _ in range(number_of_answers):
        fake_answer_id = "FAKE_answer-"+uuid.uuid4().hex
        fake_user_id = "FAKE_user-"+uuid.uuid4().hex
        answer = Answer(
            _id = fake_answer_id,
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
            user_id = fake_user_id
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
