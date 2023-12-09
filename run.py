import os
import json
from PIL import Image

f = open('link.json')

data = json.load(f)

if not os.path.isdir('/web-app/'):
    os.mkdir('/web-app')

elif os.path.isdir('/web-app/'):

    for k in (data['data']):
        link = (k['link'])
        name = (k['name'])
        print(link+name)
        c="nativefier '"+link+"' -n "+name+" --disable-dev-tools --darwin-dark-mode-support true --background-color '#000'"
        d=c
        os.system(d)
        print(d)


        g="""{
  "name": " """+name+"""",
  "version": "1.0.0",
  "description": "Placeholder for the nativefier cli to override with a target url",
  "main": "lib/main.js",
  "author": "Jia Hao",
  "license": "MIT",
  "keywords": [
    "desktop",
    "electron",
    "placeholder"
  ],
  "scripts": {
  },
  "dependencies": {
    "electron-context-menu": "^3.6.1",
    "electron-dl": "^3.5.0",
    "electron-squirrel-startup": "^1.0.0",
    "electron-window-state": "^5.0.3",
    "loglevel": "^1.8.1",
    "source-map-support": "^0.5.21"
  },
  "devDependencies": {
    "electron": "^25.7.0"
  }
}"""

        e="mv ~/apps/{}-linux-x64 /web-app/".format(name)
        os.system(e)

        try:
            img = Image.open("/web-app/{}-linux-x64/resources/app/icon.ico".format(name))
            img = img.rotate(360)
            img.save("/web-app/{}-linux-x64/resources/app/icon.png".format(name))

        except IOError:
            pass
        h=open("/web-app/{}-linux-x64/resources/app/package.json".format(name),'w')
        h.write(g)
        h.close()
        i=open('/usr/local/share/applications/org.{}.desktop'.format(name),'w')
        print("""[Desktop Entry]
        Name={}
        Exec=/web-app/{}-linux-x64/{}
        Icon=/web-app/{}-linux-x64/resources/app/icon.png
        Terminal=false
        Type=Application
        Categories=GTK;
        StartupNotify=true
        """.format(name,name,name,name))

        i.write("""[Desktop Entry]
Name={}
Exec=/web-app/{}-linux-x64/{}
Icon=/web-app/{}-linux-x64/resources/app/icon.png
Terminal=false
Type=Application
Categories=GTK;
StartupNotify=true
                """.format(name,name,name,name))
        i.close()
f.close()
