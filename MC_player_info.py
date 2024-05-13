import requests
from pystyle import Colorate, Colors
from colorama import Fore

def get_uuid(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["id"]
    else:
        return None

def get_skin_download_link(uuid):
    return f"https://crafatar.com/skins/{uuid}"

lol = """             __  __     __     _____         
            /\ \/\ \   /\ \   /\  __-.       
            \ \ \_\ \  \ \ \  \ \ \/\ \      
             \ \_____\  \ \_\  \ \____-      
              \/_____/   \/_/   \/____/      """

print(Colorate.Vertical(Colors.blue_to_white, lol))
print(' ')
username = input(f"{Fore.BLUE}U{Fore.BLUE}s{Fore.BLUE}e{Fore.BLUE}r n{Fore.CYAN}a{Fore.CYAN}m{Fore.WHITE}e:{Fore.WHITE} ")
uuid = get_uuid(username)
if uuid:
    print(f"{Fore.WHITE}The UUID for {username} is: {uuid}")
    skin_download_link = get_skin_download_link(uuid)
    print(f"{Fore.WHITE}Skin download link: {skin_download_link}")
else:
    print(f"{Fore.WHITE}Failed to get UUID for {username}")