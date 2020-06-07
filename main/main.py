from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import argparse
from engine.tokenizer import Tokenizer

parser = argparse.ArgumentParser(description='Extrating answers from input file')
parser.add_argument('filePath', type=str, help='Path of Input File')
# to expand the functionality, we can add optional param to pick values as per user Input
# parser.add_argument('--infoLineNumber', type=int, help='Path of Input File') ==> 1
# parser.add_argument('--answerLineNumber', type=int, help='Path of Input File') ==> 7
# parser.add_argument('--questionLineNumberRange', type=str, help='Path of Input File') ==> 2,6
args = parser.parse_args()

if __name__ == '__main__':
    token = Tokenizer(args.filePath)
    lines = token.get_parsed_data()

    input_sentences = lines[0].split(".")
    answer_sentences = lines[6].split(";")

    for line_number in range(1, 6):
        para_line = process.extractOne(lines[line_number], input_sentences, scorer=fuzz.token_set_ratio)[0]
        print(process.extractOne(para_line, answer_sentences, scorer=fuzz.token_set_ratio)[0].strip())



