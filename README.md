# PDFConvo-LLM-RAG

# Table of Contents
- [First Time Setup](#first-time-setup)
- [Chat Module Explanation](#chat-module)

# First Time Setup

## Using Pipenv [Recommended]

```
# Install dependencies
pipenv install

# Create a virtual environment
pipenv shell

# Initialize the database
flask --app app.web init-db

```

## Using Venv [Optional]

These instructions are included if you wish to use venv to manage your evironment and dependencies instead of Pipenv.

```
# Create the venv virtual environment
python -m venv .venv

# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
flask --app app.web init-db
```

# Running the app [Pipenv]

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
flask --app app.web init-db
```

# Running the app [Venv]

_These instructions are included if you wish to use venv to manage your evironment and dependencies instead of Pipenv._

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
flask --app app.web init-db
```



# Chat Module 

This repository contains a module named "chat" designed for chat-based applications. The module encompasses various functionalities including conversation retrieval, language modeling, memory management, and more. Below is a detailed overview of the directory structure and the functionality provided by each component within the module.

## Directory Structure

```
chat/
├── callbacks/
│   ├── __init__.py
│   └── stream.py
├── chains/
│   ├── __init__.py
│   ├── retrieval.py
│   ├── streamable.py
│   └── traceable.py
├── chat.py
├── create_embeddings.py
├── embeddings/
│   ├── __init__.py
│   └── openai.py
├── __init__.py
├── llms/
│   ├── chatopenai.py
│   └── __init__.py
├── memories/
│   ├── histories/
│   │   ├── __init__.py
│   │   └── sql_history.py
│   ├── __init__.py
│   ├── sql_memory.py
│   └── window_memory.py
├── models/
│   └── __init__.py
├── score.py
├── test_env.py
├── tracing/
│   └── langfuse.py
└── vector_stores/
    ├── __init__.py
    └── pinecone.py
```

## Components Overview

### 1. `callbacks/`
This directory contains callback handlers used in the chat module.

- **stream.py**: Defines a custom callback handler `StreamingHandler` for handling streaming in chat applications.

### 2. `chains/`
This directory contains classes representing various chains used in the chat module.

- **retrieval.py**: Defines a class `StreamingConversationalRetrievalChain` for conversational retrieval.
- **streamable.py**: Defines a class `StreamableChain` for handling streaming data.
- **traceable.py**: Defines a class `TraceableChain` for tracing data flow through a chain.

### 3. `chat.py`
Defines a function `build_chat()` for constructing a conversational retrieval chain for chat-based applications.

### 4. `create_embeddings.py`
Defines a function `create_embeddings_for_pdf()` for generating and storing embeddings for a given PDF document.

### 5. `embeddings/`
This directory contains modules related to embeddings.

- **openai.py**: Defines functions related to OpenAI embeddings.

### 6. `llms/`
This directory contains modules related to Language Models (LLMs).

- **chatopenai.py**: Defines a function `build_llm()` for constructing an LLM instance.

### 7. `memories/`
This directory contains modules related to memory management.

- **histories/**
  - **sql_history.py**: Defines a class `SqlMessageHistory` for storing message history in an SQL database.

- **sql_memory.py**: Defines a function `build_memory()` for constructing a memory component.

- **window_memory.py**: Defines a function `window_buffer_memory_builder()` for constructing a windowed memory component.

### 8. `models/`
This directory contains modules related to machine learning models.

### 9. `tracing/`
This directory contains modules related to tracing data flow.

- **langfuse.py**: Defines functionalities for tracing data flow.

### 10. `vector_stores/`
This directory contains modules related to vector stores.

- **pinecone.py**: Defines functionalities for handling vector storage using Pinecone.

## Component Functionality Details

### 1. `callbacks/stream.py`

#### StreamingHandler
- Defines a custom callback handler `StreamingHandler`.
- Inherits from `BaseCallbackHandler`.
- Provides methods for handling streaming callbacks:
  - `on_chat_model_start()`: Handles the start of chat model execution.
  - `on_llm_new_token()`: Handles the generation of a new token by the language model.
  - `on_llm_end()`: Handles the end of language model execution.
  - `on_llm()`: Handles errors that occur during language model execution.

### 2. `chains/`

#### retrieval.py
- Defines a class `StreamingConversationalRetrievalChain`.
- Inherits functionality from multiple parent classes.
- Imports necessary modules for a conversational retrieval chain.
- Provides capabilities for processing user queries and retrieving relevant information.

#### streamable.py
- Defines a class `StreamableChain`.
- Provides functionality for handling streaming data in a chat application.
- Uses Flask for accessing the current application context.
- Implements methods for streaming data through the chain asynchronously using threads.

#### traceable.py
- Defines a class `TraceableChain`.
- Provides functionality for tracing the flow of data through a chat application chain.
- Integrates with a custom tracing module to facilitate data flow tracing.
- Overrides the `__call__()` method to intercept calls to instances of `TraceableChain`.

### 3. `chat.py`

#### build_chat()
- Constructs a conversational retrieval chain for chat-based applications.
- Takes a `ChatArgs` object as input, containing parameters such as conversation ID, PDF ID, metadata, and a streaming flag.
- Initializes components such as retriever, language model, memory, and condense question LLM.
- Returns a `StreamingConversationalRetrievalChain` encapsulating the conversational retrieval logic.

### 4. `create_embeddings.py`

#### create_embeddings_for_pdf()
- Generates and stores embeddings for a given PDF document.
- Imports necessary modules including `PyPDFLoader` for loading the PDF, `RecursiveCharacterTextSplitter` for splitting text, and `vector_store` for storing embeddings.
- Initializes a text splitter and loads/splits text content of the PDF.
- Creates metadata for each section of text.
- Adds documents to the vector store for embedding generation.

### 5. `embeddings/openai.py`
- Defines functions related to OpenAI embeddings.

### 6. `llms/`

#### chatopenai.py
- Constructs an LLM instance for a chat application.
- Initializes a `ChatOpenAI` instance configured with parameters such as verbosity and streaming mode.
- Returns the constructed LLM instance.

### 7. `memories/`

#### histories/sql_history.py
- Defines a class `SqlMessageHistory` for storing message history in an SQL database.
- Provides methods for retrieving and adding messages to the conversation.

#### sql_memory.py
- Constructs a memory component for a chat application.
- Initializes a `ConversationBufferMemory` object configured with an SQL-based message history.

#### window_memory.py
- Constructs a memory component for a chat application with windowed conversation history.
- Initializes a `ConversationBufferWindowMemory` object configured with an SQL-based message history and a conversation window size.




## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to explore the repository and contribute to its development! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request. Thank you for your interest in our interactive chat system!

