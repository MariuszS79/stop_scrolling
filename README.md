# Website Blocker
This Website Blocker project allows users to easily block and unblock access to specified websites on their local machine. It's intended as a productivity tool to help minimize distractions by temporarily restricting access to time-consuming sites.

## Features
Toggle Blocking: With a single execution, toggle the blocking state of predefined websites.
Temporary Blocking: Set the script to automatically unblock websites after a specified duration.
Cross-Platform: Works on Windows, macOS, and Linux by modifying the system's hosts file.
## Requirements
Python 3.x  
Administrator or root access to modify the hosts file
## Installation
Clone the repository or download the ZIP file and extract it.
Navigate to the project directory in your terminal or command prompt.
Ensure Python 3 is installed on your system.
## Usage
To use the Website Blocker, follow these steps:

**1. Edit the Script:** Open the stop_wasting_time.py file in a text editor and modify the **websites** list to include the URLs you wish to block or unblock.  
`websites = ["www.example.com", "example.com"]`
  
**2. Run the Script:** Execute the script with administrator or root privileges.

*On Windows:* Right-click the command prompt and select "Run as administrator". Navigate to the project directory and run:  
`python stop_wasting_time.py`  
This will toggle the blocking status of the websites. If they were previously unblocked, they will be blocked, and if they were blocked, they will be unblocked.  
  
*On macOS/Linux:* Open the terminal, navigate to the project directory, and run:  
`sudo python3 stop_wasting_time.py`  
Similar to Windows, this command toggles the blocking status of the websites defined in the script.  
Ensure to run the script with the necessary privileges (administrator or root) to allow changes to the hosts file.

# Conversion to Executable  
To convert **stop_wasting_time.py** to an executable file, use **auto-py-to-exe**:  
  
**1. Install auto-py-to-exe:**  
`pip install auto-py-to-exe` 
  
**2. Run** *auto-py-to-exe* and follow the on-screen instructions to select your script and create an executable.  
Creating a Shortcut for the Executable
After converting your script to an .exe file, you might want to create a shortcut for it that is set to always run as an administrator:
  
**3.Create the Shortcut:**

Right-click on the .exe file and select "Create shortcut". If you're on the desktop, the shortcut will be created there; otherwise, you might be prompted to place the shortcut on the desktop.
Set Shortcut to Run as Administrator:

Right-click on the shortcut and select "Properties".  
"Compatibility" button.  
Check the "Run as administrator" box, then click "OK" to close, and "OK" again to close the Properties window.  
  
**Using the Shortcut**  
Now, whenever you run the script using this shortcut, it will automatically request administrative privileges, which are necessary for modifying the hosts file. This setup is particularly useful for scripts that need to make system-level changes.
  
*Starting the Script*: Running the .exe file will block the websites listed in the script if they are currently unblocked.  
*Stopping the Script*: Running the .exe file again will unblock the websites, reversing the script's action.  
  
This toggle functionality is retained in the executable, making it convenient to enable or disable website blocking with just a double-click. Remember to use the shortcut created earlier to ensure the executable runs with administrator privileges, which is necessary for it to modify the system's hosts file effectively.

# Note 
This tool modifies your system's hosts file. Use it responsibly and ensure you have backups of any modified system files. 

# Troubleshooting  
If you experience issues where websites remain accessible after attempting to block them, or if blocking does not seem to take effect immediately after unblocking, try the following steps:
  
**Browser Issues After Unblocking**  
Restart Your Browser: Some changes may not take effect until you close and reopen your browser. This refreshes the browser's cache and applies the new DNS settings.

Clear Browser Cookies and Cache: Persistent cookies or cached data might allow access to the site even after it's been blocked. Clearing your browser's cookies and cache can help ensure that the blocking is effective. Here’s how to do it for the most common browsers:

*Google Chrome*: Go to Settings > Privacy and security > Clear browsing data. Check "Cookies and other site data" and "Cached images and files," then click "Clear data."

*Mozilla Firefox*: Go to Options > Privacy & Security > Cookies and Site Data > Clear Data. Check "Cookies and Site Data" and "Cached Web Content," then click "Clear."

*Microsoft Edge*: Go to Settings > Privacy, search, and services > Clear browsing data. Choose "Cookies and other site data" and "Cached images and files," then click "Clear now."

*Safari*: Go to Safari > Preferences > Privacy > Manage Website Data > Remove All.
  
If after following these steps, you continue to have issues with website blocking or unblocking, ensure that the script is being run with administrator or root privileges, as changes to the hosts file require elevated permissions.


