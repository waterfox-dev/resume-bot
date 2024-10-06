from abc import ABC
from abc import abstractmethod

from discord.interactions import Interaction

class ICommand(ABC):
    
    @abstractmethod
    async def execute(self, interaction: Interaction) -> None:
        pass
    
    