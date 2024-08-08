from string import ascii_lowercase
from time import sleep
from os import getenv

ALPHABET     = set(ascii_lowercase + "_")
SECRET_FLAG  = getenv("FLAG", "DEAD{test_flag_which_is_exactly_this_long}")
SECRET_FLAG  = SECRET_FLAG.replace("{", "_").replace("}", "_").replace("DEAD","dead")

assert len(SECRET_FLAG) == 42, "Bad flag length"
assert set(SECRET_FLAG).issubset(ALPHABET), "Bad flag chars"

def get_flag():
    print(SECRET_FLAG)

def split_flag():
    start_offset = int(input("Start of flag substring: "))
    end_offset   = int(input("End of flag substring: "))
    new_flag     = SECRET_FLAG[start_offset:end_offset]
    assert       len(new_flag) >= 13, "Can't have such a small piece"
    anything     = input("Anything to add? Tell me: ").strip()[:20]
    assert       set(anything).issubset(ALPHABET), "That's a crazy thing to add!"
    new_flag     += anything
    globals()[new_flag] = ":)"

if __name__ == "__main__":
    split_flag()
    what_to_do = input("What should I do now? Tell: ")
    if not set(what_to_do).issubset(ALPHABET):
        print("Plz no hack :(")
    else:
        # No brute force for you. Test locally instead!
        sleep(10)
        print(eval(what_to_do))