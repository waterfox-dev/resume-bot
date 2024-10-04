from core.ai.analyzer import Analyzer

from core.struct.message_pool import MessagePool
from core.struct.message import Message

from core.utils.env_picker import pick_env_variable
from core.utils.env_picker import load_env_file_in_memory

load_env_file_in_memory(".env")

import json 

message_pool = MessagePool()

with open("data/mock.json", "r") as file :
    messages = json.load(file)
    for message in messages :
        message_pool.add(Message(**message))

analyzer = Analyzer(message_pool, pick_env_variable("OPEN_AI_KEY"))
print(analyzer.analyze())