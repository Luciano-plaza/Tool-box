import string
import random
import hashlib
import os
import socket
import threading

# Color settings

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

print(f"\n{colors.HEADER}                           Welcome to the {colors.OKCYAN}ToolBox{colors.ENDC} {colors.HEADER}by{colors.ENDC} {colors.OKCYAN}C4cker{colors.ENDC}{colors.HEADER}!{colors.ENDC}                        {colors.ENDC}")
print(f"\n{colors.HEADER}           Here you have a tool kit to start practicing basic pentesting knowledge.                        {colors.ENDC}")
print(f"\n{colors.OKGREEN}              Please follow the instructions and use this toolkit ethically.                        {colors.ENDC}")
print("                                                                                  ")
print("                                                                                  ")
print("                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            ")
print("                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            ")
print("                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀          ")
print("                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣴⣿⣿⣿⣿⣯⣤⣶⣶⣾⣿⣶⣶⣿⣿⣿⣿⣿⡿⠿⠟⠛⠉⠉⠀⠀⠀⠀      ")
print("                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠉⠁⠈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⠶⠶⠦⠄⠀⠀⠀⠀      ")
print("                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀       ")
print("                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣟⣡⣤⣾⣿⣿⣿⣿⣿⣿⢏⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⢿⣿⣿⣦⡀⠀⠀⠀⠀       ")
print("                ⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠈⠻⡄⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⠙⠻⣿⣆⠀⠀⠀      ")
print("                ⠀⠀⠀⠀⢰⣿⣿⣿⣿⡿⠛⠉⠉⠉⠛⠛⠛⠛⠋⠁⠀⠀⠀⠁⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠈⠙⢧⠀⠀       ")
print("                ⠀⠀⠀⠀⠀⠙⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠁⠀         ")
print("                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠙⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀       ")
print("                ⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀       ")
print("                ⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠈⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀      ")
print("                ⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⢋⣩⡿⠿⠿⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀       ")
print("                ⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣄⣀⡀⠀⠀⠀⠀⠀⠐⠉⠀⠀⠀⠀⠀⠀⠀⠀          ")
print("                ⠀⣾⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀          ")
print("                ⢰⣿⣿⣿⣿⣿⣿⣿⣿⡄⠙⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⣀⠀⠀⠀⠠⣄⣀⣀⡉⢻⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀        ")
print("                ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀      ")
print("                ⠀⢻⡟⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠋⠉⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀    ")
print("                ⠀⠀⠃⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠈⠉⡿⢿⣿⣿⣿⣷⡄⠀     ")
print("                ⠀⠀⠀⠀⢸⣿⣿⡟⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⣿⣿⣿⣿⣿⣧⣀⣀⡄⠀⢠⠀⠀⡀⠁⠘⣿⡿⣿⣿⣷⠀     ")
print("                ⠀⠀⠀⠀⢸⣿⡿⠁⠀⠀⠀⠙⠻⠿⣟⠻⢿⣿⣿⣿⣷⣦⡀⠀⠈⠻⢿⣿⣿⣭⣉⡉⠀⠀⠐⠀⠀⠀⠠⠀⠚⠀⠸⣿⣿⡄      ")
print("                ⠀⠀⠀⠀⣸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣦⡀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁        ")
print("                ⠀⠀⠀⠠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⠀          ")
print("                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠟⠀⠀           ")
print("                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀           ")
print("                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀           ")
print("                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀           ")

##############################

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

#####       Network Analyzer        #####

#########################################



#########################################

########       Port Scanner      ########

#########################################


def host_sanitization (host):

    octet = 0
    
    while octet != 4:
    
        try:

            # Verification variables
        
            count_dots = host.count(".")
            check_host = host.split(".")
            check_len = len(check_host)
            
            # Error type alarm

            int(check_host[octet])

            # Checking octet per octet

            if count_dots == 3 and check_len == 4 and int(check_host[octet]) in range(225):

                    octet = octet + 1

            else:

                octet = 0

                host = input(colors.FAIL + "\nInvalid input" + colors.ENDC + ". Please enter a valid IP address: ")
            
        except ValueError:

            octet = 0

            host = input(colors.FAIL + "\nInvalid input" + colors.ENDC + ". Please enter a valid IP address: ")

    return host

