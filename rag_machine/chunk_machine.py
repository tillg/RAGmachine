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

    def ensure_id_in_document(self, document: Document) -> Document:
        if document.metadata is None:
            document.metadata = {}
        if "id" not in document.metadata:
            document.metadata["id"] = str(uuid.uuid4())
        return document

    def overwrite_id_in_document(self, document: Document) -> Document:
        if document.metadata is None:
            document.metadata = {}
        document.metadata["id"] = str(uuid.uuid4())
        return document

    def chunkify_document(self, document: Document) -> List[Document]:
        logger = get_logger("ChunkMachine.chunkify_document", logging.ERROR)
        if not isinstance(document, Document):
            logger.error(
                f"Document is not an instance of Document: {document}. It is of type {type(document)}")
            raise TypeError("document must be an instance of Document")
        
        try:
            chunks = self.text_splitter.create_documents(
                [document.page_content], metadatas=[document.metadata])
        except Exception as e:
            logger.error(
                f"Error while chunkifying document: {robust_jsonify(document)}")
            logger.error(f"Error: {e}")
            raise
        for chunk in chunks:
            chunk = self.overwrite_id_in_document(chunk)
            if "id" in document.metadata:
                chunk.metadata["original_document_id"] = document.metadata["id"]
        logger.debug(f"Chunkified in chunks of length: {
                        [len(chunk.page_content) for chunk in chunks]}")
        return chunks

    def chunkify_documents(self, documents: List[Document]) -> List[Document]:
        logger = get_logger("ChunkMachine.chunkify_documents", logging.ERROR)
        if not isinstance(documents, list):
            logger.error(
                f"documents is not a list: {documents}. It is of type {type(documents)}")
            raise TypeError(f"documents must be a list, not {type(documents)}")
        if not all(isinstance(doc, Document) for doc in documents):
            logger.error(
                f"All elements in list are not instances of Document.")
            raise TypeError("All elements in documents must be instances of Document")

        #chunks = [self.chunkify_document(document) for document in documents]
        chunks = [chunk for document in documents for chunk in self.chunkify_document(document)]

        return chunks
