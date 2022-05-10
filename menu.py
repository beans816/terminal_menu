import os, re, funTree

regex_options = { }

##### CLEARS TERMINAL #####
os.system("clear")

#############   REGEX FILTERING   #############

class option_Regex:
    def __init__(self, description, fun):
        self.description = description
        self.fun = fun

def Choice1(position, description, fun):
    regex_options[position] = option_Regex(description,fun)

def userInput_regex():
    print("_______________")
    Input_re = input("    Input: ")
    print("===============")
    return regex_options[Input_re]

def allregex_descriptions():
    print("_________")
    os.system('printf "\e[6;33mCHOICE 1\e[0m\n"')
    print("=========\n")
    for k in regex_options:
        print(regex_options[k].description)

def getRegex():
    allregex_descriptions()
    try:
        Input_re = userInput_regex()
        return Input_re.fun()
    except KeyError:
        print('\n')
        os.system('printf "\e[6;33m invalid input \e[0m"')
        print('\n')        
        ##### CLEARS TERMINAL #####
        os.system("sleep 2 && clear")
        allregex_descriptions()
        return getRegex()


Choice1("1","1 : Option 1", lambda : funOption1())
Choice1("2","2 : Option 2", lambda : funOption2())
Choice1("e","e : exit", lambda : exit())
                    
def process_Regex ():
    return getRegex()
    
regex = str(process_Regex())

##### CLEARS TERMINAL #####
os.system("clear")

#############   DOWNLOADING MENU && DICTIONARY   #############

uncache_options = { }

class option_Choose:
    def __init__(self, choice_descriptions, fun_choose):
        self.choice_descriptions = choice_descriptions
        self.fun_choose = fun_choose


def Choice2(position, choice_descriptions, fun_choose):
    uncache_options[position] = option_Choose(choice_descriptions,fun_choose)
    return uncache_options[position]

def userInput_choose():
    print("_______________")
    Input_ch = input("    Input: ")
    print("===============")
    return uncache_options[Input_ch]

def allchoice_descriptions():
    print("_______________")
    os.system('printf "\e[6;33mCHOICE 2\e[0m\n"')
    print("===============\n")
    for k in uncache_options:
        print(uncache_options[k].choice_descriptions)

def extract_Error():
    try:
        Input_ch = userInput_choose()
        return Input_ch.fun_choose()
    except KeyError:
        print('\n')
        os.system('printf "\e[6;33m invalid input \e[0m"')
        print('\n')
        ##### CLEARS TERMINAL #####
        os.system("sleep 2 && clear")
        return getChoice()
    
def getChoice():
    allchoice_descriptions()
    extract_Error()

Choice2("1","1 : Option1a", lambda : funOption1a())
Choice2("2","2 : Option1b", lambda : funOption1b())
Choice2("3","3 : Option2a", lambda : funOption2a())
Choice2("4","4 : Option2b", lambda : funOption2b())
Choice2("5","5 : exit", lambda : exit())

                    
def process_Choice ():
    return getChoice()

print(process_Choice())  
