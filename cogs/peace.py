from discord.ext import commands
import discord
import os
from replit import db
import re
import random
import datetime

class peace(commands.Cog):
  # CONTSTRANT VALUES GET FROM Secret Value
  # Bad word
  
  def __init__(self, bot):
    self.bot = bot
    self.TOKEN = os.getenv('TOKEN')
    self.GUILD_ID = int(os.getenv('GUILD_ID'))
    self.ADMIN_CHANNEL_ID = int(os.getenv('ADMIN_CHANNEL_ID'))
    self.bad_words =['đụ','đĩ','cặc','buồi','lồn','đéo','chịch','địt mẹ', 'địt má','địt bố','địt cụ','địt đĩ','địt lồn','di me', 'du me', 'du ma', 'dit cu','chet me may','dit ma','dit cu', 'dit bo', 'dit lon', 'cc', ' cl ', 'clmm', 'im me','im mẹ', 'im bố', 'dit me','ditme','dime','ditbo','dime', 'dit chet cu', 'dit chet cha', 'địt', 'loz', 'sex', 'dume', 'duma','đm','Đcm','dkm']
    # Bad words version 2
    self.bad_words2 = ['chich','lon','cac', 'dm','duma', 'dcm']
  #-----------------Bad Words Prevent----------------
  #check and replace bad words
  def replaceBadWords(UserMessage, BadWordsList):
    finalMessage = UserMessage
    for item in BadWordsList:
      for word in re.sub('[^a-zA-Z 0-9 \n\. á à ả ã ạ â ấ ầ ậ ẫ ă ẳ ắ ẵ ằ ặ đ ọ ò õ ỏ ó ẹ é è ẽ ẻ ỉ í ị ì ĩ ê ệ ế ề ễ ể ọ ô ố ồ ổ ộ ỗ ợ ơ ở ớ ờ ỡ ụ ù ủ ũ ú ự ư ứ ừ ữ ử ỵ ý ỷ ý ỳ ỹ đ]','', str(finalMessage)).split():
        if word == item or (item in word and ( (word[0] == 'c' and word[-1]=='c') or (word[0]== 'l' and word[-1] == 'n'))):
          finalMessage = finalMessage.replace(item,"\*"*len(item))
    return finalMessage

  # Register another event
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.bot.user: 
      return
      
    #BAD WORDS PREVENT RULE
    # 1. Delete the message. (Done)
    # 2. Send warning text. (Done)
    # 3. Warning to admin. (Done)
    # Content of the message without numbers and special chars
    content = re.sub('[^a-zA-Z 0-9 \n\. các á à ả ã ạ â ấ ầ ậ ẫ ă ẳ ắ ẵ ằ ặ đ ọ ò õ ỏ ó ẹ é è ẽ ẻ ỉ í ị ì ĩ ê ệ ế ề ễ ể ọ ô ố ồ ổ ộ ỗ ợ ơ ở ớ ờ ỡ ụ ù ủ ũ ú ự ư ứ ừ ữ ử ỵ ý ỷ ý ỳ ỹ đ]', '', str(message.content.lower()))
    #(word[0] == 'c' and word[-1]=='c') or 
    # if (word in message.content.lower() for word in bad_words2):
    for item in self.bad_words2:
      for word in content.split(): 
        if word == item or (item in word and ( (word[0] == 'c' and word[-1]=='c') or  (word[0]== 'l' and word[-1] == 'n'))):
          # Delete message
          await message.channel.purge(limit=1)
          # Fix and re-send the message
          embed=discord.Embed(title="", description=f"{peace.replaceBadWords(message.content.lower(), self.bad_words2)}")
          embed.set_author(name=f"{message.author.display_name} ({message.author.name})", icon_url= message.author.avatar_url)
          embed.set_footer(text="*Tin nhắn đã được lọc lại do nghi vấn chứa các từ nhạy cảm.")
          await message.channel.send(embed=embed)

          return
    for item in self.bad_words:
      for word in content.split():
        if word == item:
          print(word+"/"+item)
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
          embed=discord.Embed(title="REPORT", description=f'Báo cáo về sử dụng từ nhạy cảm của thành viên\n Từ nghi vấn: \"{word}\" hoặc \"{item}\"', color=0xff0000, timestamp = datetime.datetime.utcnow())
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
# ----setup------
def setup(bot):
  bot.add_cog(peace(bot))
