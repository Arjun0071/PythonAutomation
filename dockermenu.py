import os
import getpass

os.system("tput setaf 3")
print("\t\t\t Welcome to the Docker Menu")
os.system("tput setaf 7")
print("\t\t\t-------------------------")

passwd = getpass.getpass("Enter your Password : ")

if passwd != "bondone1":
    print("password incorrect...")
    exit()

while True:
    print("""
      \n
 Enter-1.Install Docker 
 Enter-2.Check the status of Docker 
 Enter-3.Pull an Image 
 Enter-4.Install and boot Up the Container
 Enter-5.Start a Container
 Enter-6.Stop a Container
 Enter-7.Log in to a Container
 Enter-8.See the Images Downloaded
 Enter-9.See all Container ID
 Enter-10.Remove a Container
 Enter-11.Remove a Container Forcefully
 Enter-12.Remove an Image
 Enter-13.Remove an Image forcefully
 Enter-14.Make the Docker service permanent
 Enter-15.Removes all the Containers
 Enter-16.View Logs of a Container
 Enter-17.Exit
      """)
    ch = input("    Enter Your Choice :")
    print(ch)

    if int(ch) == 1:
        reqip = input("Enter the IP Of the O.S. on which you wish to install Docker : ")
        print(reqip)
        userrname = input("Enter the satndard user name of that O.S. : ")
        print(username)
        os.system(" ssh {ip} scp dockeryumrepo.py {name}@{ip}:".format(ip = reqip, name = userrname))
        os.system("ssh {} chmod 777 /home/{} ".format(reqip, userrname))
        os.system("ssh {}  python3 /home/{}/dockeryumrepo.py".format(reqip, userrname )) 
        os.system(" ssh {}  yum install docker-ce --nobest ".format(reqip))

    elif int(ch) == 2:
        reqip = input("Enter the IP on which you check the status : ")
        print(reqip)
        os.system("ssh {} systemctl status docker".format(reqip))

    elif int(ch) == 3:
        reqip = input("Enter the IP on which you want to pull the image : ")
        print(reqip)
        imagename = input("Enter the name of the image you want to pull :")
        print(imagename)
        vers = input("Enter the Version of the Image you want to pull :")
        print(vers)
        os.system("ssh {} docker pull  {}:{}".format(reqip, imagename, vers))

    elif int(ch) == 4:
        reqqip = input("Enter the Ip  on which you wish to install and boot up the container : ")
        print(reqqip)
        imgname = input("Enter the Image Name for your Container :")
        print(imgname)
        version = input("Enter the version of the Image you want for the Container :")
        print(version)
        os.system("ssh {} docker run -it {}:{}".format(reqqip, imgname, version))

    elif int(ch) == 5:
        reqqip = input("Enter the Ip  on which you wish to start the container on : ")
        print(reqqip)
        contname = input("Enter the conatiner Name : ")
        print(contname)
        os.system("ssh {} docker start {}".format(reqqip, contname))

    elif int(ch) == 6:
        reqqip = input("Enter the Ip  on which you wish to stop the container on : ")
        print(reqqip)
        contname = input("Enter the conatiner Name : ")
        print(contname)
        os.system("ssh {} docker stop {}".format(reqqip, contname))
            
    elif int(ch) == 7:
        reqqip = input("Enter the Ip  on which you wish to log in the container on : ")
        print(reqqip)
        contname = input("Enter the conatiner Name : ")
        print(contname)
        os.system("ssh {} docker attach {}".format(reqqip, contname))

    elif int(ch) == 8:
        reqqip = input("Enter the Ip  on which you wish to see the images downloaded : ")
        print(reqqip)
        os.system("ssh {} docker image".format(reqqip))

    elif int(ch) == 9:
        reqqip = input("Enter the Ip  on which you wish to see all the Container ID's on : ")
        print(reqqip)
        os.system("ssh {} docker ps -a -q".format(reqqip))

    elif int(ch) == 10:
        reqqip = input("Enter the Ip  on which you wish to remove the Container : ")
        print(reqqip)
        contname = input("Enter the conatiner Name : ")
        print(contname)
        os.system("ssh {} docker rm {}".format(reqqip, contname))

    elif int(ch) == 11:
        reqqip = input("Enter the Ip  on which you wish to remove the Container forecefully : ")
        print(reqqip)
        contname = input("Enter the conatiner Name : ")
        print(contname)
        os.system("ssh {} docker rm -f {}".format(reqqip, contname))

    elif int(ch) == 12:
        reqqip = input("Enter the Ip  on which you wish to remove the Image : ")
        print(reqqip)
        imgname = input("Enter the image Name : ")
        print(imgname)
        version = input("Enter the version of the image : ")
        print(version)
        os.system("ssh {} docker rmi {}:{}".format(reqqip, imgname, version))

    elif int(ch) == 13:
        reqqip = input("Enter the Ip  on which you wish to remove the Image forcefully : ")
        print(reqqip)
        imgname = input("Enter the image Name : ")
        print(imgname)
        version = input("Enter the version of the image : ")
        print(version)
        os.system("ssh {} docker rmi -f {}:{}".format(reqqip, imgname, version))

    elif int(ch) == 14:
        reqqip = input("Enter the Ip  on which you wish to make the Docker service permanent : ")
        print(reqqip)
        os.system("ssh {} systemctl enable docker".format(reqqip))   

    elif int(ch) == 15:
        reqqip = input("Enter the Ip  on which you wish to remove all the Containers : ")
        print(reqqip)
        os.system("ssh {} docker rm ‘docker ps -a -q’".format(reqqip))

    elif int(ch) == 16:
        reqqip = input("Enter the Ip  on which you wish to view the Logs of the Container : ")
        print(reqqip)
        contname = input("Enter the conatiner Name : ")
        print(contname)
        os.system("ssh {} docker logs {}".format(reqqip, contname))
    
    elif int(ch) == 17:
        exit()

    else        :
        print(" No such option available ")
        exit()

    



 

