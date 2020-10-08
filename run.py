import discord
import asyncio
from discord.ext import commands
from config import token
from config import EXTENSIONS

class ProjectPL (commands.Bot) : 
    def __init__ (self) :
        super().__init__ (
            command_prefix=["sim!"]
        )
        self.remove_command("help")

        for i in EXTENSIONS :
            self.load_extension (i)
    
    async def on_ready (self) :
        print ('Python Lavalink Project On.')
        print ('Username : ' + self.user.name)
    
    async def on_message (self, message) :
        if message.author.bot :
            return
        else :
            await self.process_commands (message)

bot = ProjectPL ()
bot.run (token, bot=True)

