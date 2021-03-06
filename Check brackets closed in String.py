# -*- coding: utf-8 -*-
"""
Created on Thu May 24 15:24:11 2018

@author: selem
"""

def checkio(expression):
    stack = []
    for i in range(len(expression)):
        
        if expression[i]=='{':
            stack.append(expression[i])
        elif expression[i]=='(':
            stack.append(expression[i])
        elif expression[i]=='[':
            stack.append(expression[i])
        
        #to handle when extra bracket at the end    
        
        if expression[i]=='}':
            if len(stack)==0:
                return False
            temp = stack.pop()
            if temp != "{":
                return False
        elif expression[i]==')':
            if len(stack)==0:
                return False
            temp = stack.pop()
            if temp != "(":
                return False
        elif expression[i]==']':
            if len(stack)==0:
                return False
            temp = stack.pop()
            if temp != "[":
                return False      
    if len(stack)==0:
            return True
    else: 
        return False
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
