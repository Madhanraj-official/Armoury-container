import os
cname=""
name=""
entry=open("/home/.local/shara/application/"+cname+".desktop",'w') 
entry.write("""[[Desktop Entry]
Name={}
GenericName=Terminal entering {}
Comment=Terminal entering {}
Categories=Distrobox;System;Utility
Exec=/usr/local/bin/distrobox enter  {}
Icon=/home/gokul/.local/share/icons/distrobox/{}.png
Keywords=distrobox;
NoDisplay=false
Terminal=true
TryExec=/usr/local/bin/distrobox
Type=Application
""".format(cname,cname,cname,cname,name))

