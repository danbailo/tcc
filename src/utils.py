import random
import uuid

from core.models import Answer


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
