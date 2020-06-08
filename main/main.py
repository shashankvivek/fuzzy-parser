import sys

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import argparse
from engine.tokenizer import Tokenizer

parser = argparse.ArgumentParser(description='Extrating answers from input file. The File should contain \n'
                                             '[Line 1] => Input Paragraph to search for answers \n'
                                             '[Line 2 - 6] => Individual question on each line \n'
                                             '[Line 7] => Jumbled answers separated by delimiter')
parser.add_argument('filePath', type=str, help='Path of Input File')
# to expand the functionality, we can add optional param to pick values as per user Input
# parser.add_argument('--infoLineNumber', type=int, help='Path of Input File') ==> 1
# parser.add_argument('--answerLineNumber', type=int, help='Path of Input File') ==> 7
# parser.add_argument('--questionLineNumberRange', type=str, help='Path of Input File') ==> 2,6
parser.add_argument('--delimiter', type=str, help='Delimiter for jumbled answer')
args = parser.parse_args()

if __name__ == '__main__':
    if args.filePath[-4:] != '.txt':
        print('Unsupported File Format ! Please provide txt file only')
        sys.exit()

    delimiter = ';' if args.delimiter is None else args.delimiter

    token = Tokenizer(args.filePath)
    lines = token.get_parsed_data()

    input_sentences = lines[0].split(".")
    answer_sentences = lines[6].split(delimiter)

    for line_number in range(1, 6):
        para_line = process.extractOne(lines[line_number], input_sentences, scorer=fuzz.token_set_ratio)[0]
        print(process.extractOne(para_line, answer_sentences, scorer=fuzz.token_set_ratio)[0].strip())



