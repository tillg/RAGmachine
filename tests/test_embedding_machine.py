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


class TestEmbeddingMachine(unittest.TestCase):

    EMBEDDINGS_DATA_PATH = os.environ.get(
        'EMBEDDINGS_TEST_DATA_PATH', "data/tmp/vectorDB")
    EMBEDDINGS_COLLECTION = "whatever_collection"

    # def setUp(self):
    #     if os.path.exists(self.EMBEDDINGS_DATA_PATH):
    #         shutil.rmtree(self.EMBEDDINGS_DATA_PATH)

    def test_add_documents(self):
        logger = get_logger("test_add_documents", logging.INFO)
        fake = Faker()
        chunk_machine = ChunkMachine(
            separator="\n", chunk_size=1000, chunk_overlap=3)
        documents = [Document(' '.join(fake.text()
                                       for _ in range(13))) for _ in range(100)]
        em = EmbeddingMachine(data_path=self.EMBEDDINGS_DATA_PATH,
                              collection=self.EMBEDDINGS_COLLECTION, chunk_machine=chunk_machine)
        pre_count = em.count()
        em.add_documents(documents)
        post_count = em.count()
        logger.info(f"Pre count: {pre_count}, Post count: {post_count}")

    def test_add_document_with_odyssey(self):
        logger = get_logger("test_add_document_with_odyssey", logging.INFO)
        loader = WebBaseLoader("https://www.gutenberg.org/files/1727/1727-h/1727-h.htm")
        data = loader.load()
        #logger.info(f"Data: {data}")


if __name__ == '__main__':
    unittest.main()
