from collections import Counter

PLAIN_TXT="ismailhafeez"
KEY="Australia"
ALPHABETS='abcdefghijklmnopqrstuvwxyz'
ALPHA_LIST=[]
MATRIX_SIZE=5
MATRIX=[["_" for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]
ADDED=[]

KEY=KEY.lower()

def key_init(ROW=0, COL=0, problemIJ=True):

    my_counter=Counter(ALPHABETS)
    ALPHA_LIST=list(my_counter.elements())

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

def same_row_rule():

    pass

def make_pairs():

    iter=1

    if PLAIN_TXT[iter] != KEY[iter]:
        pairs=(PLAIN_TXT[iter],KEY[iter])

    if PLAIN_TXT[iter] and KEY[iter]:

        pass
    
    print("\n", pairs)

def encrypt_text():
    pass

if __name__=="__main__":
    key_init()

    print('\nKEY MATRIX\n')
    for cell in MATRIX:
        print(cell)

    encrypt_text()
    make_pairs()

    print(f"\nPlain Text: {PLAIN_TXT}")
    print(f"Key: {KEY}")
    print(f"Encrypted Text: {KEY}\n")