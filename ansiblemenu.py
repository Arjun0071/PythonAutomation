import os
import getpass

os.system("tput setaf 3")
print("\t\t\t Welcome to the Ansible Menu")
os.system("tput setaf 7")
print("\t\t\t-------------------------")

passwd = getpass.getpass("Enter your Password : ")

if passwd != "bondone1":
    print("password incorrect...")
    exit()

while True:
    print("""
      \n
 Enter-1.Install Ansible
 Enter-2.Make an inventory
 Enter-3.Check the Connected Hosts
 Enter-4.Install httpd on all hosts
 Enter-5.Start httpd on all hosts
 Enter-6.Stop httpd on all hosts
 Enter-7.Exit
      """)
    ch = input("    Enter Your Choice :")
    print(ch)

    if int(ch) == 1:
        ip = input("Enter the IP on which you wish to install Ansible : ")
        print(ip)
        username = input("Enter your standard user name :")
        print(username)
        os.system("ssh {} pip3 install ansible".format(ip))
        os.system("ssh {} dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm".format(ip))
        os.system("ssh {} yum insatll sshpass".format(ip))
        os.system("ssh {} mkdir /etc/ansible".format(ip))
        os.system(" ssh {masip} scp ansibleconfig.py {name}@{ip}:".format(masip = ip, name = username))
        os.system("ssh {} chmod 777 /home/{} ".format(ip, username))
        os.system("ssh {}  python3 /home/{}/ansibleconfig.py".format(ip, username))

    elif int(ch) == 2:
        ip = input("Enter the IP on which you wish to add  Ansible inventory : ")
        print(ip)
        username = input("Enter your standard user name :")
        print(username)
        os.system(" ssh {masip} scp ansibleinventory.py {name}@{ip}:".format(masip = ip, name = username))
        os.system("ssh {} chmod 777 /home/{} ".format(ip, username))
        os.system("ssh {}  python3 /home/{}/ansibleinventory.py".format(ip, username))
        print("Your Inventory has been successfully made and also updated in the Ansible Config. file .Enjoy!!!!!! ")

    elif int(ch) == 3:
        ip = input("Enter the IP of your Controller node : ")
        print(ip)
        os.system(" ssh {} ansible all --list-hosts ".format(ip))

    elif int(ch) == 4:
        ip = input("Enter the IP of your Controller node : ")
        print(ip)
        os.system("ssh {} ""ansible all -m package -a ""name=httpd state=present".format(ip))

    elif int(ch) == 5:
        ip = input("Enter the IP of your Controller node : ")
        print(ip)
        os.system("ssh {} ""ansible all -m service -a ""name=httpd state=started".format(ip))

    elif int(ch) == 6:
        ip = input("Enter the IP of your Controller node : ")
        print(ip)
        os.system("ssh {} ""ansible all -m service -a ""name=httpd state=stopped".format(ip))
            
    elif int(ch) == 7:
        exit()

    else        :
        print(" No such option available ")
        exit()

    



