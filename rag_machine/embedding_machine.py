import os
import chromadb
from rag_machine.chunk_machine import ChunkMachine
from rag_machine.utils.utils import get_logger, simplify_text
from rag_machine.utils.dict2file import write_dict_to_file, read_dict_from_file
import logging
from typing import List
from langchain.docstore.document import Document
from langchain.storage import LocalFileStore


class EmbeddingMachine:

    DATA_PATH = os.environ.get(
        'DATA_PATH', "data/ingested")

    @classmethod
    def _read_index_from_file(self, index_filename):
        logger = get_logger("_read_index_from_file", logging.INFO)
        logger.info(f"Reading index from file: {index_filename}")
        if os.path.exists(index_filename):
            return read_dict_from_file(index_filename)
        return {}

    def __init__(self, data_path: str = DATA_PATH, chunk_machine=None):
        logger = get_logger("EmbeddingMachine.__init__", logging.INFO)
        self.data_path = data_path
        self.chroma_path = os.path.join(self.data_path, "chroma")
        self.document_path = os.path.join(self.data_path, "documents")
        self.collection = "DEFAULT_COLLECTION"
        self.client = chromadb.PersistentClient(path=self.chroma_path)
        self.collection = self.client.get_or_create_collection(self.collection)
        self.document_index = self._read_index_from_file(os.path.join(self.data_path, "_index.json"))
        self.chunk_machine = chunk_machine
        if self.chunk_machine is None:
            self.chunk_machine = ChunkMachine()

        logger.info(f"EmbeddingMachine initialized. Data path: {
                    self.data_path}, collection size: {self.collection.count()}")

    def search_documents_by_text(self, query_text: str):
        return self.collection.query(query_texts=[query_text])

    def search_documents_by_texts(self, query_texts: List[str]):
        return self.collection.query(query_texts=query_texts)

    def __len__(self):
        return len(self.document_index)

    def _document_to_file(self, document: Document):
        logger = get_logger("_document_to_file", logging.INFO)
        # Check if the document has a source
        if not document.metadata.get("source"):
            logger.error(f"Document without source: {document}")
            return
        
        # Transform the source to a filename
        filename = os.path.join(self.document_path, simplify_text(document.metadata["source"]) + ".json")

        # Transform to dict
        document_dict = {"page_content": document.page_content, "metadata": document.metadata}

        # Write to file
        write_dict_to_file(dictionary=document_dict, full_filename=filename)
        return


    def _file_to_document(self, source: str):
        logger = get_logger("_file_to_document", logging.INFO)
        # Transform the source to a filename
        filename = os.path.join(self.document_path, simplify_text(source) + ".json")

        # Check if file exists
        if not os.path.exists(filename):
            logger.error(f"File does not exist: {filename}")
            return None
        
        # Read file
        document_dict = read_dict_from_file(full_filename=filename)

        # Build Document
        document = Document(page_content=document_dict["page_content"], metadata=document_dict["metadata"])
        return document
    
    def _write_index_to_file(self):
        logger = get_logger("_write_index_to_file", logging.INFO)
        filename = os.path.join(self.data_path, "_index.json")
        write_dict_to_file(dictionary=self.document_index, full_filename=filename)
        return
    
    def _add_document_to_index(self, document: Document):
        logger = get_logger("_add_document_to_index", logging.INFO)
        # Check that document has a source
        if not document.metadata.get("source"):
            logger.error(f"Document without source: {document}")
            return
        # Transform source to filename
        filename = os.path.join(simplify_text(document.metadata["source"]) + ".json")
        
        self.document_index[filename] = document.metadata
        self._write_index_to_file()

    def _add_document_to_store(self, document: Document):
        logger = get_logger("_add_document_to_store", logging.INFO)
        if not isinstance(document, Document):
            logger.error(
                f"document is not an instance of Document: {document}")
            raise TypeError(f"document must be an instance of Document, not {
                            type(document)}")

    def add_document(self, document: Document):
        logger = get_logger("EmbeddingMachine.add_document", logging.INFO)
        if not isinstance(document, Document):
            logger.error(
                f"document is not an instance of Document: {document}")
            raise TypeError(f"document must be an instance of Document, not {
                            type(document)}")

        # Add the document to the store
        self._document_to_file(document)

        # Add the documen to the index
        self._add_document_to_index(document)
        
        # Chunk the document
        chunks = self.chunk_machine.chunkify_document(document)

        # Store the chunks in the collection
        chunk_page_content = []
        for chunk in chunks:
            if not chunk.page_content:
                logger.error(f"Chunk without page_content: {chunk}")
            else:
                chunk_page_content.append(chunk.page_content)
        chunk_metadatas = [chunk.metadata for chunk in chunks]
        chunk_ids = [chunk.metadata['id'] for chunk in chunks]
        self.collection.add(documents=chunk_page_content,
                            metadatas=chunk_metadatas, ids=chunk_ids)
        return

    def add_documents(self, documents: List[Document]):
        logger = get_logger("EmbeddingMachine.add_documents", logging.INFO)
        if not isinstance(documents, list):
            logger.error(f"documents is not a list. It is of type {
                         type(documents)}")
            raise TypeError(f"documents must be a list, not {type(documents)}")
        if not all(isinstance(doc, Document) for doc in documents):
            logger.error(
                f"All elements in documents must be instances of Document")
            raise TypeError(
                "All elements in documents must be instances of Document")

        for document in documents:
            self.add_document(document)

        return
