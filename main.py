import discord
import os
from datetime import datetime
import pytz
from stay_online import keep_alive
from discord.ext import commands, tasks

# Getting the information of new members
intents = discord.Intents.all()
intents.members = True

# Bot
client = commands.Bot(command_prefix= '?', intents=intents )

# CONTSTRANT VALUES GET FROM Secret Value
TOKEN = os.getenv('TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))
ADMIN_CHANNEL_ID = int(os.getenv('ADMIN_CHANNEL_ID'))
WELCOME_CHANNEL_ID = int(os.getenv('WELCOME_CHANNEL_ID'))
GOODBYE_CHANNEL_ID = int(os.getenv('GOODBYE_CHANNEL_ID'))
RULE_CHANNEL_ID = int(os.getenv('RULE_CHANNEL_ID'))
exten = ['cogs.peace','cogs.social']

# Register an event
@client.event
async def on_ready():
  """
  Creating the asynchronous function when the bot is ready
  """
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Over You!'))
  print(f'WE HAVE LOGGED IN AS {client.user}')
  # req = requests.get("https://discord.com/api/path/to/the/endpoint")
  # print(req.headers["X-RateLimit-Remaining"])
   #------------Sync Extention--------
  for cog in exten:
    try:
    #Doi token trong secret luon di. Xong het Tuan doi lai
    # chac la bo bot function cua con bot nay qua con khac 
      client.load_extension(cog)
      print(f'{cog} was loaded!')
    except Exception as e:
      print('ERROR: '+str(e))
  # --Run update server member stats--
  update_stats.start()

#------------Live Update Member Online----------
@tasks.loop(minutes=5.2)
async def update_stats():
  
  #Server ID: 887350632447619162
  guild = client.get_guild(GUILD_ID)
  
  #Edit stats Online Member
  list_member = guild.members
  list_channel = guild.channels 
  
  #Get all stats channels
  online_channel = None 
  member_channel = None
  studying_channel = None
  # bot_channel = None
  for channel in list_channel:
    if int(channel.id) == 887687580701839402: 
      online_channel = channel
    elif int(channel.id) == 887687809115254834:
      member_channel = channel
    elif int(channel.id) == 888421780744724510:
      studying_channel = channel

  onlineMembers = sum(member.status != discord.Status.offline and not member.bot for member in list_member)
  online = '💚 Online Now: ' +str(onlineMembers) + ' users'
  await online_channel.edit(name=online, reason = '')
  #Edit stats All Member
  mem = '👪 Members: ' +str(len(list_member)) + ' users'
  await member_channel.edit(name=mem,reason = '')
  #Edit stats Bots
  # bot = '🤖 Bot In Server: ' +str(sum(member.bot for member in list_member)) + ' bots'
  # await bot_channel.edit(name=bot, reason = '')
  #Edit stats Studying Member
  studyingMember = 0
  
  #Sao kì ta, nãy mình thay mỗi cái guild.channels thành list_channel mà... Trước đó đúng
  studying = (c for c in list_channel if( (c.type == discord.ChannelType.voice or c.type == discord.ChannelType.stage_voice ) and (('Study Room' in c.name ) or ('study with' in c.name) or ('study room' in c.name))))

  for channel in studying:
    studyingMember = studyingMember + len([member for member in channel.members if not member.bot])

  study = '📖 Studying: ' + str(studyingMember) + ' users'
  await studying_channel.edit(name=study, reason = '')
  
  # --gettime-- print to check running time
  vi_timezone = pytz.timezone('Asia/Ho_Chi_Minh')
  current_time = datetime.now(vi_timezone).strftime("%d/%m/%Y %H:%M ")
  print(f'Channel Status Update at {current_time}')


#-----------KEEP BOT ALIVE AND RUN IT-----------
keep_alive()
client.run(os.environ['TOKEN'])
