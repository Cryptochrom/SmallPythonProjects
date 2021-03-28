from random import choices

'''
This small script will generate random passwords.
It will take some user input regarding length of the password and and its composition.
'''

# generate a list containing all letters in upper case
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# use upper case letter list and generate another list
letters = [i.lower() for i in LETTERS]

# a list containing all numbers from 0 to 9
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# a list containing symbols
symbols = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_",
            "-", "+", "=", "{", "[", "}", "]", "|", "\\", ":", ";", "\"", "'",
            "<", ",", ">", ".", "/"]

print("Hello, this short script will generate a random password for you.")
print("First I have to ask you a few questions, to find out what the requirements for the password are. \n")
print("How long should this password be? We recommend a minimum length of 10 characters.")
PWlength = int(input("> "))

src = []

Le = input("Should upper case letters be included? (y/n): ")
if Le == "y":
    src = src + LETTERS

#print(src)

le = input("Should lower case letters be included? (y/n): ")
if le == "y":
    src = src + letters

#print(src)

nu = input("Should numbers be included? (y/n): ")
if nu == "y":
    src = src + numbers

#print(src)

sy = input("Should symbols be included? (y/n): ")
if sy == "y":
    src = src + symbols

print("We will choose from the following characters: ", src)

# defines a function that does random sampling from list containing all potentially included characters
def PWgeneration(background, PWlength):
    print(f"Generating a random {PWlength} character long password.")
    PW = choices(background, k = PWlength) # random sampling from list with potential characters
    jPW = "".join(PW) # join string together without whitespace
    print("Your new password is:", jPW)

PWgeneration(src, PWlength)
