import subprocess
import time
import os
from colorama import init, Fore, Style
from datetime import datetime
import sys

# Initialize colorama for colored output on Windows
if sys.platform == "win32":
    init(autoreset=True)

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

# Specify the folder where log files will be saved
log_folder = os.path.join(os.path.expanduser("C:\Dixon_Project\Softwares\IPerf-3.17.1"), "Logs")  # Saves in user's home directory

# Check if the folder exists; if not, create it
os.makedirs(log_folder, exist_ok=True)  # Automatically create the folder if it doesn't exist

# Create a timestamp for log file name
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = os.path.join(log_folder, f"log_{timestamp}.txt")  # Save in the specified folder

# Open the log file for writing
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
    
    print(Fore.GREEN + " |")
    log_file.write(" |\n")
    
    print(Fore.GREEN + border)
    log_file.write(border + '\n\n')

    # Ask the user for the IP address
    ip_address = input("Enter the IP address of the server: ")
    log_file.write(f"Entered IP Address: {ip_address}\n")

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
        
        # Display and log message before running the command in red
        message = f"\nRunning iperf3 command for {duration} seconds..."
        print(Fore.RED + message)
        log_file.write(message + '\n')

        # Execute the iperf3 command
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            output_message = f"iperf3 command output ({duration} seconds):\n{result.stdout}"
            print(output_message)
            log_file.write(output_message + '\n')
        except subprocess.CalledProcessError as e:
            error_message = f"An error occurred during the {duration} seconds test:\n{e.stderr}"
            print(Fore.RED + error_message)
            log_file.write(error_message + '\n')
