import sys
import argparse
import datetime
import os

def setup():
    parser = argparse.ArgumentParser(description="File Manipulation CLI")
    
    parser.add_argument("--ls", help="List directory contents at [path]")
    parser.add_argument("--cd", action="store_true", help="Change the working directory to [path]")
    parser.add_argument("--mkdir", action="store_true", help="Create a new directory at [path]")
    parser.add_argument("--rmdir", action="store_true", help="Remove the directory at [path] if its empty")
    parser.add_argument("--rm", action="store_true", help="Remove the file specified by [file]")
    parser.add_argument("--rm-r", action="store_true", help="Remove the directory at [directory]")
    parser.add_argument("--cp",nargs=2, help="Copy a file or directory from source to destination")
    parser.add_argument("--mv",nargs=2,  help="move file from [source] to [destination]")
    parser.add_argument("--find",nargs=2, help="Search for files or directories")
    parser.add_argument("--cat",nargs=2, help="Output the contents of the file")
    parser.add_argument("--show-logs", help="shows all logs with realtime")
    return parser

############  write a file and add commands history with realtimes in it   ##############

def write_log(cmd):
    with open("commands.log" , "a") as file:
     time_now = datetime.datetime.now()
     time_now = time_now.strftime("%d/%m/%Y--%I:%M-%p")
     text = f"{cmd}: {time_now} \n"
     file.write(text)   
     
#######////////////////////++++++++  commands functions  ++++++++\\\\\\\\\\\\\\\\\\\\############ 
       
def show_log(file_name = "commands.log"):
    try :
        with open(file_name, "r") as file1:
           data = file1.read()
        print(data)
    except FileNotFoundError:
        print("No file for commands log !!!!! ")
    
def list(path):
    file_name =[]
    try:
      for p,dirs ,files in os.walk(path):
         for f in files:
            f_path = os.path.join(path ,f)
            file_name.append(f_path)
      if not file_name:
          print("No files found in this directory :( )")
      for file in file_name :
         print(file) 
         
    except Exception as e:
       print(f"Error: {e}")
           
    
def chnge_dir_path():
    pass
def make_dir():
    pass
def remove_empty_dir():
    pass
def remove_file():
    pass
def remove_dir():
    pass
def copy():
    pass
def move_file():
    pass
def find():
    pass
def output_content():
    pass




parser = setup()
args = parser.parse_args()
### store user commands 
cmd = " ".join(sys.argv)
#print(args)
write_log(cmd)
#show_log()

##############++++++++++++           using the functions            ++++++++++++++++++#############

if args.ls :
    list(args.ls)
elif args.cd:
    pass