from pydantic import BaseModel
from langchain.schema import BaseChatMessageHistory


from app.web.api import (
    get_messages_by_conversation_id,
    add_message_to_conversation
)



class SqlMessageHistory(BaseChatMessageHistory, BaseModel):
    conversation_id: str

    @property
    def messages(self):
        #Gets all the messages of the conversation from db -- check the function implementation
        return get_messages_by_conversation_id(self.conversation_id)

    def add_message(self, message):
        #Add the messages to the db -- check the implementation
        return add_message_to_conversation(
            conversation_id=self.conversation_id,
            role=message.type,
            content=message.content
        )
    

    def clear(self):
        pass
