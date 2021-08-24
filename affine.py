# Liam Morrison
# affine cipher
# V 1.0
ALPHA_LIST=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
INV = [[1], [3, 9], [5, 21], [7, 15], [11, 19], [17, 23], [25]]
A_VALUES = [1, 3, 5, 9, 11, 15, 17, 19, 21, 21, 23, 25]


def go_again():
    while True:
        go = 0
        try:
            go = int(input("enter 1 to go again or 2 for exit: "))
            if go == 1 or go == 2:
                return go
        except ValueError:
            pass
        print("Invalid input")  
        
        
def hide_or_unhide():
    while True:
        crpt = 0
        try:
            crpt = int(input("enter 1 for enyncription or 2 for decrption: "))
            if crpt == 1 or crpt == 2:
                return crpt
        except ValueError:
            pass
        print("Invalid input")


def get_new_letter(letter, a, b):
    index_let = ALPHA_LIST.index(letter)
    new_let_index = index_let * a + b
    return ALPHA_LIST[new_let_index % 26]


def get_old_letter(letter, a, b):
    index_let = ALPHA_LIST.index(letter)
    old_let_index = a * (index_let - b)
    return ALPHA_LIST[old_let_index % 26]


def encrpt():
    a = ""
    b = ""
    while True:
        try:
            a = int(input(f"select an 'a' value from this list {A_VALUES} (NOTE! to dycrpt you must remember this value!): "))
            if a in A_VALUES:
                b = int(input("enter a 'b' value (NOTE! to dycrpt you must remember this value!): "))
                break
        except ValueError:
            pass
        print("Invalid input")
    word = input("enter the word that you want to encrpt(NOTE! spaces will be deleted!): ")
    word = word.replace(" ", "")
    encrption = ""
    for letter in word:
        replacement = get_new_letter(letter, a, b)
        encrption = encrption + replacement
    print(encrption)


def dycrpt():
    a = ""
    b = ""
    while True:
        try:
            a = int(input(f"select an 'a' value from this list {A_VALUES} (NOTE! this by be the original 'a' value!): "))
            if a in A_VALUES:
                b = int(input("enter a 'b' value (NOTE! this by be the original 'a' value!): "))
                break
        except ValueError:
            pass
        print("Invalid input")
    crip = input("enter the criptext that you want to dycrpt: ")
    crip = crip.replace(" ", "")
    a_inv = 0
    for i in INV:
        if a in i:
            if a == i[0]:
                a = i[1]
            else:
                a = i[0]
    word = ""
    for letter in crip:
        old_letter = get_old_letter(letter, a, b)
        word = word + old_letter
    print(word)
    

def main():
    ans = hide_or_unhide()
    if ans == 1:
        encrpt()
    else:
        dycrpt()
    again = go_again()
    if again == 1:
        main()
main()