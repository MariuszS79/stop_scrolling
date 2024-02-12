import os

hosts_path = r"C:\Windows\System32\drivers\etc\hosts" # Use r"/etc/hosts" for macOS and Linux
redirect = "127.0.0.1"


websites_to_block = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com", "www.onet.pl"]


def block_websites():
    with open(hosts_path, 'r+') as hostsfile:
        hosts_content = hostsfile.read()
        for website in websites_to_block:
            if website not in hosts_content:
                hostsfile.write(redirect + " " + website + "\n")
    print("Websites have been blocked.")

block_websites()
