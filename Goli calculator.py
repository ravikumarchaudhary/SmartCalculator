# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 07:54:10 2020

@author: ASUS
"""
from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer


responses=["Your welcome to Google Assistant ",
           "My name is Punnu Gullu","Sorry","Thanks","Out of range"]

def add(a,b):
    return a+b


def sub(a,b):
    return a-b


def mul(a,b):
    return a*b


def divide(a,b):
    return a/b


def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
        
        
        
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
        
        
        
def fact(a,b):
    f=1
    for i in range(1,a+1):
        f*=i
    return f
def end():
    print(responses[3])
    input("Press Enter key to exit")
    exit()
    
    
    
    
def myname():
    print(responses[1])
    
    
    
def sorry():
    print(responses[4])
    
    
    
def inv():
    print("Mr.RAVI CHAUDHARY INVENTED ME")

    
commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end,"INVENTED":inv}    




# main dictionary .....
ope={
     "ADDITION":add,
     "ADD":add,
     "PLUS":add,
     "SUM":add,
     "SUBTRACT":sub,
     "SUBTRACTION":sub,
     "DIFFERENCE":sub,
     "MINUS":sub,
     "MULTIPLY":mul,
     "PRODUCT":mul,
     "MULTIPLICATION":mul,
     "DIVISION":divide,
     "DIVIDE":divide,
     "FACTORIAL":fact,
     "LCM":lcm,
     "HCF":hcf
     }









def ravi(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)
    
    
    

print("\t \t","* ",responses[0]," *")
#print()
print("\t \t \t","* ",responses[1]," *")
print()

li=[]
li1=[]
li2=[]
li3=[]

while True:
    text=input("Enter some text :")
    #sentence tokenizer
    #print("\n sentence tokenizer :")
    #print(sent_tokenize(input_text))
    li1=sent_tokenize(text)
    for i in li1:
        li.append(i)

    # word tokenizer
    #print("\n word tokenizer :")
    #print(word_tokenize(input_text))
    li2=word_tokenize(text)
    for i in li2:
        li.append(i)

    # wordpunct tokenizer
    #print("\n word punct tokenizer :")
    #print(WordPunctTokenizer().tokenize(input_text))
    li3=WordPunctTokenizer().tokenize(text)
    for i in li3:
        li.append(i)
        
    #print(li)
     
    for word in li:
    #for word in text.split(' '):
        #l=ravi(text)
        if word.upper() in ope.keys():
            try:
                l=ravi(text)
                #print(len(l))
                r=ope[word.upper()](l[0],l[1])
                print(r)
            except:
                print("Something wrong")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()