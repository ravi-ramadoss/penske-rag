import os
from langchain_community.document_loaders import RSSFeedLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


#get penske rss feed url
urls = ["https://www.gopenske.com/rss.xml"]

load_dotenv()
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")
PINECONE_API_KEY=os.environ.get("PINECONE_API_KEY")

#Load all the data from rss feed
loader = RSSFeedLoader(urls=urls)
data = loader.load()
print(f"Imported {len(data)} documents from RSS feed")

print('printing sample data from RSS feed')
print(data[0])
#split the data to store
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap  = 100,
    length_function = len,
    add_start_index = True,)
texts = text_splitter.split_documents(data)


pc = Pinecone(
    api_key=os.environ.get("PINECONE_API_KEY")
)


index_name = 'penske-rss'
# Now do stuff
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name, 
        dimension=1536, 
        metric='euclidean',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-west-2'
        )
    )

index = pc.Index(index_name)  
# print(index.describe_index_stats())

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY) # set openai_api_key = 'your_openai_api_key'
PineconeVectorStore.from_documents(texts, embeddings, index_name=index_name)