import discord
from discord.utils import get
from discord.ext import commands
from gtts import gTTS, langs
from googletrans import Translator
from helper.badword import checkBadWords
class Speach(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  def is_connected(self, ctx):
    voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()
  @commands.command()
  async def join(self,ctx):
    member = ctx.message.author
    await ctx.channel.purge(limit=1)
    if not member.voice:
      await ctx.send("Bạn phải ở trong kênh thoại.")
      return
    channel = member.voice.channel
    await channel.connect()
    await ctx.send("Đã kết nối.")
  #Leave
  @commands.command()
  async def leave(self,ctx):
    await ctx.channel.purge(limit=1)
    await ctx.voice_client.disconnect()
    await ctx.send("Đã thoát kênh thoại")

  @commands.command()
  async def say(self, ctx, *name : str):
    
    guild = ctx.guild
    if not Speach.is_connected(self, ctx):
      await ctx.send("Tôi phải ở trong kênh thoại thì mới nói được chứ!")
      return
    final_words = ''
    for c in " ".join(name):
      final_words += c;
    check_mess = checkBadWords(final_words)
    if check_mess == True:
      return
    else:
      translator = Translator()
      lang = translator.detect(final_words).lang
      support_langs = langs._main_langs()
      if not lang in support_langs:
        lang = 'vi'
      tts = gTTS(final_words, lang=lang)
      tts.save('hello.mp3')
      voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
      audio_source = discord.FFmpegPCMAudio('hello.mp3')
      if not voice_client.is_connected():
        voice_client.connect()
      if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)
        if isinstance(check_mess, str):
          await ctx.send('Đang nói... (Chú ý đừng dùng từ thô lỗ nhé!)')
        else:
          await ctx.reply('Đang nói....')
        


def setup(bot):
  bot.add_cog(Speach(bot))

