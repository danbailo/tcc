from mongoengine import connect
from utils import gen_randomic_answers
from core.models import Answer
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--number", "-n",
        help="Number of fake answers to generate",
        type=int
    )

    parser.add_argument(
        "--drop", "-d",
        help="Drop all collections of Answer Document",
        action="store_true",
    )

    args = parser.parse_args()

    if not(args.number or args.drop):
        parser.error("Nenhuma ação requisitada, selecione entre --number ou --drop")

    connect(db="tcc")
    
    if args.number:
        gen_randomic_answers(args.number)
    
    if args.drop:
        print('A coleção "Anwser" foi deletada!')
        Answer.drop_collection()