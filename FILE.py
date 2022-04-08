#with open(<file name>,<access code>)as <file pointer>:
from os import system
"""import os functions
    os.remove(<filename>)
    os.rename(<old filename>,<new filename>)
    os.startfile(<directory name>)
    
    word=line.split(':')
    <filename>.tell()    "for telling "
"""
def writeit():
     f=open(input("Enter the file name: ")+'.txt','w')
     f.write(input("Enter the string for writing: "))
     f.close()     
     input("\npress any key to continue: ")     
def readit():
     f=open(input("Enter the file name: ")+'.txt','r')
     print("File Content:\n",f.read())
     f.close()     
     input("\npress any key to continue: ")     
def appendit():
     f=open(input("Enter the file name: ")+'.txt','a')
     ch='n'
     while ch not in "Yy":
          u=input("want to change the line(y/n): ")
          if u in 'yY':
               f.write("\n")
          f.write(input("Enter the string for appending: "))               
          ch=input("Want to exit(y/n): ")
     f.close()
     input("\npress any key to continue: ")
while 1:
     system("cls")
     k=int(input("\n\tMenu\n\t1-READ\n\t2-WRITE\n\t3-APPEND\n\t4-EXIT\n\nEnter your choice: "))
     system("cls")
     if k==1:
          readit()
     elif k==2:
          writeit()     
     elif k==3:
          appendit()     
     else:
          exit()               
