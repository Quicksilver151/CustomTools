#!/bin/python3

import random




def main():
    

    x = input("x:  ")
    y = input("y:  ")

    try:
        x = int(x)
        y = int(y)
    except Exception:
        print("incorrect input/inputs")
        return


    while True:

        randx = random.randint(1,x)
        randy = random.randint(1,y)
        
        grid = []

        for i in range(x):

            grid.append("")
           
            for j in range(y):

                if randx == i+1 and randy == j+1:
                    grid[i] += "X "
                elif randx == i+1:
                    grid[i] += "- "
                elif randy == j+1:
                    grid[i] += "| "
                else:
                    grid[i] += "# "
        topbar = " "
        for i in range(y):
            if i+1 >= 10:
                topbar += f"{i+1}"
            else:
                topbar += f"{i+1} "
        print("  "+topbar)
        for i in range(x):
            if i+1 <= 10:
                print(f"{i}  {grid[i]}")
            else:
                print(f"{i} {grid[i]}")

 
 

        input("\n\npress enter to continue...\n\n")
            

    



if __name__ == "__main__":
    main()

