# Import libraries
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
import os

# Ollama
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.embeddings import OllamaEmbeddings
from langchain.prompts import PromptTemplate
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader

