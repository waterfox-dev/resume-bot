from discord import Intents
from discord.client import Client
from discord.ext import commands
from discord.app_commands import CommandTree 
from discord.object import Object
from discord.interactions import Interaction

from bot.commands.ping_command import PingCommand
from bot.commands.resume_command import ResumeCommand
from bot.commands.info_command import InfoCommand

from core.utils.env_picker import pick_env_variable
from core.utils.env_picker import load_env_file_in_memory


BOT_INTENTS = Intents.default() 
BOT_CLIENT = Client(intents=BOT_INTENTS)
BOT_TREE = CommandTree(BOT_CLIENT) 

TEST_GUILD_ID = 1043261099555962970

@BOT_TREE.command(name="ping", description="Ping Resume Bot, responds with 'Pong!'", guild=Object(id=TEST_GUILD_ID))
async def ping_command(interaction: Interaction):
    await PingCommand().execute(interaction)

@BOT_TREE.command(name="resume", description="Resume the conversation", guild=Object(id=TEST_GUILD_ID))
async def resume_command(interaction: Interaction):
    await ResumeCommand().execute(interaction)
    
@BOT_TREE.command(name="info", description="Get information about Resume Bot", guild=Object(id=TEST_GUILD_ID))
async def info_command(interaction: Interaction):
    await InfoCommand().execute(interaction)

@BOT_CLIENT.event
async def on_ready():
    guild = BOT_CLIENT.get_guild(TEST_GUILD_ID)
    await BOT_TREE.sync(guild=guild)

def main(): 
    load_env_file_in_memory('.env')
    BOT_CLIENT.run(pick_env_variable('DISCORD_TOKEN'))