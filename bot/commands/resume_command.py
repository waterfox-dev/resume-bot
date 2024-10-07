from bot.commands.i_command import ICommand

from core.struct.message import Message
from core.struct.message_pool import MessagePool
from core.struct.answer import Answer

from core.database.answer_recorder import AnswerRecorder

from core.ai.analyzer import Analyzer

from core.utils.env_picker import pick_env_variable

from discord.interactions import Interaction

class ResumeCommand(ICommand):
    
    async def execute(self, interaction: Interaction) -> None:
        await interaction.response.defer() 
        pool = await self._fetch_messages(interaction)
        analyzer = Analyzer(pool, pick_env_variable('OPEN_AI_TOKEN'))
        response = analyzer.analyze()
        await interaction.followup.send(response)  
        await self._save_to_database(pool, interaction, response)
        
    async def _fetch_messages(self, interaction: Interaction) -> MessagePool:
        """Fetch the last 50 messages in the channel"""
        
        pool = MessagePool()
        messages = interaction.channel.history(limit=50)
    
        async for message in messages:
            pool.add(Message(message.id, message.content, message.author.name, str(message.created_at)))
        
        return pool

    async def _save_to_database(self, pool: MessagePool, interaction: Interaction, response: str) -> None:
        """Save the messages to the database"""
        answer: Answer = Answer()
        answer['id'] = interaction.id 
        answer['json_messages'] = pool.to_json()
        answer['response'] = response
        answer['caller_id'] = interaction.user.id
        answer['date'] = str(interaction.created_at)
        AnswerRecorder().record(answer)