# Import libraries
import logging
import os
import argparse


from dotenv import load_dotenv

from langchain_community.document_loaders import DirectoryLoader

from rag_machine.utils.utils import get_logger
from rag_machine.embedding_machine import EmbeddingMachine
from rag_machine.chunk_machine import ChunkMachine

load_dotenv()

def ingest(directory):
    logger = get_logger("ingest", logging.INFO)
    loader = DirectoryLoader(directory, glob="**/*.md", show_progress=True)
    em = EmbeddingMachine()
    docs = loader.load()
    logger.info(f"Loaded {len(docs)} documents")
    em.add_documents(docs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest data into the embedding machine.')
    parser.add_argument('--dir', default=os.environ.get('DIRECTORY_TO_INGEST', "data/knowledge/ingest"),
                        help='The directory with the data to be ingested. Default: data/knowledge/ingest')

    args = parser.parse_args()

    ingest(args.dir)
