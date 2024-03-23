import logging
import unittest
from rag_machine.chunk_machine import ChunkMachine
from rag_machine.utils.utils import get_logger
from langchain.docstore.document import Document

class TestChunkMachine(unittest.TestCase):

    def setUp(self):
        self.chunk_machine = ChunkMachine(chunk_size=100, separator=" ", chunk_overlap=3 )
        self.document = Document(page_content="""This is a really long text that spans across multiple lines.
You can write as much as you want here.
Just keep in mind that line breaks in the string will be preserved.
This is the end of the long text.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis accumsan enim sit amet nulla euismod malesuada. Phasellus vel feugiat tellus, id vehicula felis. Mauris fringilla porttitor ante sed viverra. Aliquam id nibh eu urna vestibulum vehicula. Nulla sit amet facilisis metus. Pellentesque hendrerit finibus quam sit amet fringilla. Mauris nulla nisi, dapibus sit amet nisl non, accumsan posuere lorem. Integer tempor magna nibh, sit amet viverra sapien interdum vitae. Pellentesque nec pretium nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec et fringilla lacus. Mauris pretium nibh quis lorem blandit cursus.

Suspendisse sit amet viverra est. Duis id enim at dui lobortis efficitur. Sed ut ex et mauris malesuada vestibulum id vel odio. Mauris vel nulla lacus. Ut et ornare enim. Phasellus venenatis congue odio, ac volutpat nisi viverra et. Suspendisse elementum non elit eget porttitor. Mauris elit arcu, consequat id tellus eget, lobortis iaculis erat. Vivamus efficitur maximus arcu, a pharetra enim sollicitudin vel. Donec eget orci neque. In tristique odio et augue faucibus, eget commodo velit hendrerit. Cras cursus lectus in dolor interdum, quis condimentum nisi mollis. Nam sit amet lacus at magna euismod tristique. Nulla et justo elementum, volutpat purus at, euismod eros. Praesent iaculis interdum orci, vestibulum varius sem semper vel.

Morbi pretium mauris gravida, viverra enim quis, eleifend erat. In viverra neque lorem, et elementum nisi tristique nec. Sed lobortis ac velit at consequat. Ut sed mauris massa. Nulla mollis velit et ipsum auctor, id facilisis turpis pulvinar. Nulla non elit quis enim condimentum dictum at at purus. Morbi neque sapien, feugiat vitae diam nec, pulvinar tristique purus.                                 
                                 """)

    def test_chunkify(self):
        logger = get_logger("test_chunkify", logging.INFO)
        metadata = {
            "source": "example.com",
            "category": "news",
            "date": "2023-05-01"
        }
        test_doc = Document(page_content=self.document.page_content, metadata=metadata)
        chunks = self.chunk_machine.chunkify_document(test_doc)
        self.assertIsInstance(chunks, list)
        self.assertTrue(all(isinstance(chunk, Document) for chunk in chunks))
        for chunk in chunks:
            logger.info(f"Chunk content: {chunk.page_content}")

    def test_chunkify_document(self):
            chunks = self.chunk_machine.chunkify_document(self.document)
            self.assertIsInstance(chunks, list)
            for chunk in chunks:
                self.assertIsInstance(chunk, Document)

    def test_chunkify_documents(self):
        documents = [self.document] * 5  # Initialize a list of Document instances as needed
        chunks = self.chunk_machine.chunkify_documents(documents)
        self.assertIsInstance(chunks, list)
        for chunk in chunks:
            self.assertIsInstance(chunk, Document)

    def test_metadata_preservation_and_id_overwrite(self):
        metadata = {"key": "value",
                             "id": "original_id"}  
        document = Document(page_content=self.document.page_content, metadata=metadata)  
        chunks = self.chunk_machine.chunkify_document(document)
        for chunk in chunks:
            # Check that all original metadata entries are preserved
            for key, value in document.metadata.items():
                if key != "id":
                    self.assertEqual(chunk.metadata[key], value)
            # Check that the original id is reflected as original_document_id in the chunks
            self.assertEqual(
                chunk.metadata["original_document_id"], document.metadata["id"])
            # Check that the id is overwritten
            self.assertNotEqual(chunk.metadata["id"], document.metadata["id"])

    def test_chunkify_empty_document(self):
        document = Document(page_content="")  
        chunks = self.chunk_machine.chunkify_document(document)
        self.assertEqual(len(chunks), 0)

if __name__ == '__main__':
    unittest.main()
