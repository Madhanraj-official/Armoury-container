import os
cname=input('Enter your container name')
delete="distrobox rm -n "+cname
os.system(delete)
