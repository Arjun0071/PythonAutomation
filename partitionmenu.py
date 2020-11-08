import os
import getpass

os.system("tput setaf 3")
print("\t\t\t Welcome to the Partition Menu")
os.system("tput setaf 7")
print("\t\t\t-------------------------")

passwd = getpass.getpass("Enter your Password : ")

if passwd != "bondone1":
    print("password incorrect...")
    exit()

while True:
    print("""
      \n
 Enter-1.Create Partitions to your Drive
 Enter-2.Format drive
 Enter-3.Mount Drive 
 Enter-4.Unmout Drive	
 Enter-5.Exit
      """)
    ch = input("    Enter Your Choice :")
    print(ch)
    if int(ch) == 1:
        partname = input("Enter your Partition path : ")
        print(partname)
        os.system(" fdisk {}".format(partname)
    elif int(ch) == 2:

        drive = input("enter your drive path: ")
        print(drive)
        os.system("mkfs.ext4{}".format(drive))
        os.system("udevadmin settle")
 

    elif int(ch) == 3:

        path = input("Enter the partition path:")
        print(path)
        directory = input("Enter the direc. to be mounted on :")
        print(directory)
        os.system("mount {} {}".format(path, directory))

    elif int(ch) == 4:
        directory1 = input("Enter the directory path you want to unmount")
        print(directory1)
        os.system("umount {}".format(directory1))
	
    elif int(ch) == 5:
        exit()

    else        :
        print(" No such option available ")
        exit()

    




 
