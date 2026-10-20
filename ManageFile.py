import os;
import time;
from pick import pick;

CurPath = os.getcwd()

def timer(seconds):
    for remaining in range(seconds, -1, -1):
        mins, secs = divmod(remaining, 60)
        timer_format = f"{mins:02d}:{secs:02d}"
        print(f"Redirecting in {timer_format}", end="\r")
        time.sleep(1)

def press_any_key():
    if os.name == 'nt':
        import msvcrt
        msvcrt.getch()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    title = f"""
            {"="*75}\n
            \t\t\t  File Management System
            \tCurrent directory:  {CurPath}\n
            {"="*75}
                    """
    opts = ["Navigation & Directory Control", "File & Directory Management", "File Inspection & Reading"]
    opt, ind = pick(opts, title, indicator="=>", default_index=0);

    match (opt):
        case "File & Directory Management":
            while True:
                title = f"""
            {"="*75}\n
                \t\t  File Management System
                Current directory:  {CurPath}\n
            {"="*75}
                        """
                options = ["Create a new file", "Delete a file", "Show all files"]
                option, index = pick(options, title, indicator="=>", default_index=0)
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
                    
                    case "Delete file":
                        while True:
                            filename = input("File name: ");
                            if os.path.exists(filename):
                                print(f"Are you sure to delete this file? ('{filename}')");
                                ans = input("Y/N: ")
                                if ans.lower() == "y":
                                    os.remove(filename);
                                    print(f"Successfully deleted the file: {filename}!")
                                elif ans.lower() == "n":
                                    continue;
                                else:
                                    print("Invalid, please type in the correct format.")
                                    continue;
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
                            print("\nPress any button to go back.")
                            press_any_key();
                            clear_screen()
                            break;
                

            
        
