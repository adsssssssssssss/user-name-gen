import random
from unittest import result

char = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
for i in range(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
    frist = ''.join((random.choice(char) for i in range(4)))
    result = frist 
    output = open('useres.txt', 'a')
    output.write(result + '\n')
    print(result)