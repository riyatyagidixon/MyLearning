# For Windows platform
# =============================
import subprocess
import time
import re
import os
from colorama import init, Fore, Style
from datetime import datetime
import sys

# Set the SSID and password
target_ssid = "Airtel_Zerotouch_DXB_6"
password = "Airtel@123"
iperf3_dir = "C:\Dixon_Projects\Softwares\IPerf-3.17.1"
iperf3_path = "C:\Dixon_Projects\Softwares\IPerf-3.17.1\iperf3.exe"

# Specify the folder where log files will be saved
log_folder = os.path.join(os.path.expanduser(f"{iperf3_dir}"), "Logs")  # Saves in user's home directory

# Check if the folder exists; if not, create it
os.makedirs(log_folder, exist_ok=True)  # Automatically create the folder if it doesn't exist

# Create a timestamp for log file name
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = os.path.join(log_folder, f"log_{timestamp}.txt")  # Save in the specified folder

def company_logo():
    with open(log_filename, 'w') as log_file:
        # Display company name in a smooth manner
        company_name = "Dixon Electro Appliances"
        border = "+" + "-" * (len(company_name) + 2) + ""
    
        # Print and log the company name with a border
        print(Fore.GREEN + "\n" + border)
        log_file.write(border + '\n')
    
        print(Fore.GREEN + "| ", end='')
        log_file.write("| ")
    
        smooth_print(company_name, delay=0.08, file=log_file)  # Smooth print company name
    
        print(Fore.GREEN + "|")
        log_file.write("|\n")
    
        print(Fore.GREEN + border)
        log_file.write(border + '\n\n')


# Function to print text smoothly with a delay between characters
def smooth_print(text, delay=0.1, file=None):
    for char in text:
        print(Fore.CYAN + char, end='', flush=True)
        if file:
            file.write(char)  # Also write to log file
        time.sleep(delay)
    print(Style.RESET_ALL)
    if file:
        file.write('\n')

       
def refresh_networks():
    """Refreshes the list of available networks by disconnecting and rescanning."""
    try:
        print("Refreshing network list...")
        
        # Disconnect from any connected networks
        disconnect_command = "netsh wlan disconnect"
        subprocess.run(disconnect_command, shell=True)
        
        # Wait for a few seconds to ensure the network refresh happens
        time.sleep(2)
        
        # Scan for networks again
        print("Rescanning networks...")
        refresh_command = "netsh wlan show networks"
        refreshed_scan_result = subprocess.check_output(refresh_command, shell=True).decode()
        
        return refreshed_scan_result
    
    except Exception as e:
        print(f"Error while refreshing networks: {e}")
        return ""


def scan_and_connect(ssid, password):
    try:
        # Refresh and scan networks
        scan_result = refresh_networks()

        # Check if the target SSID is available after refresh
        if ssid in scan_result:
            print(f"SSID '{ssid}' found. Attempting to connect...")

            # Create Wi-Fi profile
            profile = f"""
            <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
                <name>{ssid}</name>
                <SSIDConfig>
                    <SSID>
                        <name>{ssid}</name>
                    </SSID>
                </SSIDConfig>
                <connectionType>ESS</connectionType>
                <connectionMode>auto</connectionMode>
                <MSM>
                    <security>
                        <authEncryption>
                            <authentication>WPA2PSK</authentication>
                            <encryption>AES</encryption>
                            <useOneX>false</useOneX>
                        </authEncryption>
                        <sharedKey>
                            <keyType>passPhrase</keyType>
                            <protected>false</protected>
                            <keyMaterial>{password}</keyMaterial>
                        </sharedKey>
                    </security>
                </MSM>
            </WLANProfile>
            """

            # Write the profile to an XML file
            profile_file = f"{ssid}.xml"
            with open(profile_file, 'w') as file:
                file.write(profile)

            # Add the profile to the system
            add_profile_command = f'netsh wlan add profile filename="{profile_file}"'
            subprocess.run(add_profile_command, shell=True)

            # Connect to the network
            connect_command = f'netsh wlan connect name="{ssid}"'
            connection_result = subprocess.run(connect_command, shell=True)

            if connection_result.returncode == 0:
                print(f"Successfully connected to {ssid}")
            else:
                print(f"Failed to connect to {ssid}")
        else:
            print(f"SSID '{ssid}' not found in the scan result after refresh.")
    
    except Exception as e:
        print(f"An error occurred: {e}")


