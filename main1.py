import os

f=open('con_list.py',"w")
f.close()

os.system("""
container_manager="podman"
container_list=$(${container_manager} ps -a --no-trunc --format \
	"{{.ID}}|{{.Image}}|{{.Names}}|{{.Status}}|{{.Labels}}{{.Mounts}}")
IFS='
'
echo "i=[" \ >> con_list.py

for container in ${container_list}; do
	if [ -z "${container##*distrobox*}" ]; then

		container_image="$(printf "%s" "${container}" | cut -d'|' -f2)"

		echo "'""${container_image}""'," \ >> con_list.py
	fi
done
echo "]" \ >> con_list.py

echo "\n" \ >> con_list.py


echo "j=[" \ >> con_list.py
for container in ${container_list}; do
	if [ -z "${container##*distrobox*}" ]; then
		container_name="$(printf "%s" "${container}" | cut -d'|' -f3)"
		echo "'""${container_name}""'," \ >> con_list.py
	fi
done
echo "]" \ >> con_list.py
echo "\n" \ >> con_list.py
echo "k=[" \ >> con_list.py
for container in ${container_list}; do
	if [ -z "${container##*distrobox*}" ]; then
		container_status="$(printf "%s" "${container}" | cut -d'|' -f4)"
        if [ -z "${container_status##*Up*}" ] || [ -z "${container_status##*running*}" ]; then
			a=True
		else
			a=False
		fi
		echo "'""${a}""'," \ >> con_list.py
	fi
done
echo "]" \ >> con_list.py
    """)
import con_list

i=con_list.i
j=con_list.j
k=con_list.k
#="distrobox create --image  -n"+cname
print("Container type\n")
for m in i:
    if 'quay.io/toolbx-images/almalinux-toolbox:9' == m:
        print("AlmaLinux")
    if 'docker.io/library/alpine:latest' == m:
        print("Alpine linux")
    if 'quay.io/toolbx-images/amazonlinux-toolbox:2023' == m:
        print("Amazon_Linux")
    if 'quay.io/toolbx-images/archlinux-toolbox:latest' == m:
        print("Arch_Linux")
    if 'quay.io/toolbx-images/centos-toolbox:stream9' == m:
        print("CentOS")
    if 'registry.getcryst.al/crystal/misc/docker:latest' == m:
        print("Crystal_linux")
    if 'docker.io/library/debian:latest' == m:
        print("Debian")
    if 'quay.io/toolbx-images/fedora-toolbox:40' == m:
        print("Fedora")
    if 'docker.io/gentoo/stage3:latest' == m:
        print("Gentoo")
    if 'docker.io/kalilinux/kali-rolling:latest' == m:
        print("Kali_linux")
    if 'quay.io/toolbx-images/opensuse-toolbox:tumbleweed' == m:
        print("openSUSE")
    if 'quay.io/toolbx-images/rhel-toolbox:9.2' == m:
        print("RedHat_Enterprise_Linux")
    if 'quay.io/toolbx-images/rockylinux-toolbox:9' == m:
        print("Rocky_Linux")
    if 'quay.io/toolbx-images/ubuntu-toolbox:23.10' == m:
        print("Ubuntu")
    if 'ghcr.io/void-linux/void-glibc-full:latest'== m:
        print("Void_linux")
print('\n')
print("container name :\n")
for n in j:
    print(n)
print("\ncontainer status :\n")
for o in k:
    print(o)
