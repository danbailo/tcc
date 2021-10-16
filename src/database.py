import argparse

from mongoengine import connect, disconnect_all

from .core.models import Answer
from .utils import gen_randomic_answers

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--number', '-n',
        help='Número de respostas sintéticas que serão geradas',
        type=int
    )
    parser.add_argument(
        '--drop', '-d',
        help='Deleta a coleção que armazena as respostas',
        action='store_true',
    )
    args = parser.parse_args()

    if not(args.number or args.drop):
        # Força o usuário entrar com pelo menos um argumento
        parser.error(
            'Nenhuma ação requisitada, selecione entre --number ou --drop'
        )

    connect(db='tcc')

    if args.number:
        # Pega o número passado no argumento para gerar 'n' respostas
        gen_randomic_answers(args.number)

    if args.drop:
        # Deleta a coleção que armazena as respotas
        print('A coleção "Anwser" foi deletada!')
        Answer.drop_collection()

    disconnect_all()
