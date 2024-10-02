from core.ai.analyzer import Analyzer

from core.struct.message_pool import MessagePool

from core.struct.message import Message

import json 

message_pool = MessagePool()

with open("data/mock.json", "r") as file :
    messages = json.load(file)
    for message in messages :
        message_pool.add(Message(**message))

analyzer = Analyzer(message_pool, "KEY")
print(analyzer.analyze())