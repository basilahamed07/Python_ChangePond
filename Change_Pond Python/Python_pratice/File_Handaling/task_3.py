import os
import filecmp


def del_file(file_name):
    os.remove(file_name)
    print("File removed....")

def file_namess():
    return input("Enter the file_name: ")



def main():
    file_name = file_namess()
    del_file(file_name)
if __name__ == "__main__":
    main()