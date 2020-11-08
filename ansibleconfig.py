f = open("/etc/ansible/ansible.cfg", "a")
f.write("[defaults]")
f.write("\ninventory = ")
f.write("\nhost_key_checking=false")
f.close

