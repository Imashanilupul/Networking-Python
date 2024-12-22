import socket
import termcolor

def scan(target, ports):
    """
    Scans the specified number of ports on the given target IP address.
    """
    print(termcolor.colored(f"[?] Scanning Your IP: {target}", "light_blue"))
    for port in range(1, ports + 1):
        scan_port(target, port)

def scan_port(ipaddress, port):
    """
    Scans an individual port on a given IP address.
    """
    try:
        sock = socket.socket()
        sock.settimeout(1.0)  
        sock.connect((ipaddress, port))  
        print(termcolor.colored(f"[+] Port {port} is Open", "green"))
    except socket.timeout:
        print(termcolor.colored(f"[-] Port {port}: Timed Out", "yellow"))
    except ConnectionRefusedError:
        print(termcolor.colored(f"[-] Port {port}: Connection Refused", "red"))
    except Exception as e:
        print(termcolor.colored(f"[-] Port {port}: Error {str(e)}", "red"))
    finally:
        sock.close()

def get_local_ip_address():
    """
    Retrieves the local IP address of the user's machine.
    """
    try:
        hostname = "8.8.8.8" 
        port = 80
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((hostname, port))
            return s.getsockname()[0]
    except Exception as e:
        return f"Error: {e}"

# Main script logic
try:
    target = get_local_ip_address()
    print(termcolor.colored(f"[!] Your Local IP Address: {target}", "cyan"))

    ports = int(input(termcolor.colored("[E] Enter the Number of Ports to Scan: ", "yellow")))

    scan(target.strip(), ports)
except ValueError:
    print(termcolor.colored("[-] Invalid Input. Please enter a valid number of ports.", "red"))
except Exception as e:
    print(termcolor.colored(f"[-] An unexpected error occurred: {str(e)}", "red"))
