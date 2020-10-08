import discord
import asyncio 
from discord.ext import commands

class Etc (commands.Cog) :
   def __init__ (self, bot) :
      self.bot = bot
      self.normal_color = 0x61acf8

   @commands.command (name = '봇정보', aliases = ['정보', 'info'])
   async def info (self, ctx) :
      embed = discord.Embed (
         title = '봇 정보',
         description = '라디오 봇 정보입니다.',
         color = self.normal_color
      )
      embed.add_field (
         name = '작성 언어',
         value = 'Python',
         inline = True
      )
      embed.add_field (
         name = '봇 제작자',
         value = 'WHAT ARE YOU?',
         inline = True
      )
      embed.add_field (
         name = '초대 링크',
         value = '[클릭](https://discordapp.com/api/oauth2/authorize?client_id=761098054510051349&permissions=8&scope=bot)',
         inline = True
      )
      embed.add_field (
         name = '봇 핑',
         value = f'{round(self.bot.latency * 1000)}ms',
         inline = True
      )
      embed.set_thumbnail (url = self.bot.user.avatar_url)
      await ctx.send (embed = embed)
   
   @commands.command (name = '핑', aliases = ['봇핑', 'ping'])
   async def ping (self, ctx) :
      embed = discord.Embed (
         title = 'Pong!',
         description = f'Websocket : {round(self.bot.latency * 1000)}ms',
         color = self.normal_color
      )
      await ctx.send (embed = embed)
   
def setup (bot) :
   bot.add_cog(Etc(bot))