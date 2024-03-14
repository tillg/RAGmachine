from rag_machine.document import Document
from rag_machine.chunk import Chunk
from langchain.text_splitter import CharacterTextSplitter
from typing import List
from dotenv import load_dotenv
import logging
from rag_machine.utils.utils import get_logger
from rag_machine.utils.robust_jsonify import robust_jsonify
import os

load_dotenv()

CHUNK_MACHINE_SEPARATOR = os.environ.get('CHUNK_MACHINE_SEPARATOR', "\n\n")
CHUNK_MACHINE_CHUNK_SIZE = os.environ.get('CHUNK_MACHINE_CHUNK_SIZE', 256)
CHUNK_MACHINE_CHUNK_OVERLAP = os.environ.get('CHUNK_MACHINE_CHUNK_OVERLAP', 20)


class ChunkMachine:

    def __init__(self, separator: str = CHUNK_MACHINE_SEPARATOR, chunk_size: int = CHUNK_MACHINE_CHUNK_SIZE, chunk_overlap: int = CHUNK_MACHINE_CHUNK_OVERLAP):
        self.text_splitter = CharacterTextSplitter(
            separator=separator,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def chunkify_document(self, document: Document) -> List[Chunk]:
        logger = get_logger("ChunkMachine.chunkify_document", logging.WARNING)
        chunk_contents = self.text_splitter.create_documents(
            [document.content])
        chunks = [Chunk(document.id, content.page_content) for content in chunk_contents]
        logger.info(f"Chunkified document {document.id} chunks: {robust_jsonify(chunks)}")
        return chunks

    def chunkify_documents(self, documents: List[Document]) -> List[Chunk]:
        logger = get_logger("ChunkMachine.chunkify_documents", logging.INFO)
        chunks = []
        for document in documents:
            chunks += self.chunkify_document(document)
        return chunks