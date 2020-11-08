import os
import getpass

os.system("tput setaf 3")
print("\t\t\t Welcome to the LVM menu")
os.system("tput setaf 7")
print("\t\t\t-------------------------")

passwd = getpass.getpass("Enter your Password : ")

if passwd != "bondone1":
    print("password incorrect...")
    exit()

while True:
    print("""
      \n
 Enter-1.List Storage
 Enter-2.Format drive
 Enter-3.Mount Drive 
 Enter-4.Create Physical Volume
 Enter-5.Create Volume Group
 Enter-6.Create Logical Volume
 Enter-7.Extend Logical Volume Size
 Enter-8.Reduce Logical Volume Size
 Enter-9.List Physical Volumes
 Enter-10.List Volume Groups
 Enter-11.List Logical Volumes
 Enter-12.Exit
      """)
    ch = input("    Enter Your Choice :")
    print(ch)

    if int(ch) == 1:
     os.system("fdisk -l")

    elif int(ch) == 2:
        drive = input(" Enter your drive path : ")
        print(drive)
        os.system("mkfs.ext4 {}".format(drive))
        os.system("udevadm settle")

    elif int(ch) == 3:
        path = input("Enter the partition path:")
        print(path)
        directory = input("Enter the direc. to be mounted on :")
        print(directory)
        os.system("mount {} {}".format(path, directory))

    elif int(ch) == 4:
        drive1 = input("Enter the patition path you want to convert :")
        print(drive1)
        os.system("pvcreate {}".format(drive1))

    elif int(ch) == 5:
        Name  = input("Enter a name for your VG :")
        print(Name)
        partitions = input("Enter the path of partition you want to add :")
        print(partitions)
        os.system("vgcreate {} {} ".format(Name, partitions))

    elif int(ch) == 6:
        size = input("Enter the size you want for your LV :")
        print(size)
        name = input("Enthe the name you want to give your LV :")
        print(name)
        VGname = input("Enter your VG name :")
        print(VGname)
        os.system("lvcreate --size +{} --name {} {}".format(size, name, VGname))
            
    elif int(ch) == 7:
        size1 = input("Enter the size you want to extend  :")
        print(size1)
        loclv = input("Enter the path of ypur Logical Volume :")
        print(loclv)
        os.system("lvextend --size +{} {}".format(size1, loclv))
        os.system("resize2fs {}".format(loclv))

    elif int(ch) == 8:
        direc1 = input("enter the directory path mounted on :")
        print(direc1)
        lvpath = input("Enter your Logical Volume Path")
        print(lvpath)
        reducesize = input("Enter the amount of size to reduce :")
        print(reducesize)
        os.system("umount {}".format(direc1))
        os.system("e2fsck -ff {}".format(lvpath))
        os.system("resize2fs {} {}".format(lvpath, reducesize))
        os.system("lvreduce --size -{} {}".format(reducesize, lvpath))
        os.system("resize2fs {}".format(lvpath))
        os.system("mount {} {}".format(lvpath, direc1))

    elif int(ch) == 9:
        partpath = input("Enter the path of physical volume :")
        print(partpath)
        os.system("pvdisplay {}".format(partpath))

    elif int(ch) == 10:
        partpath1 = input("Enter the name of your Volume Group :")
        print(partpath1)
        os.system("vgdisplay {}".format(partpath1))

    elif int(ch) == 11:
        partpath2 = input("Enter the name of your Volume Group :")
        print(partpath2) 
        partpath3 = input("Enther the name of your Logical Volume :")
        print(partpath3)
        os.system("lvdisplay {}/{} ".format(partpath2, partpath3))
    
    elif int(ch) == 12:
        exit()

    else        :
        print(" No such option available ")
        exit()

    



