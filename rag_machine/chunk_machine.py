from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from typing import List
from dotenv import load_dotenv
import logging
from rag_machine.utils.utils import get_logger
from rag_machine.utils.robust_jsonify import robust_jsonify
import os
import uuid

load_dotenv()

CHUNK_MACHINE_SEPARATOR = os.environ.get('CHUNK_MACHINE_SEPARATOR', "\n\n")
CHUNK_MACHINE_CHUNK_SIZE = os.environ.get('CHUNK_MACHINE_CHUNK_SIZE', 256)
CHUNK_MACHINE_CHUNK_OVERLAP = os.environ.get('CHUNK_MACHINE_CHUNK_OVERLAP', 20)


class ChunkMachine:

    def __init__(self, separator: str = CHUNK_MACHINE_SEPARATOR, chunk_size: int = CHUNK_MACHINE_CHUNK_SIZE, chunk_overlap: int = CHUNK_MACHINE_CHUNK_OVERLAP):
        logger = get_logger("ChunkMachine.__init__", logging.INFO)
        logger.info(f"ChunkMachine initialized with separator: {
                    separator}, chunk_size: {chunk_size}, chunk_overlap: {chunk_overlap}")
        self.text_splitter = CharacterTextSplitter(
            separator=separator,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )

    def chunkify_document(self, document: Document) -> List[Document]:
        my_logger = get_logger("ChunkMachine.chunkify_document", logging.ERROR)
        chunks = self.text_splitter.create_documents(
            [document.page_content], metadatas=[document.metadata])
        for chunk in chunks:
            if chunk.metadata is None:
                chunk.metadata = {}
            chunk.metadata["id"] = str(uuid.uuid4())
            if "id" in document.metadata:
                chunk.metadata["original_document_id"] = document.metadata["id"]
        my_logger.debug(f"Chunkified in chunks of length: {
                        [len(chunk.page_content) for chunk in chunks]}")
        return chunks

    def chunkify_documents(self, documents: List[Document]) -> List[Document]:
        logger = get_logger("ChunkMachine.chunkify_documents", logging.ERROR)
        chunks = []
        for document in documents:
            chunks += self.chunkify_document(document)
        return chunks
