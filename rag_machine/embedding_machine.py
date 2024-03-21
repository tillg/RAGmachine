import os
import chromadb
from rag_machine.chunk_machine import ChunkMachine
from rag_machine.utils.utils import get_logger
import logging
from typing import List
# from rag_machine.document import Document
from langchain.docstore.document import Document


class EmbeddingMachine:

    EMBEDDINGS_DATA_PATH = os.environ.get(
        'EMBEDDINGS_DATA_PATH', "data/vectorDB")
    EMBEDDINGS_COLLECTION = os.environ.get(
        'EMBEDDINGS_COLLECTION', "default_collection")

    def __init__(self, data_path: str = EMBEDDINGS_DATA_PATH, collection: str = EMBEDDINGS_COLLECTION, chunk_machine=None):
        logger = get_logger("EmbeddingMachine.__init__", logging.INFO)
        self.data_path = data_path
        self.collection = collection
        self.client = chromadb.PersistentClient(path=self.data_path)
        self.collection = self.client.get_or_create_collection(self.collection)
        self.chunk_machine = chunk_machine
        if self.chunk_machine is None:
            self.chunk_machine = ChunkMachine()

        logger.info(f"EmbeddingMachine initialized. Data path: {
                    self.data_path}, collection size: {self.collection.count()}")

    def search_documents_by_text(self, query_text: str):
        return self.collection.query(query_texts=[query_text])

    def search_documents_by_texts(self, query_texts: List[str]):
        return self.collection.query(query_texts=query_texts)

    def count(self):
        return self.collection.count()

    def add_documents(self, documents: List[Document]):
        chunks = self.chunk_machine.chunkify_documents(documents)

        chunk_page_content = [chunk.page_content for chunk in chunks]
        chunk_metadatas = [chunk.metadata for chunk in chunks]
        chunk_ids = [chunk.metadata['id'] for chunk in chunks]

        self.collection.add(documents=chunk_page_content,
                            metadatas=chunk_metadatas, ids=chunk_ids)
