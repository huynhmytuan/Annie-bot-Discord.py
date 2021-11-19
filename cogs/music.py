from discord.ext import commands
import discord
import textwrap
import urllib
import aiohttp
import datetime
import os
from config import *

class music(commands.Cog):
  # CONTSTRANT VALUES GET FROM Secret Value
  def __init__(self, bot):
    self.bot = bot
    self.TOKEN = os.getenv('TOKEN')
    self.GUILD_ID = GUILD_ID
  
  @commands.command(aliases = ['l', 'lyrc', 'lyric']) 
  async def lyrics(self, ctx, *, search = None):
      """Tìm kiếm lời bài hát!"""
      if not search: # if user hasnt given an argument, throw a error and come out of the command
          embed = discord.Embed(
              title = "Thiếu từ khoá tìm kiếm!",
              description = "Bạn chưa nhập bất kì từ khoá nào, nên Annie không thể tìm lời được đâu!"
          )
          return await ctx.reply(embed = embed)
      
      song = urllib.parse.quote(search) # url-encode the song provided so it can be passed on to the API
      
      async with aiohttp.ClientSession() as lyricsSession:
          async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata: # define jsondata and fetch from API
              if not 300 > jsondata.status >= 200: # if an unexpected HTTP status code
                  return await ctx.send(f'Gặp vấn đề trong việc kết nối - Status Code:  {jsondata.status}')

              lyricsData = await jsondata.json() # load the json data into its json form

      error = lyricsData.get('error')
      if error: # checking if there is an error recieved by the API
          return await ctx.send(f'Gặp lỗi không xác định: {error}')

      songLyrics = lyricsData['lyrics'] # the lyrics
      songArtist = lyricsData['author'] # the author's name
      songTitle = lyricsData['title'] # the song's title
      songThumbnail = lyricsData['thumbnail']['genius'] # the song's picture/thumbnail
      for chunk in textwrap.wrap(songLyrics, 4096, replace_whitespace = False):
          embed = discord.Embed(
              title =  songTitle,
              description = f'***Tác Giả: {songArtist}***\n' + chunk,
              color = discord.Color.blurple(),
              timestamp = datetime.datetime.utcnow()
          )
          embed.set_thumbnail(url = songThumbnail)
          await ctx.channel.send(embed = embed)
# ----setup------
def setup(bot):
  bot.add_cog(music(bot))