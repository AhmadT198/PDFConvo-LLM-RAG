from langchain.chat_models import ChatOpenAI
# import langchain
# langchain.debug = True
def build_llm(chat_args):

    return ChatOpenAI(
        verbose=True,
        streaming=chat_args.streaming
    )