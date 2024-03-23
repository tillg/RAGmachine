import logging
import shutil
import unittest
from unittest.mock import MagicMock, patch
# from rag_machine.document import Document
from rag_machine.embedding_machine import EmbeddingMachine
from rag_machine.chunk_machine import ChunkMachine
import os
from faker import Faker
from langchain_community.document_loaders import WebBaseLoader
from rag_machine.utils.utils import get_logger
from langchain.docstore.document import Document
import uuid


class TestEmbeddingMachine(unittest.TestCase):

    EMBEDDINGS_DATA_PATH = os.environ.get(
        'EMBEDDINGS_TEST_DATA_PATH', "data/tmp/vectorDB")
    EMBEDDINGS_COLLECTION = "whatever_collection"

    @classmethod
    def setUpClass(cls):
        if os.path.exists(cls.EMBEDDINGS_DATA_PATH):
            shutil.rmtree(cls.EMBEDDINGS_DATA_PATH)
        chunk_machine = ChunkMachine(
            separator="\n", chunk_size=1000, chunk_overlap=3)
        cls.em = EmbeddingMachine(data_path=cls.EMBEDDINGS_DATA_PATH,
                                  collection=cls.EMBEDDINGS_COLLECTION, chunk_machine=chunk_machine)

    def test_add_documents(self):
        logger = get_logger("test_add_documents", logging.INFO)
        fake = Faker()
        documents = [Document(' '.join(fake.text()
                                       for _ in range(13))) for _ in range(100)]
        pre_count = self.em.count()
        self.em.add_documents(documents)
        post_count = self.em.count()
        logger.info(f"Pre count: {pre_count}, Post count: {post_count}")

    def test_add_document_with_odyssey(self):
        logger = get_logger("test_add_document_with_odyssey", logging.INFO)
        loader = WebBaseLoader(
            "https://www.gutenberg.org/files/1727/1727-h/1727-h.htm")
        documents = loader.load()
        # document = Document(page_content=data, metadata={"id": "odyssey"})
        document = documents[0]
        pre_count = self.em.count()
        self.em.add_documents(documents)
        post_count = self.em.count()
        logger.info(f"Pre count: {pre_count}, Post count: {post_count}")

    def test_add_and_get_document(self):
        logger = get_logger("test_add_and_get_document", logging.INFO)
        id = "the very special ID"
        metadata = {"id": id, "key": "value"}
        document = Document(page_content="lorem ipsum", metadata=metadata)
        self.em.add_documents([document])

        retrieved_documents = self.em.get_by_id([id])
        logger.info(f"Retrieved documents: {retrieved_documents}")

        self.assertEqual(len(retrieved_documents), 1)
        retrieved_document = retrieved_documents[0]
        self.assertEqual(retrieved_document.page_content,
                         document.page_content)
        self.assertEqual(retrieved_document.metadata, document.metadata)


if __name__ == '__main__':
    unittest.main()
