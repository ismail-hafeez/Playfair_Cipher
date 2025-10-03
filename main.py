from tabulate import tabulate

MATRIX_SIZE=5
MATRIX=[["_" for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]
temp_list_cipher=[]
alpha_index_dict={}
index_alpha_dict={}

def key_init(KEY,ROW=0, COL=0, problemIJ=True):
    
    ALPHABETS='abcdefghijklmnopqrstuvwxyz'

    ALPHA_LIST=[alpha for alpha in ALPHABETS]
    ADDED=[]

    # Updating Key in Matrix
    for key in KEY:
        if key in ADDED:
            continue

        if (key == 'i' or key == 'j') and problemIJ:
            if key=='i':
                key+='/j'
            if key=='j':
                key+='/i'

            problemIJ=False
            ADDED.append('i')
            ADDED.append('j')

        MATRIX[ROW][COL]=key
        ADDED.append(key)
        COL+=1  

        if COL == 5:
            COL=0
            ROW+=1

    # Updating alphabets in Matrix
    for alpha in ALPHA_LIST:
        if alpha in ADDED:
            continue

        if (alpha == 'i' or alpha == 'j') and problemIJ:
            if alpha=='i':
                alpha+='/j'
            if alpha=='j':
                alpha+='/i'

            problemIJ=False
            ADDED.append('i')
            ADDED.append('j')
        
        if ROW==5:
            break

        MATRIX[ROW][COL]=alpha
        ADDED.append(alpha)
        COL+=1  

        if COL == 5:
            COL=0
            ROW+=1

    # Creating dict to keep track of row, col
    for row in range(MATRIX_SIZE):
        for col in range(MATRIX_SIZE):
            alpha_index_dict[MATRIX[row][col]] = row, col
            index_alpha_dict[row, col] = MATRIX[row][col]

def same_row_rule(r, c1, c2):
    # Going right
    c1_right = c1 + 1
    c2_right = c2 + 1

    # If out of bounds
    if c1_right == 5:
        c1_right=0
    ciphered_1=index_alpha_dict[(r, c1_right)]
    if ciphered_1 == 'i/j':
        temp_list_cipher.append('i')
    else:   
        temp_list_cipher.append(ciphered_1)
    
    if c2_right == 5:
        c2_right=0
    ciphered_2=index_alpha_dict[(r, c2_right)]
    if ciphered_2 == 'i/j':
        temp_list_cipher.append('i')
    else:   
        temp_list_cipher.append(ciphered_2)

def same_col_rule(c, r1, r2):
    # Going down
    r1_down = r1 + 1
    r2_down = r2 + 1

    # If out of bounds
    if r1_down == 5:
        r1_down=0
    ciphered_1=index_alpha_dict[(r1_down, c)] 
    if ciphered_1 == 'i/j':
        temp_list_cipher.append('i')
    else:   
        temp_list_cipher.append(ciphered_1)
    
    if r2_down == 5:
        r2_down=0
    ciphered_2=index_alpha_dict[(r2_down, c)] 
    if ciphered_2 == 'i/j':
        temp_list_cipher.append('i')
    else:   
        temp_list_cipher.append(ciphered_2)  

def rectangle_rule(r1,r2,c1,c2):
    # --- Rectangle Rule --- #
    # Going Right
    ciphered_1=index_alpha_dict[(r1, c2)]
    if ciphered_1 == 'i/j':
        temp_list_cipher.append('i')
    else:   
        temp_list_cipher.append(ciphered_1)

    # Going Left
    ciphered_2=index_alpha_dict[(r2, c2)]
    if ciphered_2 == 'i/j':
        temp_list_cipher.append('i')
    else:   
        temp_list_cipher.append(ciphered_2)

def encrypt_text(pair_list):

    for pair in pair_list:

        # Unpacking pairs
        first, second = pair

        # Unpacking rows and columns
        row_first, col_first = alpha_index_dict[first]
        row_second, col_second = alpha_index_dict[second]

        # Checking which rule to apply
        if row_first == row_second:
            same_row_rule(row_first, col_first, col_second)

        elif col_first == col_second:
            same_col_rule(col_first, row_first, row_second)
        else:
            rectangle_rule(row_first,row_second,col_first,col_second)
            
    CIPHERED_TXT="".join(temp_list_cipher)
    
    return CIPHERED_TXT

def make_pairs(PLAIN_TXT):
    idx=0
    pair_list=[]

    # Converting Plain text str to list
    PLAIN_TXT_LIST=[w for w in PLAIN_TXT]
    
    text_range=len(PLAIN_TXT_LIST)

    while idx < text_range:
        # If only last letter left (adding X)
        if idx + 1 == text_range:
            pairs=(PLAIN_TXT_LIST[idx], 'x')
            pair_list.append(pairs)
            break
        # Making Pairs if not same
        elif PLAIN_TXT_LIST[idx] != PLAIN_TXT_LIST[idx+1]:
            if PLAIN_TXT_LIST[idx] == 'i' or PLAIN_TXT_LIST[idx] == 'j':
                temp='i/j'
                pairs=(temp, PLAIN_TXT_LIST[idx+1])
            elif PLAIN_TXT_LIST[idx+1] == 'i' or PLAIN_TXT_LIST[idx+1] == 'j':
                temp='i/j'
                pairs=(PLAIN_TXT_LIST[idx], temp)
            else:
                pairs=(PLAIN_TXT_LIST[idx], PLAIN_TXT_LIST[idx+1])
            idx+=2
            pair_list.append(pairs)
        # If same alphabets encountered
        elif PLAIN_TXT_LIST[idx] == PLAIN_TXT_LIST[idx+1]:
            PLAIN_TXT_LIST.insert(idx+1, 'x')
            # Reseting
            text_range=len(PLAIN_TXT_LIST)
            idx=0
            pair_list.clear()

    return pair_list

if __name__=="__main__":

    # User input  
    PLAIN_TXT = input("Enter Text: ").replace(" ", "").lower()
    KEY = input("Type Key: ").replace(" ", "").lower()

    # Initializing Matrix    
    key_init(KEY)

    # Printing Matrix
    print("\nKEY MATRIX\n")
    print(tabulate(MATRIX, tablefmt="grid"))

    # Making pairs
    pair_list=make_pairs(PLAIN_TXT)
    # Encrypting Text
    CIPHERED_TXT=encrypt_text(pair_list)

    # Displaying 
    print(f"\nPlain Text: {PLAIN_TXT.upper()}")
    print(f"Key: {KEY.upper()}")
    print(f"Pairs: {pair_list}")
    print(f"Encrypted Text: {CIPHERED_TXT.upper()}\n")