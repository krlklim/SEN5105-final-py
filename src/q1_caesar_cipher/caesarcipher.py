import subprocess

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def key_nums(decision):
    return 25 if decision == 'e' else 26


def dictionary_key(decision):
    return 'encrypted' if decision == 'e' else 'decrypted'


def get_mode():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt?\n").lower()
        if choice in ['e', 'd']:
            return choice
        else:
            print("Invalid choice! Please enter 'e' for encrypt or 'd' for decrypt.")


def get_key(mode):
    while True:
        mov_key = int(input(f'Please enter the key (0 to {key_nums(mode)}) to use.\n'))
        if 0 <= mov_key <= key_nums(mode):
            return mov_key
        else:
            print(f"Invalid key! Please enter a key between 0 and {key_nums(mode)}.")


def optimized_cipher_manipulations(mode, key, res_msg=''):
    message = input("Enter the message to encrypt.\n").upper()

    key = -key if mode == 'd' else key

    for word in message.split():
        for i in word:
            if i.isalpha():
                index = ABC.find(i.upper())
                new_index = (index + key) % len(ABC)
                decrypted_char = ABC[new_index].lower() if i.islower() else ABC[new_index].upper()
                res_msg += decrypted_char
            else:
                res_msg += i
        res_msg += ' '
    print(res_msg)

    subprocess.run("pbcopy", text=True, input=res_msg)
    print(f"Full {dictionary_key(mode)} text copied to clipboard.\nor\n")


def main():
    while True:
        mode = get_mode()
        mov_key = get_key(mode)
        optimized_cipher_manipulations(mode, mov_key)


if __name__ == "__main__":
    main()
