import time 
from datetime import datetime as dt

# colocar en la siguiente lista las paginas que deseamos eliminar

websites_list = [   
      "twitter.com",
      "www.twitter.com",
      "instagram.com",
      "www.instagram.com"
      "facebook.com"
]

# colocar en "host" el directorio donde se encuentra ubicado el archivo host, en el caso de windows: 'C:\Windows\System32\drivers\etc', en el caso de linux: '/etc/host/'
host = "hosts"

redirect = '127.0.0.1'

from_hour = 10
to_hour = 18

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, from_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, to_hour):
        print("work")
        with open(host, 'r+') as file:
            content = file.read()
            for website in websites_list:
               if website in content:
                   pass
               else:
                   file.write(redirect + " " +    website + "\n")
    else:
        print('relax bru')
    time.sleep(5)


