# Lab 6 by Alvaro Flores & Sarah Trainor

def main():
    # list of avail functions
    options = [encode, decode, quit]
    while running:
        display_menu()
        # promps for input from menu and runs selected choice
        selection = int(input("Please enter an option: ")) - 1
        options[selection]()


def encode():
    # prompts for password and encodes it.
    global og_password, encoded_pw
    newlist = []
    og_password = input("Please enter your password to encode:")
    for l in og_password:
        if int(l) < 7:
            newlist.append(str(int(l) + 3))
        else:
            newlist.append(str(int(l) - 7))
    encoded_pw = ''.join(newlist)
    print("Your password has been encoded and stored!")
    return encoded_pw


def decode():
    # prints out encoded pw and decoded pw
    newlist = []
    for l in encoded_pw:
        if int(l) < 3:
            newlist.append(str(int(l) + 7))
        else:
            newlist.append(str(int(l) - 3))
    decoded_pw = ''.join(newlist)
    print(f'The encoded password is {encoded_pw}, and the original password is {decoded_pw}.')


def exit():
    # terminate program
    running = False


def display_menu():
    # displays the menu
    print("""
        Menu
        ---------
        1. Encode
        2. Decode
        3. Quit
        """)


if __name__ == '__main__':
    running = True
    og_password = None
    encoded_pw = None
    main()
