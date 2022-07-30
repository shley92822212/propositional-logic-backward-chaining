symbols = {"and": "^", "or": "v", "implies": "=>"}
prefix = "reasoning>>"
debug = True
def pretty_print(s):
        print(prefix, s)

class Fact:
        valid = None
        operator = None
        variables = None
        result = None
        true = None
        def __init__(self, fact_str):
                #remove spaces
                fact_str = fact_str.replace(" ", "")

                if symbol["implies"] not in fact_str:
                        if not fact_str:
                                if debug:
                                        pretty_print("Error, empty input")
                                self.valid = False
                                return
                        self.result = fact_str
                        self.true = True

                #split
                lhs, rhs = fact_str.split(symbols["implies"], 1)

                # Check if empty
                if not lhs or not rhs:
                        if debug:
                                pretty_print("Error, empty input")
                        self.valid = False
                        return

                #check for implies
                if symbols["implies"] in rhs:
                        if debug:
                                pretty_print("Error, too many implies")
                        self.valid = False
                        return

                #remove double operators
                for s in [lhs, rhs]:
                        for op in [symbols["and"], symbols["or"]]:
                                while op+op in s:
                                        s.replace(op+op, op)

                #check only and xor or in lhs
                if symbols["and"] in lhs and symbols["or"] in lhs:
                        if debug:
                                pretty_print("Error, too many ands and ors in lhs")
                        self.valid = False
                        return

                #check rhs is only a fact
                if symbols["and"] in lhs or symbols["or"] in rhs:
                        if debug:
                                pretty_print("Error, too many ands or ors in rhs")
                        self.valid = False
                        return

                # validation done :D
                self.valid = True


                # set operator
                if symbols["and"] in lhs:
                        self.operator = symbols["and"]
                elif symbols["or"] in lhs:
                        self.operator = symbols["or"]
                else:
                        self.operator = symbols["implies"]

                # set letters
                if self.operator = symbols["implies"]:
                        self.variables = [lhs]
                else:
                        self.variables = lhs.split(self.operator)

                self.result = rhs

def check_fact(fact, fact_dict):
        if fact not fact_dict:
                return False


        if fact_dict[fact].true:
                return True
        elif fact_dict[fact].operator = symbols["implies"]:
                return check_fact(fact_dict[fact].variables[0])
        elif fact_dict[fact].operator = symbols["or"]:
                for variable in fact_dict[fact].variables:
                        if check_fact(fact_dict[fact]):
                                return True
                return False
        elif fact_dict[fact].operator = symbols["and"]:
                for variable in fact_dict[fact].variables:
                        if not check_fact(fact_dict[fact]):
                                return False
                return True

def main():
        pretty_print("This is an extended propositional backward chaining")
        pretty_print("system. Your knowledge base can only accept")
        pretty_print("facts like")
        pretty_print("P1^P2^...^Pk=>P, or")
        pretty_print("P1vP2v...vPk=>P, or")
        pretty_print("P.")
        pretty_print("Now please input your knowledge base! When you finish")
        pretty_print("your input, just type nil!")
        facts = {}
        user_input = input(prefix + " ")
        while user_input != "nil":
                fact = Fact(user_input)
                if not fact.valid:
                        pretty_print("Failed to input fact, please try again")
                else:
                        facts[fact.result] = fact
                user_input = input(prefix + " ")
        pretty_print("You have finished your input. Now you can test your system!")
        user_input = input(prefix + " ")
        while user_input != "exit":
                if not user_input:
                        pretty_print("Error, input not recognised please try again")
                if "?" in user_input:
                        user_input = user_input.replace("?", "")
                if check_fact(user_input, facts):
                        print("yes")
                else:
                        print("no")


if __name__ == '__main__':
        main()

input("Press any key to exit: ")
input("Press any key to exit: ")