#1 	Prints "turkey".
#2-27 	Prints the (opcode-1)th letter.
#28 	Prints a space.
#29 	Asks for input and stores it to 43.
#30-39 	Prints the (opcode-30)th number.
#40 	Is an if statement.
#41 	Is an equals sign.
#42 	Is an infinite loop. Another 42 will close the loop.
#43 	Is the only variable.
#44-infinity 	Is (opcode-44). 

def read(code):
    y = []
    for i in code:
        y.append(i.split())
    return y
        

def Turkey(code):
    for i in code:
        i = len(i)
        while 1:
            if i == 1: 
                print("turkey")
            elif i >= 2 and i <= 27: 
                print(chr(i+95), end="")
            elif i == 28: 
                print("", end="")
            elif i == 29:
                put = input()
            elif i >= 30 and i <= 39:
                print(i-30, end="")
            elif i == 40:
                pass
            elif i == 41:
               pass
            elif i == 42:
                pass
            elif i == 43:
                pass
            elif i <= 44:
                i = i-44
            else: break
        
my_file = open("Turkey", "r")
code = my_file.read().split("\n")
my_file.close()
c = read(code)
Turkey(c)