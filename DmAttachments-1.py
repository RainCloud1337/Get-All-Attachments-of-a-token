import  asyncio, json, time, os
try:
    import requests
    from colorama import Fore, init
except (ModuleNotFoundError):
    os.system('pip install requests colorama')

init(convert=True)

class DmAttachment:
    def __init__(self, token):
        self.token = token
        self.session = requests.Session()
        self.attachments = []
        self.user = {}
        self.api = "https://discord.com/api/v8/"
        self.file = open("attachments.txt", "a+")

    def loadUser(self):
        _response = self.session.get(f"{self.api}users/@me", headers={"Authorization": self.token})
        if _response.status_code < 400:
            self.user = _response.json()
            return self.user
        else:
            print('Invalid Token...\nClosing...')
            time.sleep(1)
            exit()

    def getDmChannels(self):
        _response = self.session.get(f"{self.api}users/@me/channels", headers={"Authorization": self.token})

        if _response.status_code < 400:
            channels = _response.json()
            if len(channels) <= 1:
                print('No Dm Channels Found For This Token...')
                time.sleep(1)
                exit()
                return
            else:
                return _response.json()

    def getMessages(self, channelID):
        _response = self.session.get(f"{self.api}/channels/{channelID}/messages", headers={"Authorization": self.token})

        if _response.status_code < 400:
            for message in _response.json():
                self.attachments.append(message['attachments'])

    def getAttachments(self):
        count = 0
        for attachment in self.attachments:
            try:
                if attachment[0]:
                    if attachment[0]['proxy_url']:
                        count+=1
                        print(f"{Fore.GREEN} !! {Fore.RESET} Attachment Found: {Fore.CYAN}{count}{Fore.RESET}")
                        self.file.write(attachment[0]['url'] + "\n")
            except:
                continue

        self.file.close()
        print(f"{Fore.CYAN}Done!")

if __name__ == "__main__":
    print(f"{Fore.RED} Token > ", end="")
    token = input('')
    attachments = DmAttachment(token)
    attachments.loadUser()
    for channel in self.getDmChannels():
        self.getMessages(channel['id'])
    self.getAttachments()
