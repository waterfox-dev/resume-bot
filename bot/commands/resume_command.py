from bot.commands.i_command import ICommand

from core.struct.message import Message
from core.struct.message_pool import MessagePool

from core.ai.analyzer import Analyzer

from core.utils.env_picker import pick_env_variable

from discord.interactions import Interaction
from discord.message import Message as DiscordMessage

class ResumeCommand(ICommand):
    
    async def execute(self, interaction: Interaction) -> None:
        await interaction.response.defer() 
        pool = await self._fetch_messages(interaction)
        analyzer = Analyzer(pool, pick_env_variable('OPEN_AI_TOKEN'))
        await interaction.followup.send(analyzer.analyze())  
        
    async def _fetch_messages(self, interaction: Interaction) -> MessagePool:
        """Fetch the last 50 messages in the channel"""
        
        pool = MessagePool()
        messages = interaction.channel.history(limit=50)
    
        async for message in messages:
            pool.add(Message(message.id, message.content, message.author.name, str(message.created_at)))
        
        return pool
