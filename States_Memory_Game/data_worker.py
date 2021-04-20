# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
import pandas
import os
import platform
import subprocess

data_dictionary = {
    "state": [],
    "was_correct": [],
    "total_correct": []
}


class States:
    def __init__(self):
        self.compare = False
        self.guess = ""
        self.answers_given = 0
        self.answers_correct = 0

    def check_state(self, guess):
        self.guess = guess.title()
        df = pandas.read_csv("50_states.csv")
        st = df.state
        value = df[st == self.guess]
        self.found_result(value)
        self.append_answers_data()
        try:
            state = value.state.to_string(index=False)
            # state = value.state.item()
            x_state = int(value.x)
            y_state = int(value.y)
            return x_state, y_state, state
        except KeyError as ke:
            print(f"error {ke}")
        except TypeError as te:
            print(f"TYPE: {te}")

    def found_result(self, value):
        self.answers_given += 1
        df = pandas.read_csv("../correct_answers.csv")
        found = df[df['state'].str.contains(self.guess).to_list()]
        if len(value) and not found.empty:
            if not found.count()[0]:
                self.compare = True
                self.answers_correct = self.last_score()
                self.answers_correct += 1
            else:
                self.compare = False
                self.answers_correct = self.last_score()
        elif len(value) and found.empty:
            self.compare = True
            self.answers_correct = self.last_score()
            self.answers_correct += 1

        else:
            self.compare = False

    @staticmethod
    def last_score():
        df = pandas.read_csv("../correct_answers.csv")

        if df.total_correct.notnull().any():
            row_max_score = df.total_correct.max()
        else:
            row_max_score = 0
        return row_max_score

    def append_answers_data(self):
        data_to_save = {
            "state": [self.guess],
            "was_correct": [self.compare],
            "total_correct": [self.answers_correct]
        }
        df = pandas.DataFrame(data_to_save)
        df.to_csv('correct_answers.csv', mode='a', header=False, sep=",")

    @staticmethod
    def new_game_memory():
        new_data = pandas.DataFrame(data_dictionary)
        new_data.to_csv("correct_answers.csv")

    @staticmethod
    def states_to_learn():
        df1 = pandas.read_csv("50_states.csv")
        df2 = pandas.read_csv("../correct_answers.csv")
        col1 = df1.state.to_list()
        col2 = df2.state.to_list()
        set1 = set(col1)
        set2 = set(col2)
        missing = list(sorted(set1 - set2))
        data_to_save = {
            "state": missing
        }
        df = pandas.DataFrame(data_to_save)
        df.to_csv('states_to_learn.csv')

    @staticmethod
    def open_states_to_learn():
        filepath = "../states_to_learn.csv"
        if platform.system() == 'Darwin':
            subprocess.call(('open', filepath))
        elif platform.system() == 'Windows':
            os.startfile(filepath)
        else:
            subprocess.call(('xdg-open', filepath))


if __name__ == "__main__":
    states = States()
    # states.new_game_memory()

    # answer = "tennessee"
    # state_returned = states.check_state(answer)
    # if state_returned:
    #     print(f"RETURNED: {state_returned[0]} {state_returned[1]} {state_returned[2]}")

    # states.create_answers_data()
    # states.append_answers_data()

    # score = states.last_score()
    # print(f"SCORE RESULT {score}")

    states.states_to_learn()
