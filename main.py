import os
#Code:
def main():
  running = True
  while running:
    print("===== File Manager =====",end="\n")
    print("1 - List files")
    print("2 - Create file")
    print("3 - Delete file")
    print("4 - Exit")
    answer =input(">>>")
    if answer == "1"or answer == "List files":
      directory = input("Directory: ")
      try:
        print(os.listdir(directory))
      except FileNotFoundError:
        print("Directory not found.")
    elif answer == "2"or answer == "Create file":
      directory = input("Directory: ")
      file_name = input("Filename: ")
      if not os.path.exists(directory):
        print("Directory doesn't exist!")
      else:
        with open(os.path.join(directory, file_name), "w"):
          print("File created !")
    elif answer == "3"or answer == "Delete file":
      directory = input("Directory: ")
      file_name = input("Filename: ")
      try:
        os.remove(os.path.join(directory, file_name))
        print("File deleted !")
      except FileNotFoundError:
        print("File not found.")
    elif answer == "4"or answer == "Exit":
      print("Thanks for chosing File organizer by Stickamir")
      print("Exiting ...")
      break
    else:
      print("Command not existing , please type a existing command")


if __name__ == "__main__":
  main()