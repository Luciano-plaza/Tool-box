import string
import random
import hashlib
import os
import socket

class colors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        
        ENDC = '\033[0m' #Close the color, always use this at the end of the colored text to reset the color.

# Welcome message and tool selection

print(f"\n{colors.HEADER}                               Welcome to the {colors.OKCYAN}ToolBox{colors.ENDC} {colors.HEADER}by{colors.ENDC} {colors.OKCYAN}C4cker{colors.ENDC}{colors.HEADER}!{colors.ENDC}                        {colors.ENDC}")
print(f"\n{colors.HEADER}               Here you have a tool kit to start practicing basic pentesting knowledge.                        {colors.ENDC}")
print(f"\n{colors.OKGREEN}                  Please follow the instructions and use this toolkit ethically.                        {colors.ENDC}")
print("                                                                                      ")
print("                                                                                      ")
print("                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            ")
print("                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            ")
print("                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀          ")
print("                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣴⣿⣿⣿⣿⣯⣤⣶⣶⣾⣿⣶⣶⣿⣿⣿⣿⣿⡿⠿⠟⠛⠉⠉⠀⠀⠀⠀      ")
print("                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠉⠁⠈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⠶⠶⠦⠄⠀⠀⠀⠀      ")
print("                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀       ")
print("                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣟⣡⣤⣾⣿⣿⣿⣿⣿⣿⢏⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⢿⣿⣿⣦⡀⠀⠀⠀⠀       ")
print("                    ⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠈⠻⡄⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⠙⠻⣿⣆⠀⠀⠀      ")
print("                    ⠀⠀⠀⠀⢰⣿⣿⣿⣿⡿⠛⠉⠉⠉⠛⠛⠛⠛⠋⠁⠀⠀⠀⠁⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠈⠙⢧⠀⠀       ")
print("                    ⠀⠀⠀⠀⠀⠙⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠁⠀         ")
print("                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠙⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀       ")
print("                    ⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀       ")
print("                    ⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠈⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀      ")
print("                    ⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⢋⣩⡿⠿⠿⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀       ")
print("                    ⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣄⣀⡀⠀⠀⠀⠀⠀⠐⠉⠀⠀⠀⠀⠀⠀⠀⠀          ")
print("                    ⠀⣾⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀          ")
print("                    ⢰⣿⣿⣿⣿⣿⣿⣿⣿⡄⠙⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⣀⠀⠀⠀⠠⣄⣀⣀⡉⢻⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀        ")
print("                    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀      ")
print("                    ⠀⢻⡟⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠋⠉⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀    ")
print("                    ⠀⠀⠃⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠈⠉⡿⢿⣿⣿⣿⣷⡄⠀     ")
print("                    ⠀⠀⠀⠀⢸⣿⣿⡟⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⣿⣿⣿⣿⣿⣧⣀⣀⡄⠀⢠⠀⠀⡀⠁⠘⣿⡿⣿⣿⣷⠀     ")
print("                    ⠀⠀⠀⠀⢸⣿⡿⠁⠀⠀⠀⠙⠻⠿⣟⠻⢿⣿⣿⣿⣷⣦⡀⠀⠈⠻⢿⣿⣿⣭⣉⡉⠀⠀⠐⠀⠀⠀⠠⠀⠚⠀⠸⣿⣿⡄      ")
print("                    ⠀⠀⠀⠀⣸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣦⡀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁        ")
print("                    ⠀⠀⠀⠠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⠀          ")
print("                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠟⠀⠀           ")
print("                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀           ")
print("                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀           ")
print("                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀           ")


print("\nWhich tools do you want to use?\n")
print(f"    {colors.FAIL}1){colors.ENDC} Password Generator")
print(f"    {colors.FAIL}2){colors.ENDC} Network Analyzer")
print(f"    {colors.FAIL}3){colors.ENDC} Port Scanner")
print(f"    {colors.FAIL}4){colors.ENDC} Simple Password Cracker")

# Variables of the functions

input_tool_mode = input("\nEnter the number corresponding to the tool you want to use: ")

# Check if the input mode is valid

while input_tool_mode not in ['1', '2', '3', '4']:
    
    input_tool_mode = input(colors.FAIL + "\nInvalid input." + colors.ENDC + " Please enter a valid number (1, 2, 3, or 4): ")
    

###############################

