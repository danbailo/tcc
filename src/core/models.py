from mongoengine import BooleanField, Document, StringField


class Answer(Document):
        """ Armazena as respostas do usuário no banco de dados """
        answer_1 = BooleanField(required=True)
        answer_2 = BooleanField(required=True)
        answer_3 = BooleanField(required=True)
        answer_4 = BooleanField(required=True)
        answer_5 = BooleanField(required=True)
        answer_6 = BooleanField(required=True)
        answer_7 = BooleanField(required=True)
        answer_8 = BooleanField(required=True)
        answer_9 = BooleanField(required=True)
        answer_10 = BooleanField(required=True)
        answer_11 = BooleanField(required=True)
        evaded = BooleanField(required=True)
