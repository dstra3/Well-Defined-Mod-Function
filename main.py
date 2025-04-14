# Author: Declan Straut
# Written on 4/14/25 for problem 8.24 of assignment 9 of my Foundations of Math class

# This program tests if the following function is well-defined, i.e. the representation of [x]_base1 does not matter
# f([x]_base1) = [func(x)]_base2

question_c = {
    "base1": 8,
    "base2": 10,
    "func": lambda x : 6*x
}
question_d = {
    "base1": 10,
    "base2": 10,
    "func": lambda x : 6*x
}
question_e = {
    "base1": 43,
    "base2": 43,
    "func": lambda x : 11*x-5
}
question_f = {
    "base1": 15,
    "base2": 15,
    "func": lambda x : 5*x-11
}

verbose = True
classes_to_test = 10
def test(base1: int, base2: int, func):
    failed = False
    for base_num in range(base1): # 0,1,2,...,base1-1
        if verbose:
            print(f"-------Testing [{base_num}]_{base1}-------")
        answer = None
        for scalar in range(classes_to_test): # Try several congruent classes
            scaled_num = base_num + base1*scalar
            func_output = func(scaled_num) % base2
            if answer == None:  # save base answer to compare to outputs from other classes
                answer = func_output
            if verbose:
                print(f"f([{scaled_num}]_{base1}) = [{func_output}]_{base2}", end="")
            if func_output != answer:
                if verbose:
                    print("\t!!!FAILED!!!")
                failed = True
            else:
                if verbose:
                    print()
    if failed:
        print("!!!NOT a well-defined function!!!")
    else:
        print("***Well-defined function***")

# -------------------------------------------------------------
print("----------Part c----------")
test(**question_c)
print("----------Part d----------")
test(**question_d)
print("----------Part e----------")
test(**question_e)
print("----------Part f----------")
test(**question_f)
