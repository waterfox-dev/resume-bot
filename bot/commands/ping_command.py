from bot.commands.i_command import ICommand

from discord.interactions import Interaction

class PingCommand(ICommand):
    
    async def execute(self, interaction: Interaction) -> None:
        await interaction.response.send_message("Pong!")