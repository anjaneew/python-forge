from math import e

# varaible scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Local scope

def fun1():
    a = 1
    print(a) # we cant print other variable cz we cant see it.  

def fun2():
    b = 2 
    print(b) # we cant print other variable cz we cant see it. 

fun1()  #1  
fun2()  #2

# local scope - two different variables in same name

def fun3():
    x = 3 
    print(x)

def fun4():
    x = 13 
    print(x)    

fun3()  #3  
fun4()  #13    

# Enclosed - functions 1st check locally then enclosed

def fun5():
    x = 3 

    def fun6():
        print(x) #3
    fun6()    

fun5()   

# Global - outside of any 

def fun6():
    print(y)

def fun7():
    print(y)    

y = 300

fun6()  #300  
fun7()  #300 

# Built-in

# from math import e - above
# print(e) # e is built in

def fun8():
    print(e)  # e is built in

fun8() # 2.718281828459045    