### Password Generator

###############################

def password_generator(long_passwd):
        
    # Validate the password length input and ensure it is a valid integer within the recommended range (12-128 characters).

    while type(long_passwd) != int or long_passwd < 12 or long_passwd > 128:

        # Check if the input is a valid integer.

        try:

            long_passwd = int(long_passwd)

        except ValueError:

            long_passwd = input(colors.FAIL + "\nInvalid input." + colors.ENDC + " Please enter a valid integer for the password length: ")

        # Check if the password length is within the recommended range.
        
        if type(long_passwd) == int:

            if long_passwd < 12:

                long_passwd = input( colors.WARNING + "\nWarning:" + colors.ENDC + " A password shorter than " + colors.WARNING + "12" + colors.ENDC + " characters may be less secure. Please enter a new length: ")
            
            elif long_passwd > 128:

                long_passwd = input( colors.WARNING + "\nWarning:" + colors.ENDC + " A password longer than " + colors.WARNING + "128" + colors.ENDC + " characters may be difficult to use. Please enter a new length: ")


    passwd = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=long_passwd))

    print(colors.BOLD + "\nYour password is: "+ colors.ENDC + colors.OKGREEN + passwd + colors.ENDC + "\n")


#########################################

### Network Analyzer

#########################################



#########################################

### Port Scanner

#########################################

def port_scanner(host, port):

    soc = socket.socket()

    try:

        soc.connect(host, port)

        soc.settimeout(0.3)

    except:
        
        return False

    else:

        return True

#########################################

### Password Cracker

#########################################

def password_cracking(hash_file, dictionary_file):

    file_exists = False

    # Check if the dictionary file exists.

    while not file_exists:

            wordlistfile = os.path.isfile(dictionary_file)

            if wordlistfile:

                file_exists = True

            else:

                dictionary_file = input(colors.FAIL + "\nFile not found. " + colors.ENDC + "Please enter a valid file path: ")

    # Open the dictionary file and read the passwords.

    with open(dictionary_file, 'r') as file:
        
        print("\nStarting password cracking...\n")

        dictionary = [line.strip() for line in file]

        # Iterate through the dictionary and hash each password to compare with the provided hash.

        for password in dictionary:
            
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            if hashed_password == hash_file:
                
                print(colors.OKGREEN + "[+] " + colors.ENDC + "Password found: " + colors.OKCYAN + password + colors.ENDC + "\n")
                
                break
                    
        else:
            
            print(f"{colors.FAIL}[-] {colors.ENDC}Password {colors.FAIL}not found{colors.ENDC} in the dictionary please try with a different dictionary file or check the hash you entered.\n")


# Header messages and calling functions

if input_tool_mode == '1':

    print(f"\n{colors.HEADER}                                   Password Generator!                        {colors.ENDC}")
    
    print(f"\n{colors.OKCYAN}               This tool will help you create a strong and secure password.                        {colors.ENDC}\n")

    long_passwd = input("Enter the desired password length: ")

    password_generator(long_passwd)

elif input_tool_mode == '2':

    print(f"\n{colors.HEADER}                                   Port Scanner                        {colors.ENDC}")

    print(f"\n{colors.HEADER}               This toll will help you to make a basic port scanning                        {colors.ENDC}")

    host = input("Enter the host: ")

    for port in range(1, 1024):

        if port_scanner(host, port):
            
            print(f"{colors.OKGREEN}[+] {host}:{port} is open      {colors.ENDC}")
        
        else:
            
            print(f"{colors.OKGREEN}[!] {host}:{port} is closed    {colors.ENDC}", end="\r")


elif input_tool_mode == '3':

    print(f"\n{colors.HEADER}                                   Soon                        {colors.ENDC}")

elif input_tool_mode == '4':

    print(f"\n{colors.HEADER}                                   Password Cracker!                        {colors.ENDC}")
    print(f"\n{colors.OKCYAN}           This tool will help you crack passwords using a dictionary attack.                        {colors.ENDC}\n")

    hash_file = input(f"Enter the {colors.WARNING}SHA-256 hash{colors.ENDC} of the password you want to crack: ")
    dictionary_file = input(F"Enter the {colors.WARNING}path{colors.ENDC} to the dictionary file: ")
    password_cracking(hash_file, dictionary_file)

