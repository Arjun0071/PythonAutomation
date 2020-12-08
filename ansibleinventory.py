ip = input("Enter the IP of the Host : ")
print(ip)
passwd = input("Enter the password of the O.S. : ")
print(passwd)
connec = input("Enter the connection type : ")
print(connec)
name = input("Enter a path for your inventory .txt file : ")
print(name) 
f = open("{}".format(name), "a")
f.write("{}".format(ip))
f.write(" ansible_user=root")
f.write(" ansible_ssh_pass={}".format(passwd))
f.write(" ansbile_connection={}".format(connec))
f.close()

a = open("/etc/ansible/ansible.cfg", "a")
a.write("[defaults]")
a.write("\ninventory = {}".format(name))
a.write("\nhost_key_checking=false")
a.close




