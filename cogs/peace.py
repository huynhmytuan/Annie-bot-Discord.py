from discord.ext import commands
import discord
import os
from replit import db
import re
from helper.badword import checkBadWords
import datetime
from config import *

class peace(commands.Cog):
  # CONTSTRANT VALUES GET FROM Secret Value
  # Bad word
  
  def __init__(self, bot):
    self.bot = bot
    self.GUILD_ID = GUILD_ID
    self.ADMIN_CHANNEL_ID = ADMIN_CHANNEL_ID
    
  # Register another event
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.bot.user: 
      return
    check_mess = checkBadWords(message.content)
    if check_mess == True:
      #Delete message
      await message.channel.purge(limit=1)
      #Response message:
      await message.channel.send(f'Tin nhắn từ "{message.author.mention}" có những lời lẽ không hay, xin đừng thô lỗ! Hãy như Annie, thông minh, học giỏi, đáng yêu, nết na thùy mị.')
      
      if str(message.author) not in db.keys():
        db[str(message.author)] = 1
      elif str(message.author) in db.keys():
        db[str(message.author)] = int(db[str(message.author)]) + 1
      # Send notification to admins
      admin_channel = self.bot.get_guild(self.GUILD_ID).get_channel(self.ADMIN_CHANNEL_ID)
      # ---Setup embed report-------
      embed=discord.Embed(title="REPORT", description=f'Báo cáo về sử dụng từ nhạy cảm của thành viên', color=0xff0000, timestamp = datetime.datetime.utcnow())
      embed.add_field(name="Thành Viên:", value=f"{message.author.mention}", inline=True)
      embed.add_field(name="Kênh:", value=f"{message.channel.mention}", inline=True)
      embed.add_field(name="Số lần lỗi", value=f"{db[str(message.author)]}", inline=True)
      embed.add_field(name="Nội dung tin nhắn", value=f"{message.content}", inline=False)
      embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/1810/1810790.png')
      # ----Send embed----
      await admin_channel.send(embed=embed)
      # Seset Counter
      if int(db[str(message.author)]) >= 20:
        db[str(message.author)] =  0
      return
    elif isinstance(check_mess, str):
      embed=discord.Embed(title="", description=f"{check_mess}")
      embed.set_author(name=f"{message.author.display_name} ({message.author.name})", icon_url= message.author.avatar_url)
      embed.set_footer(text="*Tin nhắn đã được lọc lại do nghi vấn chứa các từ nhạy cảm.")
      await message.channel.send(embed=embed)
      return
    
# ----setup------
def setup(bot):
  bot.add_cog(peace(bot))
