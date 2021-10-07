from discord.ext import commands
import discord
import os
from replit import db
import re
import random
import datetime

class encourage(commands.Cog):
  # CONTSTRANT VALUES GET FROM Secret Value
  # Bad word
  
  def __init__(self, bot):
    self.bot = bot
    self.TOKEN = os.getenv('TOKEN')
    self.GUILD_ID = int(os.getenv('GUILD_ID'))
    self.STUDY_GOAL_CHANNEL_ID = int(os.getenv('STUDY_GOAL_CHANNEL_ID'))
    #------Conversation Tmplate------#
    self.sayhi = ['hello ','Chào ','Hi ','Xin chào ','chào ','xin chào ','hi ', 'nihao ','konichiwa ','Annie ']
    self.Hi_Template = ['Rất vui được gặp bạn!','Annie là hỗ trợ viên của cộng đồng Creative Hub đó. Nếu cần giúp hãy nhớ đến Annie ha!','Hôm nay trời đẹp nhỉ? Có vẻ rất thích hợp để học và vui chơi!', 'Nếu như bạn cảm thấy mình cô đơn thì hãy nhớ là còn có Annie luôn bên cạnh!','Một với một là hai, bạn với Annie là một đôi đó hehe :3','Hoa hồng nào cũng có gai, nhưng mà Annie thì không có đâu nhé!\n Annie rất thân thiện đó. <3','Nụ cười của bạn thật tươi, Annie có thể nói chuyện với bạn được không?','Không dễ gì gặp được nhau giữa dòng đời đâu đó! Bạn với Annie có duyên lắm đó nha!!!!']
    self.Sad = ['huhu','hix','buồn','sad','chán','nản']
    self.Encourage_Template = ['Đừng buồn nhé, luôn có Annie bên bạn.','Ai chọc bạn, đứng ra đây đi. Annie không thích đâu nhé!','Đời có bao nhiêu đâu mà buồn, hãy vững tin và quên đi tất cả.','Quẳng gánh lo đi và vui sống. Chỉ cần chúng ta bình tĩnh và xác định đúng mục tiêu thì thành công sẽ luôn mỉm cười với mình.','Tôi không thể bảo vệ trái tim bạn khỏi đau thương và rỉ máu, nhưng tôi sẽ cùng bạn làm những điều thật ý nghĩa và tươi đẹp để làm lành vết thương ấy.','Thành công lớn nhất là ta biết đứng dậy sau thất bại. Vấp ngã ở đâu hãy đứng lên ở đó. Tôi tin bạn có thể làm điều đó tốt.',' Buồn bạn có thể khóc, nhưng khóc xong hãy mạnh mẽ bước tiếp. Cuộc sống sẽ không có chỗ cho những kẻ chỉ biết nhìn về quá khứ mà lãng phí tương lai đâu đấy.']
    

  #-----------------Bad Words Prevent----------------
  # Register another event
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.bot.user: 
      return
    if message.content.startswith(tuple(self.sayhi)):
      await message.channel.send(f'Chào {message.author.name}! {random.choice(self.Hi_Template)}')
    elif any(word in message.content.lower() for word in self.Sad):
      await message.channel.send(f'Này {message.author.name}!\n{random.choice(self.Encourage_Template)}')
    elif message.channel.id == self.STUDY_GOAL_CHANNEL_ID:
      react = '💪'
      await message.add_reaction(emoji=react)
# ----setup------
def setup(bot):
  bot.add_cog(encourage(bot))
