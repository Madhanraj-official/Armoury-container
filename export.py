import os
distro_name=input("Enter armoury container name :")
export=input("if you want export app type app or export binary type bin :")
if export == 'app':
    app_name=input("Enter app name [terminal cammand only]:")
    export_app="/usr/local/bin/distrobox-enter  -n {} --   /usr/bin/distrobox-export --app {}  %U".format(distro_name,app_name)
    os.system(export_app)

if export == 'bin':
    sudo_user=input("this binary access sudo[y/n]:")
    sudo_user=sudo_user.lower()
    if sudo_user=="y":
        bin_name=input("Enter binary path :")
        export_bin="/usr/local/bin/distrobox-enter  -n {} --   /usr/bin/distrobox-export --bin {} --sudo %U".format(distro_name,bin_name)
        os.system(export_bin)
    else :
        bin_name=input("Enter binary path :")
        export_bin="/usr/local/bin/distrobox-enter  -n {} --   /usr/bin/distrobox-export --bin {}  %U".format(distro_name,bin_name)
        os.system(export_bin)
