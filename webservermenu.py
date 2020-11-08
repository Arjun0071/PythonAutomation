import os
import getpass

os.system("tput setaf 3")
print("\t\t\t Welcome to the Config. Web Server Menu")
os.system("tput setaf 7")
print("\t\t\t-------------------------")

passwd = getpass.getpass("Enter your Password : ")

if passwd != "bondone1":
    print("password incorrect...")
    exit()

while True:
    print("""
      \n
 Enter-1.Install httpd
 Enter-2.Start the httpd service
 Enter-3.Stop the httpd service
 Enter-4.Check the status of the Service
 Enter-5.Exit
      """)
    ch = input("    Enter Your Choice :")
    print(ch)

    if int(ch) == 1:
     	os.system("yum install httpd")
        print("Please add your required web page in /var/www/html ") 

    elif int(ch) == 2:
        os.system("systemctl start httpd")
        print("Please add your required web page in /var/www/html ")

    elif int(ch) == 3:
        os.system("systemctl stop httpd")
        
    elif int(ch) == 4:
        os.system("systemctl status httpd")

    elif int(ch) == 5:
        exit()

    else        :
        print(" No such option available ")
        exit()

    



