from colorama import Fore
import sys,time
import os

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(2./90)

def main():
    os.system("cls && title Notepad's Tool")
    sprint(f"""
{Fore.MAGENTA}
███╗   ██╗ ██████╗ ████████╗███████╗██████╗  █████╗ ██████╗ 
████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗
██╔██╗ ██║██║   ██║   ██║   █████╗  ██████╔╝███████║██║  ██║
██║╚██╗██║██║   ██║   ██║   ██╔══╝  ██╔═══╝ ██╔══██║██║  ██║
██║ ╚████║╚██████╔╝   ██║   ███████╗██║     ██║  ██║██████╔╝
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝     ╚═╝  ╚═╝╚═════╝ 
{Fore.LIGHTMAGENTA_EX}
═════════════════════════════════════════════════════════════  
{Fore.WHITE}
[0] Exit
[1] Option      [5] Option  
[2] Option      [6] Option 
[3] Option      [7] Option 
[4] Option      [8] Option                                   
""")
    options = input("=$>")
    
    if options == "0":
       os.system("exit")
    elif options == "1":
       print(options)
       time.sleep(0.5)
       main()
    elif options == "2":
       print(options)
       time.sleep(0.5)
       main()
    elif options == "3":
       print(options)
       time.sleep(0.5)
       main()
    elif options == "4":
       print(options)
       time.sleep(0.5)
       main()
    elif options == "5":
       print(options)
       time.sleep(0.5)
       main()
    elif options == "6":
       print(options)
       time.sleep(0.5)
       main()
    elif options == "7":
       print(options)
       time.sleep(0.5)
       main()
    elif options == "8":
       print(options)
       time.sleep(0.5)
       main()

main()