def get_wifi_ip_address():
    try:
        # Run the 'ipconfig' command and capture the output
        ipconfig_result = subprocess.check_output("ipconfig", shell=True).decode()

        # Look for the section related to 'Wireless LAN adapter Wi-Fi'
        wifi_section = re.search(r"Wireless LAN adapter Wi-Fi.*?:\s*(.*?)(?=\n\n|\Z)", ipconfig_result, re.DOTALL)

        if wifi_section:
            wifi_info = wifi_section.group(1)

            # Search for the IPv4 Address using a regular expression
            ipv4_match = re.search(r"IPv4 Address.*?:\s*([0-9\.]+)", wifi_info)

            if ipv4_match:
                ip_address = ipv4_match.group(1)
                return ip_address
            else:
                return "IPv4 Address not found."
        else:
            return "Wireless LAN adapter Wi-Fi not found."
    
    except Exception as e:
        return f"An error occurred: {e}"


def run_iperf3_server():

    # Command to start iperf3 in server mode
    server_command = f'start cmd /k "{iperf3_path} -s"'

    # Run the command using subprocess.Popen to get the process handle
    server_process = subprocess.Popen(server_command, shell=True)

    print(f"iPerf3 server started with PID: {server_process.pid}")
    
    return server_process
    
def stop_iperf3_server(server_process):
    # Close the server by terminating its process
    print(f"Terminating server process with PID: {server_process.pid}")
    
    # Terminate the process
    os.system(f'taskkill /F /PID {server_process.pid}')

def is_iperf3_server_running():
    # Check for running iperf3 server process using 'tasklist'
    try:
        output = subprocess.check_output("tasklist", shell=True, text=True)

        # Check if 'iperf3.exe' is present in the task list
        if "iperf3.exe" in output:
            print("iPerf3 server is already running.")
            return True
        else:
            print("iPerf3 server is not running.")
            return False

    except subprocess.CalledProcessError as e:
        print(f"Error checking running processes: {e}")
        return False

def run_iperf3_server():
    # Command to start iperf3 in server mode
    server_command = f'start cmd /k "{iperf3_path} -s"'

    # Run the command in a new terminal
    subprocess.run(server_command, shell=True)
    print("iPerf3 server started.")

def execute_iper3_client_cmds():
    # Open the log file for writing
    with open(log_filename, 'w') as log_file: #4
        # Ask the user for the IP address
        ip_address = wifi_ip_address#input("Enter the IP address of the server: ")
        log_file.write(f"Entered IP Address: {ip_address}\n")

        # Launch the iperf3 server
        if not is_iperf3_server_running():
            # Step 2: If not running, start the iperf3 server
            run_iperf3_server()
            time.sleep(20)
        else:
            print("Server already running, skipping launch.")
    
        # List of commands with varying time durations, with the 30-second command first
        iperf_commands = [
            {
                "command": [
                    "iperf3.exe", "-c", ip_address, "-u", "-b", "500M", "-t", "5", "-l", "1400"
                ],
                "duration": 6
            },
            {
                "command": [
                    "iperf3.exe", "-c", ip_address, "-u", "-b", "500M", "-t", "10", "-l", "1400"
                ],
                "duration": 11
            }
        
        ]

        # Iterate over the commands and run them
        for iperf_case in iperf_commands:
            duration = iperf_case["duration"]
            command = iperf_case["command"]
            formatted_command = ' '.join(command)
            
            # Display and log message before running the command in red
            message = f"\nRunning iperf3 [{formatted_command}] for {duration - 1} seconds..."
            print(Fore.GREEN + message)
            log_file.write(message + '\n')

            # Execute the iperf3 command
            try:
                result = subprocess.run(command, capture_output=True, text=True, check=True)
                output_message = f"iperf3 [{formatted_command}] output ({duration - 1} seconds):\n{result.stdout}"
                print(Fore.WHITE + output_message)
                log_file.write(output_message + '\n')
            except subprocess.CalledProcessError as e:
                error_message = f"An error occurred during the {duration - 1} seconds test:\n{e.stderr}"
                print(Fore.RED + error_message)
                log_file.write(error_message + '\n')
            

# Initialize colorama for colored output on Windows
if sys.platform == "win32":
    init(autoreset=True)
    
# Step#1 print the company logo
company_logo()

# Step#2 Call the function to scan and connect
scan_and_connect(target_ssid, password)

# Step#3 Get and display the IP address for Wi-Fi
time.sleep(1)
wifi_ip_address = get_wifi_ip_address()
print(f"Wi-Fi IPv4 Address: {wifi_ip_address}")

# Step#4 Execute the iperf3 client commands and write into log file
execute_iper3_client_cmds()