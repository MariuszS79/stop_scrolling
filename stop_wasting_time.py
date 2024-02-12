
import os
import time

# Path to the hosts file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if os.name == 'nt' else "/etc/hosts"
redirect = "127.0.0.1"
# Websites you want to control
websites = ["www.facebook.com", "facebook.com", "www.onet.pl", "onet.pl", "www.reddit.com", "reddit.com", "www.instagram.com", "instagram.com"]

def toggle_websites_blocking():
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        blocked = False
        for line in content:
            if any(website in line for website in websites):
                blocked = True
                break
        
        if blocked:
            # If websites are found in the file, remove them (unblock)
            new_content = [line for line in content if not any(website in line for website in websites)]
            file.writelines(new_content)
            print("Websites have been unblocked.")
        else:
            # If websites are not found in the file, block them
            file.writelines(content)
            for website in websites:
                file.write(f"{redirect} {website}\n")
            print("Websites have been blocked.")
        file.truncate()

toggle_websites_blocking()

time.sleep(3)