#he file_name can be a combined file path/name, you will need to add the file extension to the file_name when opening a file.

#This function should use file_name included and file_content to write a .txt file.

#Write a append_to_file function that takes in the same parameters and appends to the .txt file.

#Write a read_file function that takes in a file name and returns the content of the .txt file.
def write_file(file_name, file_content):
    with open(f"{file_name}.txt",mode ='w',encoding='utf-8') as log_file:
        log_file.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt",mode='a',encoding='utf-8') as append_file:
        append_file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt", 'r',encoding='utf-8') as f:
      return f.read()
 