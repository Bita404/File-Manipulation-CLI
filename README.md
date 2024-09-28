## :open_file_folder: File-Manipulation-CLI :open_file_folder:
This project contains some of the linux commands for File handling such as ls,cd,mkdir and more ,
we introduced the commands by using argparse library it can aslo shows the commands log with real time by using datetime library
each commands has its own function and errors are almost handled.
## requirments 
- python 3 
- os , sys , argparse ,datetime liberaries 
## Usage
File handling 
- "--ls" --> List directory contents at [path]
- "--cd"--> Change the working directory to [path]
- "--mkdir" --> Create a new directory at [path]
- "--rmdir" --> Remove the directory at [path] if its empty
- "--rm" --> Remove the file specified by [file]
- "--rm-r"--> Remove the directory at [directory]
- "--cp" --> Copy a file or directory from source to destination
- "--mv" --> move file from [source] to [destination]
- "--find" --> Search for files or directories
- "--cat" --> Output the contents of the file
- "--show-logs" --> shows all logs with realtime
## commands.Log
It contaians each logs and its arguments ,the time of execution and its outcome (if it was succesful or it has any error)

