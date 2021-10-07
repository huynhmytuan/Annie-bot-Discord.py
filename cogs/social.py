from discord.ext import commands
import discord
import os


class social(commands.Cog):
    # CONTSTRANT VALUES GET FROM Secret Value
    def __init__(self, bot):
        self.bot = bot
        self.TOKEN = os.getenv('TOKEN')
        self.GUILD_ID = int(os.getenv('GUILD_ID'))
        self.WELCOME_CHANNEL_ID = int(os.getenv('WELCOME_CHANNEL_ID'))
        self.GOODBYE_CHANNEL_ID = int(os.getenv('GOODBYE_CHANNEL_ID'))
        self.RULE_CHANNEL_ID = int(os.getenv('RULE_CHANNEL_ID'))
        #Guild and channels
        self.guild = self.bot.get_guild(self.GUILD_ID)
        self.welcome_channel = self.guild.get_channel(self.WELCOME_CHANNEL_ID) 
        self.rule_channel = self.guild.get_channel(self.RULE_CHANNEL_ID)
        self.goodbye_channel = self.guild.get_channel(self.GOODBYE_CHANNEL_ID)

    # Register an event
    # #-------------------WELCOME------------------------
    # # 1. Send message welcome in channel and inbox (Done)
    # # 2. Send Server Rule (Update later just send "This is rule")
    #ua khoan, Neu minh dem cai get channel ra ben ngoai
    #Thi moi lan ham nay chay dau can phai request channel
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

        help_text = ":bangbang: Lưu ý: hãy nhớ cập nhật bằng cách nhấp vào các biểu tượng của tin nhắn trong kênh ╔✅verify✅╗ để có thể thấy và tham gia vào các nội dung của server nhé.:catjam1: \nClick vào biểu tượng  :pencil:  để tham gia các hoạt động học tập và tài liệu \nClick vào biểu tượng  :video_game:  để giải trí (đọc sách, nghe nhạc, chơi game,...) \nClick vào biểu tượng :brain: để tham gia tất cả nội dung học tập và vui chơi.\n Nếu bạn đã xác minh và vẫn chưa thấy hoặc tham gia vào các kênh, hãy vui lòng nhắn vào #feedback-hỗ-trợ-nhận-role để được hỗ trợ."
        em=discord.Embed(title="HƯỚNG DẪN SỬ DỤNG", description=f"{help_text}", color=0x00ada2)
        em.set_image(url="https://lh3.googleusercontent.com/Vd3wd4QGpzy-OdCNb8Ubum15jgrTtMhc_E-1bVfHZ-SpOiEHdqEC-vcJlipvEehxBDoUQPwe9pFdyAnt7V43Jb-D9F60ydMe7vs94cnYXX2ExNYeKw7Qtm6bXIW393AmjmXIEOMu8iRXmiLJgd5vUB-TNgX4iJoJejihYve914L-AQF3G0qU789QiCE9vlekBCFi466P29teaqsHFXCqgUiFgABb0J2EmD2BjNxnwyJJl2Twbfq6w2K23QjWT9DIIwki7z5KtT0eoIadQt2HYwZqfxgSidoihAj6OvzpMI-zXKpe6gHFfCNPmddVn89FiWgsqLyQQtJ8tbXgRX7d5eXqd_3eb9UjqwguTtBzJ8HKbySG37CPEjZO3lZuo6SWiKCk4qul_Cdp7GpUogdakpmfiKy7reU7tI9rBzwyWd1lyGgv-WSbYXi5CEGTfyf1qzYBsUREApPorCDQrmwsJiV4evePJZc3EiPtyxm7m2g184rCfaPd6B0xg8JIt_PLroEhq-VovHO0mWxWX2Kt2uT-_cY92pHE7WS-Ck6IgwUG16Z0fAXtTnyBX2EuETiGQ0vDzG49ZSEDX71Jitkhgt1P7ZS4cpOewDRkpcCZbmA_SDbzVPKjZTbOnn7LSoYbWVR5kgwH1VCSL0bnXgZwjD5Aohmqu71zXbeZoZ6wbYWlBbXuk1oasuEnoTABCVtX1CvyJZ2H9D6_jCNoIV_9_oHx=w1322-h342-no?authuser=0")
        await member.send(
            f'Chào mừng đến {self.guild.name} , rất vui được {member.name} gia nhập! :partying_face:\nCùng nhau xây dựng một cộng đồng vui chơi và học tập lớn mạnh nhé! '
        )
        await member.send(embed=em)

    # -------------------Goodbye-----------------------
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # Goodbye the  member in the goodbye-my-love channel
        await self.goodbye_channel.send(
            f'Tạm biệt {member.mention}, một người nữa lại bỏ Annie đi... :pleading_face: '
        )


# ----setup------
def setup(bot):
    bot.add_cog(social(bot))
