massip = input("Enter your Ip of the Master Node : ")
print(massip)
portnum = input("Enter the Port number : ")
print(portnum)
f = open("/etc/hadoop/core-site.xml", "a")
f.write("<property>")
f.write("\n<name>fs.default.name</name>")
f.write("\n<value>hdfs://{}:{}</value>".format(massip, portnum))
f.write("\n</property>")
f.close()