import sys
import argparse
import datetime
import os

def setup():
    parser = argparse.ArgumentParser(description="File Manipulation CLI")
    ####++++++++++ commands as arguments
    parser.add_argument("--ls", help="List directory contents at [path]")
    parser.add_argument("--cd", help="Change the working directory to [path]")
    parser.add_argument("--mkdir", help="Create a new directory at [path]")
    parser.add_argument("--rmdir", help="Remove the directory at [path] if its empty")
    parser.add_argument("--rm", help="Remove the file specified by [file]")
    parser.add_argument("--rm-r", help="Remove the directory at [directory]")
    parser.add_argument("--cp",nargs=2, help="Copy a file or directory from source to destination")
    parser.add_argument("--mv",nargs=2,  help="move file from [source] to [destination]")
    parser.add_argument("--find",nargs=2, help="Search for files or directories")
    parser.add_argument("--cat",nargs=2, help="Output the contents of the file")
    parser.add_argument("--show-logs",action="store_true", help="shows all logs with realtime")
    return parser

############  write a file and add cmd history with realtimes and output if output  ##############

def write_log(cmd, outcome):
    with open("commands.log" , "a") as file:
     time_now = datetime.datetime.now()
     time_now = time_now.strftime("%d/%m/%Y--%I:%M-%p")
     text =f"{cmd}: {time_now} | outcome : {outcome} \n"
     file.write(text)
     
#######////////////////////++++++++  commands functions  ++++++++\\\\\\\\\\\\\\\\\\\\############ 
########## --show-logs      
def show_log(file_name = "commands.log"):
    try :
        with open(file_name, "r") as file1:
           data = file1.read()
        print(data)
    except FileNotFoundError:
        print("Commands log File NOT Found ! ! !   (⩺_⩹) ")
        
######### --ls 
def list(path):
    file_name =[]
    try:
      for p,dirs ,files in os.walk(path):
         for f in files:
            f_path = os.path.join(path ,f)
            file_name.append(f_path)
      if not file_name:
          print("No Files Found in this directory !!!  (⩺_⩹) ")
      for file in file_name :
         print(file) 
      return "Listed Successfully" 
    except Exception as e:
       print(f"Error ! ! ! : {e}")
       return f"Error: {e}"   
######## --cd
def chnge_dir_path(path):
    try :
        os.chdir(path)
        print(f"Changed working directory path to: {path} succesfully !")
        return "Changed Directory Successfully"
    except FileNotFoundError:
        print(f"'{path}' Directory Not Found ! !!!!  （＞д＜） ")
        return "Directory Not Found"
    except NotADirectoryError:
        print(f"'{path}' is Not a Directory !   ☜(`o´)  ")
        return "That Was Not a Directory"    
        
############# --mkdir        
def make_dir(path): 
    try :
        os.mkdir(path)
        print(f"Directory made in'{path}' Succesfully ")
        return "Directory Created"
    except FileExistsError:
        print(f"Directory '{path}' already exists !!!ʅ(°ヮ°)ʃ")
        return "Directory Already Exists" 
    except PermissionError:
            print(f"Permission denied !!!!  Cannot Create Directory '{path}'  !!ʅ(°ヮ°)ʃ .")  
            return "Permission Denied" 
               
############# --rmdir        
def remove_empty_dir(path):
    try:
        os.rmdir(path)
        print(f"The Empty '{path}' Directory Removed successfully !!! ")
        return "Directory Removed"
    except FileNotFoundError:
        print(f"Directory '{path}' Not Found !  !!ʅ(°ヮ°)ʃ")
        return "Directory Not Found"
    except OSError:
        print(f"'{path}' is Not empty or Cant Be Removed ! !!ʅ(°ヮ°)ʃ")
        return "Directory Not Empty or Can't Be Removed"
        
############# --rm   [file]
def remove_file(path):
    try:
        os.remove(path)
        print(f"File '{path}' Removed Succesfully")
        return "File Removed"
    except FileNotFoundError:
        print(f"File '{path}' not found !!!  ʅ(°ヮ°)ʃ ")
        return "File Not Found"
        
############  --rm-r    
def remove_dir(path):
    try:
        for p , dirs, files in os.walk(path, topdown=False):
            for file in files:
                os.remove(os.path.join(p, file))
            for dir in dirs:
                os.rmdir(os.path.join(p, dir))
        os.rmdir(path)
        print(f"Directory '{path}' and its contents Removed Successfully!")
        return "Directory and Contents Removed"
    except FileNotFoundError:
        print(f"Directory '{path}' Not Found ! ! !  ʅ(°ヮ°)ʃ")
        return "Directory Not Found"
    except Exception as e:
        print(f"Error!!!!  ʅ(°ヮ°)ʃ: {e}")
        return f"Error: {e}"
        
