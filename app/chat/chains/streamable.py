from flask import current_app

from app.chat.callbacks.stream import StreamingHandler
from queue import Queue
from threading import Thread


class StreamableChain:
    def stream(self,input): #Override the built-in stream function
       queue = Queue()
       handler = StreamingHandler(queue)
       
       def task(app_context):
          app_context.push() # adding the thread to the current app context of flask -- not langchain related
          self(input, callbacks=[handler])

       Thread(target=task, args=[current_app.app_context()]).start() # the arg is related to flask not langchain

       while True:
           token = queue.get()
           if token is None:
               break
           yield token 