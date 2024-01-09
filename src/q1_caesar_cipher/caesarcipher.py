import subprocess  # python library to give an ability for the user to auto-copy text

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # constant for keeping an alphabet


# method to check decision and return correct output for the user in console
def key_nums(decision):
    return 25 if decision == 'e' else 26


# method to check decision and return correct output for the user in console
def dictionary_key(decision):
    return 'encrypted' if decision == 'e' else 'decrypted'


# method to handle the user's choice about the mode of the cipher
def get_mode():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt?\n").lower()
        if choice in ['e', 'd']:
            return choice
        else:
            print("Invalid choice! Please enter 'e' for encrypt or 'd' for decrypt.")


# method to handle the user's choice about the key of the cipher
def get_key(mode):
    while True:
        mov_key = int(input(f'Please enter the key (0 to {key_nums(mode)}) to use.\n'))
        if 0 <= mov_key <= key_nums(mode):
            return mov_key
        else:
            print(f"Invalid key! Please enter a key between 0 and {key_nums(mode)}.")


def optimized_cipher_manipulations(mode, key, res_msg=''):
    message = input("Enter the message to encrypt.\n").upper()  # input message, .upper() method makes input CAPSLOCK

    key = -key if mode == 'd' else key  # ternary operator to use the correct key with the proper mode

# logic of the caesar cipher
    for word in message.split():  # splitting message with separate words
        for i in word:
            if i.isalpha():  # .isalpha(): check alphabet letters (a-z) to encrypt/decrypt only letters
                index = ABC.find(i.upper())
                new_index = (index + key) % len(ABC)
                decrypted_char = ABC[new_index].lower() if i.islower() else ABC[new_index].upper()
                res_msg += decrypted_char
            else:
                res_msg += i
        res_msg += ' '
    print(res_msg)  # return encrypted/decrypted message

    subprocess.run("pbcopy", text=True, input=res_msg)  # subprocess library, auto-copy text to RAN
    print(f"Full {dictionary_key(mode)} text copied to clipboard.\nor\n")


# entry point
def main():
    while True:
        mode = get_mode()
        mov_key = get_key(mode)
        optimized_cipher_manipulations(mode, mov_key)


if __name__ == "__main__":
    main()
