from discord.ext import commands
import requests
import discord
from googletrans import Translator
import asyncio
import os
import time

class quotes(commands.Cog):
  # CONTSTRANT VALUES GET FROM Secret Value
  def __init__(self, bot):
    self.bot = bot
    self.TOKEN = os.getenv('TOKEN')
    self.GUILD_ID = int(os.getenv('GUILD_ID'))
    self.translator = Translator()

  # -----Random quoute serve ------
  @commands.command(brief='Random 1 câu nói truyền cảm hứng [EN].', description='Hiển thị 1 câu nối truyền cảm hứng. Lưu ý: Hiện tại chỉ hỗ trợ câu nói tiếng anh.', aliases = ['quote'] )
  async def q(self, ctx, type):
    if(type=='anime'):
      # Get API DATA
      response = requests.get("https://animechan.vercel.app/api/random").json()
      # Embed Setup
      try:
        embed = quotes.quoteEmbed(self,response['character'],"\""+response['quote']+"\"","\""+self.translator.translate(response['quote'], dest='vi').text+"\"",type,response['anime'])
        await ctx.reply(embed=embed)
      except Exception as e:
        print(e)
    if type == 'book':
      response = requests.get("https://api.hamatim.com/quote").json()
      # Embed Setup
      try:
        embed = quotes.quoteEmbed(self,response['author'],response['text'],self.translator.translate(response['text'], dest='vi').text,type,response['book'],response['author_img'])
        await ctx.reply(embed=embed)
      except Exception as e:
        print(e)
    if type == 'joke':
      await ctx.reply("Đang si nghĩ.. chờ xíu...")
      # time.sleep(3)
      joke = requests.get('https://v2.jokeapi.dev/joke/Any?blacklistFlags=racist').json()
      if joke["type"] == "single": 
        await ctx.reply(joke["joke"])
      else:
        await ctx.send(joke["setup"])
        time.sleep(5)
        await ctx.send(joke["delivery"])

  # --Kick Error Checks--
  @q.error
  async def q_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
     #notice command result in admin channel
      embed=discord.Embed(title="Vui lòng chọn loại qoute:", description="*Lưu ý hiện tại toàn bộ quote đều bằng tiếng anh. \nPhần dịch hoàn toàn được dịch thông qua Google Translate)\nChọn bằng cách sử dụng các lệnh sau:", color=0x00a0bd)
      embed.add_field(name="Lệnh: ?q anime", value="Trích dẫn câu nói các nhân vật trong anime.", inline=False)
      embed.add_field(name="Lệnh: ?q book", value="Câu nói được trích từ sách.", inline=False)
      embed.add_field(name="Lệnh: ?q joke", value="Câu nói đùa kiểu Mỹ.", inline=False)
      await ctx.reply(embed=embed)

  def quoteEmbed(self, author,text,viText,type, book, image_url="None"):
    try:
      embed=discord.Embed(title="Random Quote", description=f"Thể loại: {type}", color=0x05f7f7)

      if(type=="book"):
        embed.add_field(name="Tác giả:", value=f"{author}", inline=True)
        embed.add_field(name="Tên sách:", value=f"{book}", inline=True)
        embed.set_thumbnail(url=image_url)
      if type == 'anime':
        embed.add_field(name="Nhân vật:", value=f"{author}", inline=True)
        embed.add_field(name="Anime:", value=f"{book}", inline=True)
        embed.set_thumbnail(url='https://i.redd.it/uxhmt1hivkw51.jpg')

      embed.add_field(name="Nội dung:", value=f"{text}", inline=False)
      embed.add_field(name="Dịch nghĩa:", value=f"{viText}", inline=False)
      return embed
    except Exception as e:
      print(e)
    
# ----setup------
def setup(bot):
  bot.add_cog(quotes(bot))
