# Playfair Cipher in Python

This project is a Python implementation of the **Playfair Cipher**, a classical polygraphic substitution cipher invented in 1854 by Charles Wheatstone and promoted by Lord Playfair (hence the name).  

The cipher encrypts **pairs of letters (digraphs)** instead of single letters, making frequency analysis attacks harder than simple substitution ciphers.

---

## How Playfair Cipher Works  

### 1. Key Matrix Setup (5×5 grid)  
- A keyword is written into a 5×5 matrix (no repeated letters).  
- The rest of the alphabet is filled in order.  
- Traditionally, **I and J share one cell**.  

---

### 2. Preprocessing Plaintext  
- Convert text to lowercase.  
- Remove spaces and punctuation.  
- Replace `j` with `i` (if following the `i/j` rule).  
- Split into **pairs of letters**:  
  - If both letters are the same → insert an `"x"` between them.  
  - If odd number of letters → append `"x"` at the end.  


---

### 3. Encryption Rules  
For each pair of letters:  

- **Same Row** → Replace each letter with the letter **to its right** (wrap around if needed).  
- **Same Column** → Replace each letter with the letter **below it** (wrap around if needed).  
- **Rectangle Rule** → Each letter is replaced with the letter in the **same row but column of the other letter**.  

---

### 4. Decryption  
- Reverse the same rules:  
  - Right → Left  
  - Down → Up  
  - Rectangle rule remains the same.  

---

## How to Run  

```bash
python playfair_cipher.py
```

## Example
Enter Text: hellcraft

Type Key: australia

KEY MATRIX
A   U   S   T   R
L   I/J B   C   D
E   F   G   H   K
M   N   O   P   Q
V   W   X   Y   Z

Plain Text: HELLCRAFT
Key: AUSTRALIA
Pairs: [('h', 'e'), ('l', 'x'), ('l', 'c'), ('r', 'a'), ('f', 't')]
Encrypted Text: UBNNQBBUPZ






