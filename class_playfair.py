from tabulate import tabulate

class PlayfairCipher:
    # --- Constructor ---
    def __init__(self, key: str, text: str):
        self.key=key
        self.text=text
        self.MATRIX_SIZE=5
        self.MATRIX=[["_" for _ in range(self.MATRIX_SIZE)] for _ in range(self.MATRIX_SIZE)]
        self.temp_list_cipher=[]
        self.alpha_index_dict={}
        self.index_alpha_dict={}

    # --- Matrix / Key setup ---
    def key_init(self):
        ROW=0
        COL=0
        ALPHABETS='abcdefghijklmnopqrstuvwxyz'
        ALPHA_LIST=[alpha for alpha in ALPHABETS]
        ADDED=[]
        problemIJ=True

        # Updating Key in Matrix
        for key in self.key:
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

            self.MATRIX[ROW][COL]=key
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

            self.MATRIX[ROW][COL]=alpha
            ADDED.append(alpha)
            COL+=1  

            if COL == 5:
                COL=0
                ROW+=1

    def create_lookup_dicts(self):
        # Creating dict to keep track of row, col
        for row in range(self.MATRIX_SIZE):
            for col in range(self.MATRIX_SIZE):
                self.alpha_index_dict[self.MATRIX[row][col]] = row, col
                self.index_alpha_dict[row, col] = self.MATRIX[row][col]

    # --- Pair handling ---
    def make_pairs(self) -> list:
        idx=0
        pair_list=[]

        # Converting Plain text str to list
        PLAIN_TXT_LIST=[w for w in self.text]
        
        text_range=len(PLAIN_TXT_LIST)

        while idx < text_range:
            # If only last letter left (adding X)
            if idx + 1 == text_range:
                # If i or j
                if PLAIN_TXT_LIST[idx] == 'i' or PLAIN_TXT_LIST[idx] == 'j':
                    temp='i/j'
                    pairs=(temp, 'x')
                else:
                    pairs=(PLAIN_TXT_LIST[idx], 'x')
                pair_list.append(pairs)
                break
            # If I and J are immediate neighbours
            elif PLAIN_TXT_LIST[idx] == 'i' and PLAIN_TXT_LIST[idx+1] == 'j' or PLAIN_TXT_LIST[idx] == 'j' and PLAIN_TXT_LIST[idx+1] == 'i':
                PLAIN_TXT_LIST.insert(idx+1, 'x')
                # Reseting
                text_range=len(PLAIN_TXT_LIST)
                idx=0
                pair_list.clear()
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
        
    # --- Encryption rules ---
    def same_row_rule(self, row: int, col1: int, col2: int, mode: int):
        if mode == 1:
            # Going right
            new_c1 = col1 + 1
            new_c2 = col2 + 1
            # If out of bounds
            if new_c1 == 5:
                new_c1=0
            if new_c2 == 5:
                new_c2=0

        elif mode == 0:
            # Going left
            new_c1 = col1 - 1
            new_c2 = col2 - 1
            # If out of bounds
            if new_c1 == -1:
                new_c1=4
            if new_c2 == -1:
                new_c2=4

        ciphered_1=self.index_alpha_dict[(row, new_c1)]
        if ciphered_1 == 'i/j':
            self.temp_list_cipher.append('i')
        else:   
            self.temp_list_cipher.append(ciphered_1)
        ciphered_2=self.index_alpha_dict[(row, new_c2)]
        if ciphered_2 == 'i/j':
            self.temp_list_cipher.append('i')
        else:   
            self.temp_list_cipher.append(ciphered_2)
 
    def same_col_rule(self, col: int, row1: int, row2: int, mode: int):
        if mode == 1:
            # Going down
            r1_new = row1 + 1
            r2_new = row2 + 1
            # If out of bounds
            if r1_new == 5:
                r1_new=0
            if r2_new == 5:
                r2_new=0
        if mode == 0:
            # Going up
            r1_new = row1 - 1
            r2_new = row2 - 1
            # If out of bounds
            if r1_new == -1:
                r1_new=4
            if r2_new == -1:
                r2_new=4
        
        ciphered_1=self.index_alpha_dict[(r1_new, col)] 
        if ciphered_1 == 'i/j':
            self.temp_list_cipher.append('i')
        else:   
            self.temp_list_cipher.append(ciphered_1)
        ciphered_2=self.index_alpha_dict[(r2_new, col)] 
        if ciphered_2 == 'i/j':
            self.temp_list_cipher.append('i')
        else:   
            self.temp_list_cipher.append(ciphered_2) 

    def rectangle_rule(self, r1: int, r2: int, c1: int, c2: int):
        # --- Rectangle Rule --- #
        # Going Right
        ciphered_1=self.index_alpha_dict[(r1, c2)]
        if ciphered_1 == 'i/j':
            self.temp_list_cipher.append('i')
        else:   
            self.temp_list_cipher.append(ciphered_1)

        # Going Left
        ciphered_2=self.index_alpha_dict[(r2, c1)]
        if ciphered_2 == 'i/j':
            self.temp_list_cipher.append('i')
        else:   
            self.temp_list_cipher.append(ciphered_2)

    # --- Cipher operations ---
    def cipher(self, pair_list: list, mode: int) -> str:
        self.temp_list_cipher = []

        for pair in pair_list:

            # Unpacking pairs
            p1, p2 = pair

            # Unpacking rows and columns
            row_p1, col_p1 = self.alpha_index_dict[p1]
            row_p2, col_p2 = self.alpha_index_dict[p2]

            # Checking which rule to apply
            if row_p1 == row_p2:
                self.same_row_rule(row_p1, col_p1, col_p2, mode)
            elif col_p1 == col_p2:
                self.same_col_rule(col_p1, row_p1, row_p2, mode)
            else:
                self.rectangle_rule(row_p1, row_p2, col_p1, col_p2)
            
        CIPHERED_TXT="".join(self.temp_list_cipher)
        return CIPHERED_TXT

    # --- Utility ---
    def display_matrix(self):
        # Printing Matrix
        print("\nKEY MATRIX\n")
        print(tabulate(self.MATRIX, tablefmt="grid"))



