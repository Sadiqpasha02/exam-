import Time
import os,csv 

def select():
    x = input("Enter the mode of examination (neet(1)/jee(2)): ")
    y = input("Enter mode of exam (full paper(f)/subject paper(s)): ")

    try:
        if y == "s":
            if x == "1":
                s = input("Choose subject (botany(b)/zoology(z)/physics(p)/chemistry(c)): ")
                if s == "b":
                    a = Neet_b()
                elif s == "z":
                    a = Neet_z()
                elif s == "p":
                    a = Neet_p()
                elif s == "c":
                    a = Neet_c()
                else:
                    raise ValueError("Invalid subject selected!")
            elif x == "2":
                s = input("Choose subject (physics(p)/chemistry(c)/maths(m)): ")
                if s == "c":
                    a = jee_c()
                elif s == "m":
                    a = jee_m()
                elif s == "p":
                    a = jee_p()
                else:
                    raise ValueError("Invalid subject selected!")
        elif y == "f":
            if x == "1":
                a = Neet_f()
            elif x == "2":
                a = jee_f()
            else:
                raise ValueError("Invalid mode of examination selected!")
        else:
            raise ValueError("Invalid mode of exam!")
        return a
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

# NEET functions for selecting papers
def Neet_f():
    print("Select question paper (NEET full):")
    pyq = input("neet 1 (1)/neet 2 (2)/neet 3 (3): ")
    if pyq == "1":
        return "./neet/neetf/neet1.txt", "./neet/neetf/neet1key.txt", 3.0
    elif pyq == "2":
        return "./neet/neetf/neet2.txt", "./neet/neetf/neet2key.txt", 3.0
    elif pyq == "3":
        return "./neet/neetf/neet3.txt", "./neet/neetf/neet3key.txt", 3.0

def Neet_b():
    print("Select NEET botany paper:")
    bq = input("neet botany 1 (1)/neet botany 2 (2)/neet botany 3 (3): ")
    if bq == "1":
        return "./neet/neets/neetb1.txt", "./neet/neets/neetb1key.txt", 0.5
    elif bq == "2":
        return "./neet/neets/neetb2.txt", "./neet/neets/neetb2key.txt", 0.5
    elif bq == "3":
        return "./neet/neets/neetb3.txt", "./neet/neets/neetb3key.txt", 0.5

def Neet_z():
    print("Select NEET zoology paper:")
    zq = input("neet zoology 1 (1)/neet zoology 2 (2)/neet zoology 3 (3): ")
    if zq == "1":
        return "./neet/neets/neetz1.txt", "./neet/neets/neetz1key.txt", 0.5
    elif zq == "2":
        return "./neet/neets/neetz2.txt", "./neet/neets/neetz2key.txt", 0.5

def Neet_p():
    print("Select NEET physics paper:")
    pq = input("neet physics 1 (1)/neet physics 2 (2)/neet physics 3 (3): ")
    if pq == "1":
        return "./neet/neets/neetp1.txt", "./neet/neets/neetp1key.txt", 1.0
    elif pq == "2":
        return "./neet/neets/neetp2.txt", "./neet/neets/neetp2key.txt", 1.0

def Neet_c():
    print("Select NEET chemistry paper:")
    cq = input("neet chemistry 1 (1)/neet chemistry 2 (2)/neet chemistry 3 (3): ")
    if cq == "1":
        return "./neet/neets/neetc1.txt", "./neet/neets/neetc1key.txt", 1.0
    elif cq == "2":
        return "./neet/neets/neetc2.txt", "./neet/neets/neetc2key.txt", 1.0

# JEE functions for selecting papers
def jee_f():
    print("Select question paper (JEE full):")
    pyq = input("jee 1 (1)/jee 2 (2)/jee 3 (3): ")
    if pyq == "1":
        return "./jee/jeef/jee1.txt", "./jee/jeef/jee1key.txt", 3.0
    elif pyq == "2":
        return "./jee/jeef/jee2.txt", "./jee/jeef/jee2key.txt", 3.0

def jee_m():
    print("Select JEE maths paper:")
    mq = input("jee maths 1 (1)/jee maths 2 (2)/jee maths 3 (3): ")
    if mq == "1":
        return "./jee/jees/jeem1.txt", "./jee/jees/jeem1key.txt", 1.0
    elif mq == "2":
        return "./jee/jees/jeem2.txt", "./jee/jees/jeem2key.txt", 1.0

def jee_p():
    print("Select JEE physics paper:")
    pq = input("jee physics 1 (1)/jee physics 2 (2)/jee physics 3 (3): ")
    if pq == "1":
        return "./jee/jees/jeep1.txt", "./jee/jees/jeep1key.txt", 1.0
    elif pq == "2":
        return "./jee/jees/jeep2.txt", "./jee/jees/jeep2key.txt", 1.0

def jee_c():
    print("Select JEE chemistry paper:")
    cq = input("jee chemistry 1 (1)/jee chemistry 2 (2)/jee chemistry 3 (3): ")
    if cq == "1":
        return "./jee/jees/jeec1.txt", "./jee/jees/jeec1key.txt", 1.0
    elif cq == "2":
        return "./jee/jees/jeec2.txt", "./jee/jees/jeec2key.txt", 1.0

# Exam function (to handle the exam logic)
def exam(Qpaper, key_sheet, Time):
    print(f"Starting exam for {Time} hours...")
    # Implement the logic for timing and handling the question paper here
     # Simulate the exam time
    # def Questions():
    #     file = open(r,Qpaper)
    #     x = file.readlines(3)
    #     def read_Question():
    #         print ("\r",x[1]," "*25)
    #         print ("\r",x[2]," "*25)
    #         print ("\r",x[3]," "*25)
    #         print ("enter the ans or press :")
    #         print ("p for previous question ")
    #         print ("n for next question ")
    #         print ("s to submit")
    #         print ("the no of the question to reach the respective question")
    #         ans = input (":")
    #         return ans,len(x[1])+len(x[2])+len(x[3])
    #     ans,len = read_Question()
    #     if ans == "p":
    #         cpos= f.tell()
    #         f.seek(cpos-len-3)
    # x = Time.timer(hours) 


# Main script execution
top = select()
if top:
    print(f"Selected exam: {top}")
    exam(top[0], top[1], top[2])
