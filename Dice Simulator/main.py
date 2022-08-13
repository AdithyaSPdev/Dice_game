# this is a simple dice simulator
import random
from time import sleep

def dice():
    print('Your dice is spinning')
    sleep(1)
    
    dices  = [1,2,3,4,5,6]
    
    print(random.choice(dices))

dice()
