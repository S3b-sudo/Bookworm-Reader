import os
import requests
import shutil

print("Bookworm Installer")
print("=========================")

if os.name == "posix":
    pass
else:
    print("[ERROR] You are running Windows or another opperating system which may not be supported")
    print("=========Options=========")
    print("(1) Run Anyway")                                                                             
    print("(Return) Quit")
    
    while True:
        choice = input("Choose a Nomber: ")

        if choice == "1":
            pass
        else:
            quit()

input("Press 'Return' to begin: ")

print("Creating virtual python environment...")
os.system("python -m venv BookW")
print("==================")
print("Installing dependencies...")
os.system("source BookW/bin/activate && pip install -r requirements.txt")
print("==================")
print("Making run.sh executable...")
os.system("chmod +x run.sh")
print("==================")
print("Making Folders...")
os.system("mkdir voices")    
print("==================")            
print("Done")
quit()
