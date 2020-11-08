import os
import getpass

os.system("tput setaf 3")
print("\t\t\t Welcome to the AWS Menu")
os.system("tput setaf 7")
print("\t\t\t-------------------------")

passwd = getpass.getpass("Enter your Password : ")

if passwd != "bondone1":
    print("password incorrect...")
    exit()

while True:
    print("""
      \n
 Enter-1.Login to AWS account
 Enter-2.Start your Instance
 Enter-3.Stop your Instance
 Enter-4.Create a New Instance
 Enter-5.Create a New Key
 Enter-6.Create a Security Group 
 Enter-7.Create a Volume
 Enter-8.Attach Volume to Instance
 Enter-9.Create a S3 Bucket
 Enter-10.Upload an image file/file to Bucket
 Enter-11.Make your Bucket Public
 Enter-12.Create a Cloud Front Distribution
 Enter-13.Describe All Instances
 Enter-14.Exit
      """)
    ch = input("    Enter Your Choice :")
    print(ch)

    if int(ch) == 1:
     	os.system("aws configure")

    elif int(ch) == 2:
        insid = input("Enter your Instance ID : ")
        print(insid)
        os.sytem(" aws ec2 start-instances --instance-id {}".format(insid))	      

    elif int(ch) == 3:
        insid = input("Enter your Instance ID : ")
        print(insid)
        os.system(" aws ec2 stop-instances --instance-id {}".format(insid))

    elif int(ch) == 4:
        amiid = input("Enter Your AMI ID : ")
        print(amiid)
        instype = input("Enter Your Instance Type : ")
        print(instype) 
        subid = input("Enter the subnet ID : ")
        print(subid)
        secid = input("Enter the security group ID : ")
        print(secid)
        keyname = input("Enter the key name : ")
        print(keyname)
        os.system(" aws ec2 run-instances --image-id {} --instance-type {} --count 1 --subnet-id {} --security-group-id {} --key-name {} ".format(amiid, instype, subid, secid, keyname))
       

    elif int(ch) == 5:
        keyname1 = input("Enter a name for your key")
        print(keyname1)
        os.system(" aws ec2 create-key-pair --key-name {} ".format(keyname1))

    elif int(ch) == 6:
        secgrpname = input("Enter a name for your security group : ")
        print(secgrpname)
        decript = input("Enter description you want to give : ")
        print(descript)
        os.system(" aws ec2 create-security-group --group-name {} --description {} ".format(secgrpname, descript))
            
    elif int(ch) == 7:
        voltype = input("Enter your Volume type : ")
        print(voltype)
        size = input("Enter the size you want for your volume : ")
        print(size)	
        avzone =input("Enter the AV zone where you want to have the volume : ")
        print(avzone)
        os.system("aws ec2 create-volume --volume-type {} --size {} --availability-zone {} ".format(voltype, size, avzone))
        

    elif int(ch) == 8:
        ins1id = input("Enter your Instance ID : ")
        print(ins1id)
        vol1id = input("Enter your Volume ID : ")
        print(vol1id)
        devicename = input("Enter your device name : ")
        print(vol1id)
        os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device {} ".format(isn1id, vol1id, devicename))


    elif int(ch) == 9:
        buckname = input("Enter  a name for your new Bucket : ")
        print(buckname)
        regname = input("Enter the region name(in ID form) you want the Bucket in : ")
        print(regname)
        os.system("aws s3api create-bucket --bucket {a} --region {b} --create-bucket-configuration LocationConstraint={b} ".format(a=buckname, b=regname))

    elif int(ch) == 10:
        imagepath = input("Enter the path of your image file :")
        print(imagepath)
        bucketname = input("Enter your Bucket Name : ")
        print(bucketname)
        os.system("aws s3 cp {} s3://{} ".format(imagepath, bucketname))

    elif int(ch) == 11:
        bucketname = input("Enter your Bucket Name : ")
        print(bucketname)
        os.system("aws s3api put-bucket-acl --acl public-read --bucket {} ".format(bucketname))
    
    elif int(ch) == 12:
        bucketname = input("Enter your Bucket Name : ")
        print(bucketname)
        os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com ".format(bucketname))

    elif int(ch) == 13:
        os.system("aws ec2 describe-instances")
    
    elif int(ch) == 14:
        exit()

    else        :
        print(" No such option available ")
        exit()

    



