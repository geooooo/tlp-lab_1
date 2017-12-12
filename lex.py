"""
    Лексический анализатор
    на конечных автоматах
"""


import string


next_state = {
    # символы:  +   -   :   =   b   e   g   i   n   d   \w   \d   space
    # S0 - start
    0: {
        "+":    3,
        "-":    1,
        ":":    5,
        "b":    8,
        "e":   14,
        r"\W": 18,
        r"\d": 20
    },
    # S1
    1: {
        " ": 2,
    },
    # S2 - stop
    # S3
    3: {
        " ": 2
    },
    # S4 - убрал
    # S5
    5: {
        "=": 6
    },
    # S6
    6: {
        " ": 7
    },
    # S7 - stop
    # S8
    8: {
        "e": 9
    },
    # S9
    9: {
        "g": 10
    },
    # S10
    10: {
        "i": 11
    },
    # S11
    11: {
        "n": 12
    },
    # S12
    12: {
        " ": 13
    },
    # S13 - stop
    # S14
    14: {
        "n": 15
    },
    # S15
    15: {
        "d": 16
    },
    # S16
    16: {
        " ": 13
    },
    # S17 - убрал
    # S18
    18: {
        r"\d": 18,
        " ": 19
    },
    # S19 - stop
    # S20
    20: {
        r"\d": 20,
        ".": 21,
        ",": 22,
        " ": 24
    },
    # S21
    21: {
        r"\d": 23
    },
    # S22
    22: {
        r"\d": 23
    },
    # S23
    23: {
        r"\d": 23,
        " ": 24
    }
    # S24 - stop
}


def state_machine():
    global lex_val
    lex_val = ""
    cur_state = 0
    cur_input = recognize()
    set_end_states = {2, 7, 24, 19, 13}
    while (cur_state not in set_end_states) and (cur_input != "endf"):
        # print("cur_input = {0}\ncur_state = {1}\n".format(cur_input, cur_state))
        try:
            cur_state = next_state[int(cur_state)][cur_input]
        except KeyError:
            raise Exception("Лексическая ошибка !")
        if cur_state not in set_end_states:
            cur_input = recognize()
    if (cur_state not in set_end_states) and (cur_input == "endf"):
        raise Exception("Лексическая ошибка !")
    elif cur_state == 7:
        return "assign"
    elif cur_state == 2:
        return "op"
    elif cur_state == 13:
        return "keyw"
    elif cur_state == 19:
        return "id"
    elif cur_state == 24:
        return "num"


def recognize():
    global lex_val
    global entry
    if entry == "":
        result = "endf"
    else:
        if entry[0] in ".,+-:=begind ":
            result = entry[0]
        elif entry[0] in string.digits:
            result = r"\d"
        elif entry[0] in string.ascii_uppercase:
            result = r"\W"
        else:
            result = "error"
        lex_val += entry[0]
        entry = entry[1:]
    return result


entry = "A B C A1 B12 C123 - end + begin := 1,2 123,123 123 1 12 1.2 123.123 3.14 3,14 "#input()
while entry != "":
        print("{0} '{1}'".format(state_machine(), lex_val.strip()))
