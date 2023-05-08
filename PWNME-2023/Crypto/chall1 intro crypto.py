#!/usr/bin/env python3
from itertools import cycle

FLAG_ENCRYPTED = open("./message-encrypted.txt", "r").read().split(',')
CLUE = "S*********s***y***k************w***s****************n***********************P***********_r*4*********************o***uck*****t******************"
SECRET_LENGHT = 16


clue_blocks = [CLUE[i:i+SECRET_LENGHT] for i in range(0, len(CLUE), SECRET_LENGHT)]
print(clue_blocks)
SECRET = ['']*SECRET_LENGHT

for i in range(len(clue_blocks)):
    for j in range(len(clue_blocks[i])):
        
        if clue_blocks[i][j] != "*":
            charIndex = j + i*SECRET_LENGHT     
            print(charIndex)       
            SECRET[j] = (ord(CLUE[charIndex]) ^ int(FLAG_ENCRYPTED[charIndex]))
            
            

def decrypt():
    return ''.join(chr((int(a) ^ b)) for a, b in zip(FLAG_ENCRYPTED, cycle(SECRET)))

print(decrypt())