from bot.commands.i_command import ICommand

from discord.interactions import Interaction
from discord.embeds import Embed

class InfoCommand(ICommand):
    
    async def execute(self, interaction: Interaction) -> None:
        
        embed = Embed(title="Resume Bot", description="Resume Bot is a Discord bot that uses OpenAI's GPT-4o Mini to resume conversations", color=0x00ff00)
        embed.add_field(name="Current pool strategy", value="Resume Bot currently fetches the last 50 messages in the channel", inline=False)
        embed.add_field(name="Current AI model", value="Resume Bot uses OpenAI's GPT-4o Mini", inline=False)
        embed.add_field(name="Current AI model temperature", value="Resume Bot uses a temperature of 0.7", inline=False)
        await interaction.response.send_message(embed=embed)