###############################

def port_sanitization(port):

    port_validate = False

    while not port_validate:

        try:
            
            port_range = '-' in port
            port_checker = port.split('-')

            # Checking if a port range exists

            if port_range:

                start_port = port_checker[0]
                end_port = port_checker[1]
                
                if len(port_checker) == 2 and int(start_port) in range(65535) and int(end_port) in range(65535) and int(start_port) < int(end_port):

                    port_validate = True
            
                else:

                    port = input(colors.FAIL + "\nInvalid input" + colors.ENDC + ". Please enter a valid port or port range (default: 0-65535): ")

            # Default value

            elif len(port) == 0:

                port_validate = True

                port = '0-65535'

            # Unique port

            elif int(port) in range(65535):

                port_validate = True

            else:

                port = input(colors.FAIL + "\nInvalid input" + colors.ENDC + ". Please enter a valid port or port range (default: 0-65535): ")

        # Error catcher

        except ValueError:

            port = input(colors.FAIL + "\nInvalid input" + colors.ENDC + ". Please enter a valid port or port range (default: 0-65535): ")

    return port

##############################

def open_ports(host, port):

    sock = socket.socket()
    
    try:
        
        sock.settimeout(0.2)
        sock.connect((host, port))
        
        print(f"{colors.OKGREEN}[+]{colors.ENDC} Port {colors.OKGREEN}{port}{colors.ENDC} is open")

        sock.close()

    except:

        pass


##############################

def port_scanner(host, port):

    port_range = port.split('-')

    if len(port_range) == 2:

        start_port = int(port_range[0])
        end_port = int(port_range[1])

        try:

            for port in range(start_port, end_port + 1):

                thread = threading.Thread(target=open_ports, args=(host, port))

                thread.start()

        except KeyboardInterrupt:
            print("\n Exiting Program!\n")

        except socket.gaierror:
            print("\n Hostname Could Not Be Resolved!")

        except socket.error:
            print(" Server not responding!")

    
    else:

        # This contain a bug(bug fix is needed)

        thread = threading.Thread(target=open_ports, args=(host, port))

        thread.start()



#########################################

########    Password Cracker     ########

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

##############################

# Header messages and calling functions

if input_tool_mode == '1':

    # Banner

    print(f"\n{colors.HEADER}                                   Password Generator!                        {colors.ENDC}")
    
    print(f"\n{colors.OKCYAN}               This tool will help you create a strong and secure password.                        {colors.ENDC}\n")

    # Requesting data and calling functions

    long_passwd = input("Enter the desired password length: ")

    password_generator(long_passwd)


elif input_tool_mode == '2':

    # Banner

    print(f"\n{colors.HEADER}                                   Soon                        {colors.ENDC}")



elif input_tool_mode == '3':

    # Banner

    print(f"\n{colors.HEADER}                                   Port Scanner                        {colors.ENDC}")

    print(f"\n{colors.HEADER}               This toll will help you to make a basic port scanning                        {colors.ENDC}\n")

    # Requesting data and calling functions

    host = input("Enter the target host: ")

    port = input("Enter a valid port or port range (default: 0-65535): ")

    port_scanner(host_sanitization(host), port_sanitization(port))



elif input_tool_mode == '4':

    # Banner

    print(f"\n{colors.HEADER}                                   Password Cracker!                        {colors.ENDC}")

    print(f"\n{colors.OKCYAN}           This tool will help you crack passwords using a dictionary attack.                        {colors.ENDC}\n")

    # Requesting data and calling functions

    hash_file = input(f"Enter the {colors.WARNING}SHA-256 hash{colors.ENDC} of the password you want to crack: ")

    dictionary_file = input(F"Enter the {colors.WARNING}path{colors.ENDC} to the dictionary file: ")

    password_cracking(hash_file, dictionary_file)

