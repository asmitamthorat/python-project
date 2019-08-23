

import os
import json

Fname = {'SPORT': 'sport.json', 'MATH': 'math.json'}
QData = {1: 'MATH', 2:'SPORT'}

def __openFile(Flag):
    sourceJsonPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), Fname[Flag])
    with open(sourceJsonPath, 'r') as f:
        distros_dict = json.load(f)
        return distros_dict

def quiz():
    print("Select quiz : \n 1. Math quiz \n 2. Sport quiz")
    ch = int(input("Enter your choice : "))
    cnt=0
    if ch in QData.keys():
        Data = __openFile(QData[ch])
        for q in Data.keys():
            print(Data[q]['q'])
            for key, value in Data[q]['opt'].items():
                print("{} : {}".format(key, value))

            a=int(input('Enter correct option:'))
            b=Data[q]['answer']
            if a==int(b):
                print('Your answer is Correct')
                cnt+=1
            else:
                print('Entered option is wrong.....Correct option is',b)
            
                
        print(' Your Score is',cnt)
                
        
                
                
    else:
        print("You entered wrong option")

def main():
    quiz()

if __name__ == '__main__':
    main()
