import os;
import sys;
import time;
import msvcrt;
from pick import Picker;

CurPath = os.getcwd()

def showMenu(options, title, indicator="=>", default_index=0):
    picker = Picker(
        options,
        title,
        indicator=indicator,
        default_index=default_index
    )

    def go_back(picker):
        return None, -1

    picker.register_custom_handler(ord("q"), go_back)

    return picker.start()

def timer(seconds):
    for remaining in range(seconds, -1, -1):
        mins, secs = divmod(remaining, 60)
        timer_format = f"{mins:02d}:{secs:02d}"
        print(f"Redirecting in {timer_format}", end="\r")
        time.sleep(1)

def press_any_key():
    if os.name == 'nt':
        msvcrt.getch()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def folderSubMenu():
    while True:
        title = f"""
        {"="*75}\n
        \t\t\t   File Management System
        \t Current directory:  {CurPath}\n
        \t\t   Press 'q' to return to previous menu\n
        {"="*75}
                """

        options = ["Create a new folder", "Delete a folder", "Navigate to other directory"]
        option, index = showMenu(options, title, indicator="=>", default_index=0)

        if index == -1:
            return

        print(f"You selected: '{option}'")

        match (option):
            case "Create a new folder":
                foldername = input("Folder name: ")
                if not os.path.exists(foldername):
                    os.mkdir(foldername);
                    print(f"Successfully created a new folder: {foldername}!");
                    timer(3);
                    clear_screen();
                else:
                    print("The folder is already exists.");
                    press_any_key();
                    clear_screen();
                continue;
            
            case "Delete a folder":
                while True:
                    foldername = input("Folder name: ")
                    if os.path.exists(foldername):
                        print(f"Are you sure to delete this folder? ('{foldername}')")
                        ans = input("Y/N: ")
                        if ans.lower() == "y":
                            os.rmdir(foldername);
                            print(f"Successfully deleted the folder: {foldername}!")
                            timer(3)
                            clear_screen()
                            break;
                        elif ans.lower() == "n":
                            clear_screen()
                            break;
                    else:
                        print("The folder does not exist.")
                        press_any_key()
                        clear_screen()
                        break;
            
            case "Navigate to other directory":
                while True:
                    
                    break;

def fileSubMenu():
    while True:
        title = f"""
        {"="*75}\n
        \t\t\t   File Management System
        \t Current directory:  {CurPath}\n
        \t\t   Press 'q' to return to previous menu\n
        {"="*75}
                """
        options = ["Create a new file", "Delete a file", "Show all files", "Show all files (hidden files included)"]
        option, index = showMenu(options, title, indicator="=>", default_index=0)

        if index == -1:
            return

        print(f"You selected: '{option}'")

        match (option):
            case "Create a new file":
                filename = input("File name: ");
                if not os.path.exists(filename):
                    with open(filename, "w") as file:
                        file.write("");
                    print(f"Successfully created a new file: {filename}!")
                    timer(3)
                    clear_screen()
                else:
                    print("The file already exists.");
                    press_any_key()
                    clear_screen()
                continue;
            
            case "Delete a file":
                while True:
                    filename = input("File name: ");
                    if os.path.exists(filename):
                        print(f"Are you sure to delete this file? ('{filename}')");
                        ans = input("Y/N: ")
                        if ans.lower() == "y":
                            os.remove(filename);
                            print(f"Successfully deleted the file: {filename}!")
                            timer(3)
                            clear_screen()
                            break;
                        elif ans.lower() == "n":
                            clear_screen()
                            break;
                    else:
                        print("The file does not exist.")
                        press_any_key()
                        clear_screen()
                        break;
            
            case "Show all files":
                while True:
                    print(f"Every files inside this directory: '{CurPath}'\n");
                    for k, v in enumerate(os.listdir(CurPath)):
                        if os.path.isfile(os.path.join(CurPath, v)):
                            print(f"{k+1}. {v} : {os.path.getsize(v)} Bytes");
                    print("\nPress any key to return.")
                    press_any_key();
                    clear_screen()
                    break;

            case "Show all files (hidden files included)":
                while True:
                    print(f"Every files inside this directory: '{CurPath}'\n");
                    for k, v in enumerate(os.listdir(CurPath)):
                        print(f"{k+1}. {v} : {os.path.getsize(v)} Bytes");
                    print("\nPress any key to return.")
                    press_any_key();
                    clear_screen()
                    break;

def mainMenu():
    while True:
        title = f"""
        {"="*75}\n
        \t\t\t   File Management System
        \t Current directory:  {CurPath}\n
        \t\t   Press 'q' to return to previous menu\n
        {"="*75}
                """
        options = ["Navigation & Directory Control", "File & Directory Management", "File Inspection & Reading", "Exit the program"]
        option, index = showMenu(options, title, indicator="=>", default_index=0);

        if index == -1:
            continue

        match (option):
            case "Navigation & Directory Control":
                folderSubMenu()

            case "File & Directory Management":
                fileSubMenu()

            case "File Inspection & Reading":
                        print("Currently unavailable")
                        print("Press any key to return")
                        press_any_key()
                        clear_screen()
                        continue;

            case "Exit the program":
                sys.exit("Hope to see you again, Goodbye!")

mainMenu()        
