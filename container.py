import os
print("""
Available distro container in Armoury
      
        AlmaLinux
        Alpine_Linux
        Amazon_Linux
        Arch_Linux
        Debian
        CentOS(Stream)
        Crystal_linux
        Fedora
        Gentoo
        Kali_linux
        openSUSE
        RedHat_Enterprise_Linux
        Rocky_Linux
        Ubuntu
        Void_linux


""")
distro_name=input("enter distro name :") 
type__= distro_name.lower()
name=input("enter container name (7 character recomented):")
cname=" "+name+" --yes"

#linux containers
AlmaLinux="distrobox create --image quay.io/toolbx-images/almalinux-toolbox:9 -n"+cname
Alpine_Linux="distrobox create --image quay.io/toolbx-images/alpine-toolbox:3.18 -n"+cname
Amazon_Linux="distrobox create --image quay.io/toolbx-images/amazonlinux-toolbox:2023 -n"+cname
Arch_Linux="distrobox create --image quay.io/toolbx-images/archlinux-toolbox:latest -n"+cname
CentOS="distrobox create --image quay.io/toolbx-images/centos-toolbox:stream9 -n"+cname
Crystal_linux="distrobox create --image registry.getcryst.al/crystal/misc/docker:latest"+cname
Debian="distrobox create --image quay.io/toolbx-images/debian-toolbox:12 -n"+cname
Fedora="distrobox create --image quay.io/toolbx-images/fedora-toolbox:40 -n"+cname
Gentoo="distrobox create --image docker.io/gentoo/stage3:latest -n"+cname
Kali_linux="distrobox create --image docker.io/kalilinux/kali-rolling:latest -n"+cname
openSUSE="distrobox create --image quay.io/toolbx-images/opensuse-toolbox:tumbleweed -n"+cname
RedHat_Enterprise_Linux="distrobox create --image quay.io/toolbx-images/rhel-toolbox:9.2 -n"+cname
Rocky_Linux="distrobox create --image quay.io/toolbx-images/rockylinux-toolbox:9 -n"+cname
Ubuntu="distrobox create --image quay.io/toolbx-images/ubuntu-toolbox:23.10  -n"+cname
Void_linux="distrobox create --image ghcr.io/void-linux/void-glibc-full:latest -n"+cname

def create(type_):
    if "almaLinux"in type_:
        os.system(AlmaLinux)

    elif'alpine_Linux' in type_:
        os.system(Alpine_Linux)

    elif'amazon_Linux' in type_:
        os.system(Amazon_Linux)

    elif 'arch_Linux' in type_:
        os.system(Arch_Linux)

    elif 'debian' in type_:
        os.system(Debian)

    elif 'centOS' in type_:
        os.system(CentOS)
    elif 'stream' in type_:
        os.system(CentOS)

    elif 'crystal_linix' in type_:
        os.system(Crystal_linux)

    elif 'fedora' in type_:
        os.system(Fedora)

    elif 'gentoo' in type_:
        os.system(Gentoo)

    elif 'kali_linux' in type_:
        os.system(Kali_linux)

    elif  'opensuse' in type_:
        os.system()

    elif 'redhat_enterprise_linux' in type_:
        os.system(RedHat_Enterprise_Linux)

    elif 'rocky_linux' in type_:
        os.system(Rocky_Linux)

    elif 'ubuntu' in type_:
        os.system(Ubuntu)

    elif 'void_linux' in type_:
        os.system(Void_linux)

    else:
        print ("Enter correct distro name")

create(type__)
print (type__)
