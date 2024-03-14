import shutil
import unittest
from unittest.mock import MagicMock, patch
from rag_machine.document import Document
from rag_machine.embedding_machine import EmbeddingMachine
from rag_machine.chunk_machine import ChunkMachine
import os
from faker import Faker

class TestEmbeddingMachine(unittest.TestCase):

    EMBEDDINGS_DATA_PATH = os.environ.get(
        'EMBEDDINGS_TEST_DATA_PATH', "data/tmp/vectorDB")
    EMBEDDINGS_COLLECTION = "whatever_collection"

    def setUp(self):
        if os.path.exists(self.EMBEDDINGS_DATA_PATH):
            shutil.rmtree(self.EMBEDDINGS_DATA_PATH)

    def test_init(self):
        em = EmbeddingMachine(data_path=self.EMBEDDINGS_DATA_PATH,
                              collection=self.EMBEDDINGS_COLLECTION)
        self.assertEqual(em.data_path, self.EMBEDDINGS_DATA_PATH)
        self.assertEqual(em.collection.name, self.EMBEDDINGS_COLLECTION)

    def test_add_documents(self):
        fake = Faker()
        chunk_machine = ChunkMachine(separator="\n", chunk_size=10, chunk_overlap=3)
        documents = [Document(' '.join(fake.text()
                            for _ in range(13))) for _ in range(100)]
        em = EmbeddingMachine(data_path=self.EMBEDDINGS_DATA_PATH,
                            collection=self.EMBEDDINGS_COLLECTION, chunk_machine=chunk_machine)
        em.add_documents(documents)

if __name__ == '__main__':
    unittest.main()
