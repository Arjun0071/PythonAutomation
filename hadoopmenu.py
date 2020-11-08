import os
import getpass

os.system("tput setaf 3")
print("\t\t\t Welcome to the Hadoop Menu")
os.system("tput setaf 7")
print("\t\t\t-------------------------")

passwd = getpass.getpass("Enter your Password : ")

if passwd != "bondone1":
    print("password incorrect...")
    exit()

while True:
    print("""
      \n 
 Enter-1.Create 1 Master Node
 Enter-2.Create 1 Data Node
 Enter-3.Add Data Node
 Enter-4.Setup a Client Node
 Enter-5.Check the Hadoop  Report
 Enter-6.See the files in cluster
 Enter-7.Upload the files in Cluster
 Enter-8.Remove the files from the Cluster
 Enter-9.Read the files from the Cluster
 Enter-10.Upload the file with blocksize
 Enter-11.Exit

      """)
    ch = input("    Enter Your Choice :")
    print(ch)

    if int(ch) == 1:
        masip = input("Enter the Ip for your Master Node :")
        print(masip)
        username = input("Enter your standard user name :")
        print(username)
        os.system(" ssh {} "" rpm -ivh jdk-8u171-linux-x64.rpm;rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force""".format(masip))
        os.system(" ssh {ip} scp masappend.py {name}@{ip}:".format(ip = masip, name = username))
        os.system("ssh {} chmod 777 /home/{} ".format(masip, username))
        os.system("ssh {} mkdir /nn1".format(masip))   
        os.system("ssh {}  python3 /home/{}/masappend.py".format(masip, username))
        os.system("ssh {} hadoop namenode -format".format(masip))
        os.system("ssh {} systemctl stop firewalld".format(masip))
        os.system("ssh {} hadoop-daemon.sh start namenode".format(masip))

    elif int(ch) == 2:
        data1ip = input(" Enter the IP for your Data Node : ")
        print(data1ip)
        username1 = input("Enter your standard user name :")
        print(username1)
        os.system(" ssh {} "" rpm -ivh jdk-8u171-linux-x64.rpm;rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force""".format(data1ip))
        os.system(" ssh {ip1} scp dataappend1.py {name1}@{ip}:".format(ip1 = data1ip, name1 = username1))
        os.system("ssh {} chmod 777 /home/{} ".format(data1ip, username1))
        os.system("ssh {} mkdir /dn1".format(data1ip))  
        os.system("ssh {}  python3 /home/{}/dataappend1.py".format(data1ip, username1))
        os.system("ssh {} hadoop-daemon.sh start datanode".format(data1ip))
        

    elif int(ch) == 3:
        data2ip = input(" Enter the IP for your Data Node: ")
        print(data1ip)
        username2 = input("Enter your standard user name :")
        print(username2)
        os.system(" ssh {} "" rpm -ivh jdk-8u171-linux-x64.rpm;rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force""".format(data1ip))
        os.system(" ssh {ip2} scp dataappend2.py {name2}@{ip}:".format(ip2 = data2ip, name2 = username2))
        os.system("ssh {} chmod 777 /home/{} ".format(data2ip, username2))
        os.system("ssh {} mkdir /dn2".format(data2ip))  
        os.system("ssh {}  python3 /home/{}/dataappend2.py".format(data2ip, username2))
        os.system("ssh {} hadoop-daemon.sh start datanode".format(data2ip))
        
       
    elif int(ch) == 4:
        clientip = input(" Enter the IP for your Client Node : ")
        print(clientip)
        username3 = input("Enter your standard user name :")
        print(username3)
        os.system(" ssh {} "" rpm -ivh jdk-8u171-linux-x64.rpm;rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force""".format(data1ip))
        os.system(" ssh {ip1} scp clientappendcore.py {name3}@{clientip}:".format(ip3 = clientip, name3 = username3))
        os.system("ssh {} chmod 777 /home/{} ".format(clientip, username3))
        os.system("ssh {}  python3 /home/{}/clientappendcore.py".format(clientip, username3))
	
    elif int(ch) == 5: 
        ip4 = input("Enter the IP of the O.S.(The one's Connected in Hadoop Cluster) you want to check the hadoop cluster report : ")
        print(ip4)
        os.system(" shh {} hadoop dfsadmin -report ")

    elif int(ch) == 6:
        os.system("hadoop fs -ls / ")
            
    elif int(ch) == 7:
        file = input("Enter the file path to be Uplaoded : ")
        print(file)
        os.system("hadoop fs -put {} / ".format(file))

    elif int(ch) == 8:
        file1 = input("Enter the file name to be Removed : ")
        print(file1)
        os.system("hadoop fs -rm /{}".format(file1)) 

    elif int(ch) == 9:
        file2 = input("Enter the file name that you wanna Read :")
        print(file2)
        os.system("hadoop fs -cat /{}".format(file2))

    elif int(ch) == 10:
        size = input("Enter the block size you want for the file : ")
        print(size)
        file3 = input("Enter the file name to be Uploaded : ")
        print(file3)
        os.system("hadoop fs -Ddfs.block.size={} - put {} / ".format(size, file3)) 

    elif int(ch) == 11:
        exit()

    else        :
        print(" No such option available ")
        exit()

    



