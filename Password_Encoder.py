# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:52:28 2023

@author: urani
"""

def encoder(user_input):
    password = ''
    
    for i in user_input:
        temp = str(int(i) + 3) 
        if int(i) >= 7:
            password += temp[-1]
        else: password += temp
        #user_input.replace(user_input[i], int(user_input[i]) += 3)
    print(password)
    
def decoder(password):
    pass
    
def main():
    while True:
        user_input = input()
        if user_input.isdigit() == True:
            break
    
    user_input = str(user_input)
    encoder(user_input)
    
if __name__ == '__main__':
    main()