#############   --cp  both file and dir  
####......... for directory ........########     
def copy_dir(source , destination):
    try:
        os.mkdir(destination) 
        for item in os.listdir(source):
            s = os.path.join(source, item)
            d = os.path.join(destination, item)
            if os.path.isdir(s):
                #... recursive function ...#
                copy_dir(s, d) 
            else:
                copy_dir(s, d)  
        print(f"Copied directory '{source}' to '{destination}' Successfully !")
        return "Directory Copied"
    except FileExistsError:
        print(f"directory in '{destination}' Already Exists ! !  ʅ(°ヮ°)ʃ ")
        return "Destination Directory Exists" 
    except FileNotFoundError:
        print(f"Source directory '{source}' Not Found !   ʅ(°ヮ°)ʃ")
        return "Source Directory Not Found"
    except PermissionError:
        print(f"Permission Denied for copying '{source}' to '{destination}' !   ʅ(°ヮ°)ʃ !")
        return "Permission Denied"
    except Exception as e:
        print(f"Error !!!!! : {e}")
        return f"Error: {e}"
        
########........ for file .....########        
def copy_file(source, destination):
    try:
        with open(source, 'rb') as src, open(destination, 'wb') as dest:
            dest.write(src.read())
        print(f"File '{source}' copied to '{destination}' Successfully ! !")
        return "File Copied"
    except Exception as e:
        print(f"Error copying file !   ʅ(°ヮ°)ʃ ! : {e}")
        return f"Error: {e}"
#####<<<<< main function for copy file AND dir >>>>>########         
def copy(source, destination):
    if os.path.isdir(source):
        copy_dir(source, destination)
    else:
        copy_file(source, destination)
            
############  --mv       
def move_file(source ,destination):
    try:
         os.replace(source, destination)  
         print(f"Moved '{source}' to '{destination}' successfully ! ! ! ")
         return "Moved Successfully"
    except FileNotFoundError:
        print(f"'{source}' source Not Found ! !  !  ʅ(°ヮ°)ʃ ")
        return "Source Not Found"
    except IsADirectoryError:
        print(f"'{source}' Is a Directory ! !  ʅ(°ヮ°)ʃ  ")
        return "Source Is a Directory"
    except Exception as e:
        print(f"Error !!!ʅ(°ヮ°)ʃ: {e}")
        return f"Error: {e}"

############ --find
def find(path,pattern):
    try:
        for p, dirs, files in os.walk(path):
            for file in files:
                if pattern in file:
                    print(os.path.join(p, file))
                    found = True
                    return "File(s) Found" if found else "No Matching Files Found"
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"

############# --cat 
def output_content(file):
    try:
        with open(file, 'r') as f:
            content = f.read()
            print(content)
            return "File Content Displayed"
    except FileNotFoundError:
        print(f"File '{file}' Not Found ! ! !   ! !  ʅ(°ヮ°)ʃ ")
        return "File Not Found"
    except Exception as e:
        print(f"Error!!!!!: {e}")
        return f"Error: {e}"
    
parser = setup()
args = parser.parse_args()
### store user commands 
cmd = " ".join(sys.argv)
outcome = None
#print(args)
#write_log(cmd)
##############++++++++++++           using the functions            ++++++++++++++++++#############

if args.ls :
     outcome =list(args.ls)
elif args.cd:
     outcome =chnge_dir_path(args.cd)
elif args.mkdir :
     outcome =make_dir(args.mkdir)
elif args.rmdir:
     outcome =remove_dir(args.rmdir)
elif args.rm :
     outcome=remove_file(args.rm)
elif args.rm_r :
     outcome=remove_dir(args.rm_r)
elif args.cp :
     outcome=copy(args.cp[0],args.cp[1])
elif args.mv :
     outcome=move_file(args.mv[0],args.mv[1])
elif args.find :
     outcome=find(args.find[0],args.find[1])
elif args.cat :
     outcome=output_content(args.cat)
elif args.show_logs :
     show_log()
     outcome = "displayed command logs"
else :
    print("No Command Provided, Enter a command !!!!ʅ(°ヮ°)ʃ ")
    outcome = "No Command Provided"   

#########  outcome status  #########    
if outcome is not None :
    write_log(cmd , outcome)

       


         
