import os
f=open('img_list.py',"w")
f.close()
f=open('name_list.py',"w")
f.close()
f=open('status_list.py',"w")
f.close()
os.system("""

#!/bin/sh

container_manager="podman"

container_list=$(${container_manager} ps -a --no-trunc --format \
	"{{.ID}}|{{.Image}}|{{.Names}}|{{.Status}}|{{.Labels}}{{.Mounts}}")
IFS='
'
echo "i=[" \ >> img_list.py
echo "j=[" \ >> name_list.py
echo "s=[" \ >> status_list.py
for container in ${container_list}; do
	if [ -z "${container##*distrobox*}" ]; then

		container_id="$(printf "%s" "${container}" | cut -d'|' -f1 | cut -c1-12)"
		container_image="$(printf "%s" "${container}" | cut -d'|' -f2)"
		container_name="$(printf "%s" "${container}" | cut -d'|' -f3)"
		container_status="$(printf "%s" "${container}" | cut -d'|' -f4)"

        if [ -z "${container_status##*Up*}" ] || [ -z "${container_status##*running*}" ]; then
			a=True
		else
			a=False
		fi

		echo "'""${container_image}""'," \ >> img_list.py
		echo "'""${container_name}""'," \ >> name_list.py
		echo "'""${a}""'," \ >> status_list.py
	fi
done
echo "]" \ >> img_list.py
echo "]" \ >> name_list.py
echo "]" \ >> status_list.py



    """)
import img_list
import name_list
import status_list



i=img_list.i
j=name_list.j
s=status_list.s


#="distrobox create --image  -n"+cname

print("Container type\n")

for k in i:
    if 'quay.io/toolbx-images/almalinux-toolbox:9' == k:
        print("AlmaLinux")
    if 'docker.io/library/alpine:latest' == k:
        print("Alpine linux")
    if 'quay.io/toolbx-images/amazonlinux-toolbox:2023' == k:
        print("Amazon_Linux")
    if 'quay.io/toolbx-images/archlinux-toolbox:latest' == k:
        print("Arch_Linux")
    if 'quay.io/toolbx-images/centos-toolbox:stream9' == k:
        print("CentOS")
    if 'registry.getcryst.al/crystal/misc/docker:latest' == k:
        print("Crystal_linux")
    if 'docker.io/library/debian:latest' == k:
        print("Debian")
    if 'quay.io/toolbx-images/fedora-toolbox:40' == k:
        print("Fedora")
    if 'docker.io/gentoo/stage3:latest' == k:
        print("Gentoo")
    if 'docker.io/kalilinux/kali-rolling:latest' == k:
        print("Kali_linux")
    if 'quay.io/toolbx-images/opensuse-toolbox:tumbleweed' == k:
        print("openSUSE")
    if 'quay.io/toolbx-images/rhel-toolbox:9.2' == k:
        print("RedHat_Enterprise_Linux")
    if 'quay.io/toolbx-images/rockylinux-toolbox:9' == k:
        print("Rocky_Linux")
    if 'quay.io/toolbx-images/ubuntu-toolbox:23.10' == k:
        print("Ubuntu")
    if 'ghcr.io/void-linux/void-glibc-full:latest'==k:
        print("Void_linux")

print('\n')
print("container name :\n")

for l in j:

    print(l)

print("\ncontainer status :\n")

for g in s:
    print(g)
