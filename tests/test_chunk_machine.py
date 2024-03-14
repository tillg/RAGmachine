import logging
import unittest
from rag_machine.chunk import Chunk
from rag_machine.chunk_machine import ChunkMachine
from rag_machine.document import Document
from rag_machine.utils.utils import get_logger

class TestChunkMachine(unittest.TestCase):

    def setUp(self):
        self.chunk_machine = ChunkMachine(chunk_size=10, separator="\n", chunk_overlap=3 )
        self.document = Document("""This is a really long text that spans across multiple lines.
You can write as much as you want here.
Just keep in mind that line breaks in the string will be preserved.
This is the end of the long text.""")

    def test_chunkify(self):
        logger = get_logger("test_chunkify", logging.INFO)
        chunks = self.chunk_machine.chunkify_document(self.document)
        self.assertIsInstance(chunks, list)
        self.assertTrue(all(isinstance(chunk, Chunk) for chunk in chunks))
        for chunk in chunks:
            logger.info(f"Chunk ID: {chunk.id}, Chunk content: {chunk.content}")


if __name__ == '__main__':
    unittest.main()
