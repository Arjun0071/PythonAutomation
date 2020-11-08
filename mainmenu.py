import os
import getpass

os.system("tput setaf 3")
print("\t\t\t Welcome to the Main Menu")
os.system("tput setaf 7")
print("\t\t\t-------------------------")

passwd = getpass.getpass("Enter your Password : ")

if passwd != "bondone1":
    print("password incorrect...")
    exit()

while True:
    print("""
      \n
 Enter-1.LVM menu
 Enter-2.Configuring Web Server
 Enter-3.AWS Menu
 Enter-4.Docker Menu
 Enter-5.Partitions Menu
 Enter-6.Hadoop Menu
 Enter-7.Ansible Menu
 Enter-8.Exit
      """)
   
    ch = input("    Enter Your Choice :")
    print(ch)

    if int(ch) == 1:
        masip = input("Enter the Ip on which you want to access this menu on  :")
        print(masip)
        username = input("Enter your standard user name :")
        print(username)
        os.system(" ssh {ip} scp lvmmenu.py {name}@{ip}:".format(ip = masip, name = username))
        os.system("ssh {} chmod 777 /home/{} ".format(masip, username))
        os.system("ssh {}  python3 /home/{}/lvmmenu.py".format(masip, username )) 

    elif int(ch) == 2:
       	masip = input("Enter the Ip on which you want to access this menu on  :")
        print(masip)
        username = input("Enter your standard user name :")
        print(username)
        os.system(" ssh {ip} scp webservermenu.py {name}@{ip}:".format(ip = masip, name = username))
        os.system("ssh {} chmod 777 /home/{} ".format(masip, username))
        os.system("ssh {}  python3 /home/{}/webservermenu.py".format(masip, username )) 

    elif int(ch) == 3:
        masip = input("Enter the Ip on which you want to access this menu on  :")
        print(masip)
        username = input("Enter your standard user name :")
        print(username)
        os.system(" ssh {ip} scp awsmenu.py {name}@{ip}:".format(ip = masip, name = username))
        os.system("ssh {} chmod 777 /home/{} ".format(masip, username))
        os.system("ssh {}  python3 /home/{}/awsmenu.py".format(masip, username )) 

    elif int(ch) == 4:
        masip = input("Enter the Ip on which you want to access this menu on  :")
        print(masip)
        username = input("Enter your standard user name :")
        print(username)
        os.system(" ssh {ip} scp dockermenu.py {name}@{ip}:".format(ip = masip, name = username))
        os.system("ssh {} chmod 777 /home/{} ".format(masip, username))
        os.system("ssh {}  python3 /home/{}/dockermenu.py".format(masip, username )) 

    elif int(ch) == 5:
        masip = input("Enter the Ip on which you want to access this menu on  :")
        print(masip)
        username = input("Enter your standard user name :")
        print(username)
        os.system(" ssh {ip} scp partitionmenu.py {name}@{ip}:".format(ip = masip, name = username))
        os.system("ssh {} chmod 777 /home/{} ".format(masip, username))
        os.system("ssh {}  python3 /home/{}/partitionmenu.py".format(masip, username )) 

    elif int(ch) == 6:
        masip = input("Enter the Ip on which you want to access this menu on  :")
        print(masip)
        username = input("Enter your standard user name :")
        print(username)
        os.system(" ssh {ip} scp hadoopmenu.py {name}@{ip}:".format(ip = masip, name = username))
        os.system("ssh {} chmod 777 /home/{} ".format(masip, username))
        os.system("ssh {}  python3 /home/{}/hadoopmenu.py".format(masip, username )) 
            
    elif int(ch) == 7:
        masip = input("Enter the Ip on which you want to access this menu on  :")
        print(masip)
        username = input("Enter your standard user name :")
        print(username)
        os.system(" ssh {ip} scp ansiblemenu.py {name}@{ip}:".format(ip = masip, name = username))
        os.system("ssh {} chmod 777 /home/{} ".format(masip, username))
        os.system("ssh {}  python3 /home/{}/ansiblemenu.py".format(masip, username ))
    elif int(ch) == 8:
        exit()
    else        :
        print(" No such option available ")
        exit()

  

   
    




