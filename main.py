import time
import math
from colorama import Fore, Back, Style

# operations function

def op():
    print("+ => Sum")
    print("- => Subtract")
    print("* => Multiply")
    print("/ => Division")
    print("% => Remainder")
    print("^ => Pow")
    print("! => Root")

# calculator function

def calc():
    num1 = float(input(Fore.MAGENTA + "Enter Frist Number: "))
    op = str(input(Fore.CYAN + "Enter Operation: "))
    num2 = float(input(Fore.MAGENTA + "Enter Second Number: "))
    hfile = open("history.txt", "a")

    if op == "+":
        print(Fore.LIGHTGREEN_EX + str(num1) + " + " + str(num2) + " = " + Style.BRIGHT + str(num1 + num2))
        hfile.write(str(num1) + " + " + str(num2) + " = " + str(num1 + num2) + "\n")
        hfile.close()
    elif op == "-":
        print(Fore.LIGHTGREEN_EX + str(num1) + " - " + str(num2) + " = " + Style.BRIGHT + str(num1 - num2))
        hfile.write(str(num1) + " - " + str(num2) + " = " + str(num1 - num2) + "\n")
        hfile.close()
    elif op == "*" or op.lower == "x" or op == "×":
        print(Fore.LIGHTGREEN_EX + str(num1) + " × " + str(num2) + " = " + Style.BRIGHT + str(num1 * num2))
        hfile.write(str(num1) + " x " + str(num2) + " = " + str(num1 * num2) + "\n")
        hfile.close()
    elif op == "/" or op == "÷":
        print(Fore.LIGHTGREEN_EX + str(num1) + " ÷ " + str(num2) + " = " + Style.BRIGHT + str(num1 / num2))
        hfile.write(str(num1) + " ÷ " + str(num2) + " = " + str(num1 / num2) + "\n")
        hfile.close()
    elif op == "%":
        print(Fore.LIGHTGREEN_EX + str(num1) + " ÷ " + str(num2) + " = " + str(num1 / num2))
        print(Style.BRIGHT + "Remainder: " + str(num1 % num2))
        hfile.write(str(num1) + " % " + str(num2) + " = " + str(num1 % num2) + "\n")
        hfile.close()
    elif op == "^":
        print(Fore.GREEN + str(num1) + "^" + str(num2) + " = " + Style.BRIGHT + str(pow(num1, num2)))
        hfile.write(str(num1) + "^" + str(num2) + " = " + str(pow(num1, num2)) + "\n")
        hfile.close()
    elif op == "!":
        print(Fore.GREEN + "!" + str(num1) + " = " + Style.BRIGHT + str(math.sqrt(num1)))
        hfile.write("!" + str(num1) + " = " + str(math.sqrt(num1)) + "\n")
        hfile.close()
    else:
        print(Fore.RED + "Error!")

# history function

def history(cmd):
    if cmd == "show":
        rfile = open("history.txt", "r")
        print(rfile.read())
        rfile.close()
    elif cmd == "clear":
        wfile = open("history.txt", "w")
        wfile.write("")
        wfile.close()
        print(Back.RED + Fore.LIGHTWHITE_EX + Style.BRIGHT + "Cleared!")
        print(Style.RESET_ALL)

# loading

print("Loading...\n")

#* while for auto run

while True:
    time.sleep(1)

    # interface

    print(Fore.RESET + "0. Operations\n" + Fore.GREEN + "1. Calculator\n" + Fore.BLACK + "2. History\n" + Fore.RED + "3. Clear History")

    command = int(input(Back.LIGHTWHITE_EX + Fore.BLACK + "Choose: "))
    print(Back.RESET + Fore.RESET)

    if command == 0:
        op()
    elif command == 1:
        calc()
    elif command == 2:
        history("show")
    elif command == 3:
        history("clear")