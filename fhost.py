import subprocess
import os
import sys
from termcolor import colored

def banner():
   print(colored('''
   
██╗  ██╗ ██████╗ ███████╗████████╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████║██║   ██║███████╗   ██║       █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══██║██║   ██║╚════██║   ██║       ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝███████║   ██║       ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
-------------c̷̲o̷̲d̷̲e̷̲d̷̲ b̷̲y̷̲ w̷̲h̷̲i̷̲t̷̲e̷̲d̷̲e̷̲v̷̲i̷̲l̷̲----------------------------------------------------
   
   ''',"cyan"))

class HostFinder:
    def __init__(self):
        self.host = "127.0.0.1/24"
        self.up_hosts = []

    def set_host(self, host):
        self.host = host
        self.up_hosts = []
        self.find_host()

    def find_host(self):
        self.up_hosts = []
        print(colored(f"[+] Scanning for the host address {self.host}", "yellow"))
        try:
            output = subprocess.run(["nmap", "-sn", self.host], capture_output=True, text=True, check=True)
            for i, line in enumerate(output.stdout.splitlines()):
                if "Host is up" in line:
                    self.up_hosts.append(output.stdout.splitlines()[i - 1].split()[4])
            print(colored("[+] Scanning Completed.", "green"))
        except subprocess.CalledProcessError:
            print(colored("[!] Error: Invalid host address or nmap command not found.", "red"))
        except Exception as e:
            print(colored(f"[!] Error: {e}", "red"))

    def clear(self):
        try:
            os.system('clear')
            banner()
        except Exception as e:
            print(colored(f"[!] Error: {e}", "red"))

    def print_host(self):
        if not self.up_hosts:
            print(colored("[!] Error: No Hosts to print.", "red"))
        else:
            print(colored("[+] Hosts That are up:", "green"))
            for h in self.up_hosts:
                print(colored(h, "yellow"))

    def save_file(self, file_name="hosts.txt"):
        if not self.up_hosts:
            print(colored("[!] Error: No Hosts to save", "red"))
            return

        try:
            with open(file_name, 'a') as f:
                for u in self.up_hosts:
                    f.write(u + '\n')
            print(colored(f"[*] Successfully saved Hosts to {file_name}", "green"))
        except IOError:
            print(colored("[!] Error: Failed to open the file.", "red"))
        except Exception as e:
            print(colored(f"[!] Error: {e}", "red"))

    def help(self):
        print(colored('''find the hosts that are up in the given host range.
        help    : this command shows help message
        scan    : it will scan the hosts
        sethost : sets the host address
        exit    : exits the script
        clear   : it clears the terminal
        print   : it is to print all the found hosts
        save    : it will save the hosts that found''', "green"))


def main():
    host_finder = HostFinder()
    while True:
        command = input(">> ")
        if command == "sethost":
            host = input("Host for scanning: ")
            host_finder.set_host(host)
        elif command == "scan":
            host_finder.find_host()
        elif command == "help":
            host_finder.help()
        elif command == "clear":
            host_finder.clear()
        elif command == "save":
            file_name = input(colored("Enter the file name[Default: hosts.txt]: ", "green")) or "hosts.txt"
            host_finder.save_file(file_name)
        elif command == "print":
            host_finder.print_host()
        elif command == "exit":
            print(colored("Bye Bye.....", "red"))
            break
        else:
            print(colored("[!] Invalid Command! try help to see the commands..","red"))
try:
    main()
except Exception as e:
    print(colored(f"Error: {e}","red"))
except KeyboardInterrupt:
    print(colored("\n[!] User Interrupted.","red"))
    sys.exit(0)

