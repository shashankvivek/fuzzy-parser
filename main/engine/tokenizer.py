
class Tokenizer:

    def __init__(self,file_path):
        self.__file_path = file_path
        with open(file_path) as input_file:
            self.lines = [line.rstrip() for line in input_file]
    #     file not found error to be handled

    # def get_file_path(self):
    #     return self.__file_path;

    def get_parsed_data(self):
        return self.lines

    # def get_


