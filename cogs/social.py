from discord.ext import commands
import discord
import os
from config import *

class social(commands.Cog):
    # CONTSTRANT VALUES GET FROM Secret Value
    def __init__(self, bot):
        self.bot = bot
        self.TOKEN = os.getenv('TOKEN')
        self.GUILD_ID = GUILD_ID
        self.WELCOME_CHANNEL_ID = WELCOME_CHANNEL_ID
        self.GOODBYE_CHANNEL_ID = GOODBYE_CHANNEL_ID
        self.RULE_CHANNEL_ID = RULE_CHANNEL_ID
        #Guild and channels
        self.guild = self.bot.get_guild(self.GUILD_ID)
        self.welcome_channel = self.guild.get_channel(self.WELCOME_CHANNEL_ID) 
        self.rule_channel = self.guild.get_channel(self.RULE_CHANNEL_ID)
        self.goodbye_channel = self.guild.get_channel(self.GOODBYE_CHANNEL_ID)

    # Register an event
    # #-------------------WELCOME------------------------
    # # 1. Send message welcome in channel and inbox (Done)
    # # 2. Send Server Rule (Update later just send "This is rule")
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Welcome the new member in the welcome channel
        await self.welcome_channel.send(
            f'Chào mừng {member.mention} đến với Cộng đồng học tập {self.guild.name}! :partying_face: :v: \nGhé qua kênh {self.rule_channel.mention} để đọc luật nhé!'
        )
        embed = discord.Embed(
            title=f"Chào mừng {member.name} ",
            description=
            f"Cảm ơn đã tham gia {self.guild.name}! :partying_face: :v:")
        embed.set_thumbnail(url=member.avatar_url)
        await self.welcome_channel.send(embed=embed)

        await member.send(
            f'Chào mừng đến {self.guild.name} , rất vui được {member.name} gia nhập! :partying_face:\nCùng nhau xây dựng một cộng đồng vui chơi và học tập lớn mạnh nha!'
        )

    # -------------------Goodbye-----------------------
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # Goodbye the  member in the goodbye-my-love channel
        await self.goodbye_channel.send(
            f'{member.mention} đã rời đi :pleading_face: '
        )


# ----setup------
def setup(bot):
    bot.add_cog(social(bot))
