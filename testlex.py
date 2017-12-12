"""
    Лексический анализатор
"""


input_signals = {
    "dot":   "точка",
    "dash":  "тире",
    "space": "пробел",
    "other": "неопознаный символ",
    "endf":  "конец последовательности"
}


next_state = [
    # символы:  .   -    space    other
    # S0
    {
        "dot":    1,
        "dash":   1,
        "space":  2,
        "other": -1
    },
    # S1
    {
        "dot":   -1,
        "dash":  -1,
        "space":  0,
        "other": -1
    }
]


# entry - входная последовательность
# lex_var - значение распознаваемой лексемы


def state_machine():
    """
    function state_machine : lexeme_class;
    var cur_state:state; cur_input:input_signal;
    begin
      lex_val:='';
      cur_state:=s0;
      cur_input:=recognize;
      while (cur_state<>S2) and (cur_input<>endf) do
      begin
        cur_state:=next_state[cur_input, cur_state];
        if cur_state=S_error then
            raise exception.create(‘Лексическая ошибка');
        if cur_state<> s2 then
            cur_input:=recognize;
      end;
      if (cur_state <> S2) and (cur_input=endf) then
        raise exception.create('Лексическая ошибка')
      else
        result:=letter;
    end;
    """
    global lex_val
    lex_val = ""
    cur_state = 0
    cur_input = recognize()
    while (cur_state != 2) and (cur_input != "endf"):
        # print("cur_input = {0}\ncur_state = {1}\n".format(cur_input, cur_state))
        cur_state = next_state[int(cur_state)][cur_input]
        if cur_state == -1:
            raise Exception("Лексическая ошибка !")
        if cur_state != 2:
            cur_input = recognize()
    if (cur_state != 2) and (cur_input == "endf"):
        raise Exception("Лексическая ошибка !")
    else:
        return "letter"


def recognize():
    """
    function recognize:input_signal;
    begin
        if entry='' then
            result:=endf
        else
        begin
            case entry[1] of
                '.': result:=dot;
                '-': result:=dash;
                ' ': result:=space;
                else result:=other
            end;
            lex_val:=lex_val+entry[1];
            entry:=copy(entry, 2,length(entry));
        end;
    end;
    """
    global lex_val
    global entry
    if entry == "":
        result = "endf"
    else:
        if entry[0] == ".":
            result = "dot"
        elif entry[0] == "-":
            result = "dash"
        elif entry[0] == " ":
            result = "space"
        else:
            result = "other"
        lex_val += entry[0]
        entry = entry[1:]
    return result


entry = ". - -  .  . .  - - -  "#input()
while entry != "":
    if state_machine() == "letter":
        print("Буква '{0}'".format(lex_val))
