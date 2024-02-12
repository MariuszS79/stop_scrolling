hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # Use r"/etc/hosts" for macOS and Linux

# List the websites you want to unblock
websites_to_unblock = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com", "www.onet.pl", "www.onet.pl"]

def unblock_websites():
    with open(hosts_path, 'r+') as file:
        lines = file.readlines()  # Read all lines in the file
        file.seek(0)  # Move the file pointer to the start of the file
        for line in lines:
            if not any(website in line for website in websites_to_unblock):
                file.write(line)  # Write back lines that don't match the block list
        file.truncate()  # Truncate the file to the new size

unblock_websites()
print("Websites have been unblocked.")