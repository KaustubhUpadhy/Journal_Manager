import os  # will be used for getting a list of text files in the directory
import datetime  # will be used for adding the last update line in the files


# A function that asks the user if they want to create a file and if yes then prompt them for a file name and create it.

def file_creation():
    name = input("Enter File name: ")
    with open(name, "x") as f:
        print(f.name, "created!!")

# Function that would ask for opening a file and will bring a list of text files for the user to select from and read out its content

def file_reader():
    # print(os.listdir()) gives a list of all files and directories
    lst = [
        fin for fin in os.listdir() if os.path.isfile(fin)
    ]  # .isfile() returns true if the given path or argument is a regular file
    print(lst)
    file_name = input("Select and type your file name from the given list: ")
    try:
        with open(file_name, "r") as f:
            contents = (
            f.read()
        )  
        print(contents)
    except FileNotFoundError as error:
        print(error)
        print("Sorry. This File does not exist. Please create one and come back later.")
        q = input("Do you want to create a new one?:")
        if q.upper()=="YES":
            file_creation()
        else:
            pass
    finally:
         print("Operation Executed Successfully!!")

# Function that would write into the file which the user chooses

def write_func():
    lst = [fin for fin in os.listdir() if os.path.isfile(fin)]
    print(lst)
    file_name = input("Select and type your file name from the given list: ")
    with open(file_name, "a") as f:
        inp_dec = input("Do you have a set number of lines that you want to add? (yes/no):")
        if inp_dec.upper()=="YES":
                num_lines = int(input("How many lines are you seeking to add:"))
                for i in range(0,num_lines):
                    content = input("Enter what you want to pass in to write:")
                    f.write("\n")
                    f.write(content)
        elif inp_dec.upper()=="NO":
                con = input("Do you wish to continue still?:")
                while con.upper()=="YES":
                    content = input("Enter what you want to pass in to write:")
                    f.write("\n")
                    f.write(content)
                    con = input("Do you wish to continue still?:")
        else:
                print("Wrong input!! Please try again.")
                inp_dec = input("Do you have a set number of lines that you want to add? (yes/no):")
        now = datetime.datetime.now()
        date_lst = ["\n\n","Updated on ", now.strftime(" %d/%m/%Y, %H:%M:%S")]
        f.writelines(date_lst)


def eraser():
    option = int(input("Do you want to delete a file or erase its contents?(Type 1 or 2 respectively):"))
    if option==1:
        lst = [fin for fin in os.listdir() if os.path.isfile(fin)]
        print(lst)
        file_name = input("Select and type your file name from the given list: ")
        try:
            if os.path.isfile(file_name):
                  print("Ok deleting the file.....")
            else:
                pass
        except FileNotFoundError:
            print("Incorrect File Name. Plase try again")
            eraser()    
        finally:
            os.remove(file_name)
            print("\n File Deleted Sucessfully!!")
    elif option==2:
        lst = [fin for fin in os.listdir() if os.path.isfile(fin)]
        print(lst)
        file_name = input("Select and type your file name from the given list: ")
        try:
           with open(file_name,"w")as f:
                pass 
        except FileNotFoundError:
            print("Incorrect File Name. Plase try again")
            eraser()
         
def Menu():
    print("What do you want to do?:")
    options = ["New Journal Entry","Read previous journal entry","Edit previous Journal entry", "Delete or Erase the contents of a file"]
    n = 0
    for i in options:
        n= n+1
        print(n,":",i)
    whatcon =input("Do you wish to perform an action?(yes/no):")
    if whatcon.upper()=="YES":
        opt = int(input("What's your choice?(Enter your number):"))
        if opt==1:
            file_creation()
            Menu()
        elif opt==2:
            file_reader()
            Menu()
        elif opt==3:
            write_func()
            Menu()
        else: 
            eraser()
            Menu()
    elif whatcon.upper()=="NO":
         print("Thankyou for using this. Hope you found it useful!!")
    else:
         print("Incorrect option!!")
         Menu()
  
Menu()
