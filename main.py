from class_playfair import PlayfairCipher
import re

if __name__=="__main__":

    print("\n---- PLAYFAIR CIPHER ----\n")

    # User input
    PLAIN_TXT = input("Enter Text: ").lower()
    KEY = input("Type Key: ").lower()
    MODE = int(input("[1] Encryption\n[0] Decryption\nMode: "))

    # Remove everything except letters a–z
    PLAIN_TXT = re.sub(r'[^a-z]', '', PLAIN_TXT)
    KEY = re.sub(r'[^a-z]', '', KEY)

    # Creating object
    obj=PlayfairCipher(KEY, PLAIN_TXT)

    # Initializing Matrix    
    obj.key_init()
    obj.create_lookup_dicts()

    # Printing Matrix
    obj.display_matrix()

    # Making pairs
    pair_list=obj.make_pairs()
    # Encrypting Text
    CIPHERED_TXT=obj.cipher(pair_list, MODE)

    # Displaying 
    print(f"\nPlain Text: {PLAIN_TXT.upper()}")
    print(f"Key: {KEY.upper()}")
    print(f"Pairs: {pair_list}")
    if MODE:
        print(f"Encrypted Text: {CIPHERED_TXT.upper()}\n")
    else:   
        print(f"Decrypted Text: {CIPHERED_TXT.upper()}\n")