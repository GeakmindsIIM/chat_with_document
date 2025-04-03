import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AISearch:
    def __init__(self):
        self.search_client = SearchClient(
            endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
            index_name=os.getenv("AZURE_SEARCH_INDEX_NAME"),
            credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
        )

    def hybrid_search(self, query, embedding):
        """Perform hybrid search using Azure Cognitive Search."""
        try:
            vector_query = VectorizedQuery(
                vector=embedding,
                k_nearest_neighbors=3,
                fields="text_vector"
            )
            
            results = self.search_client.search(
                search_text=query,
                vector_queries=[vector_query],
                select=["chunk", "title"],
                top=3
            )
            return list(results)
        except Exception as e:
            print(f"Error performing search: {str(e)}")
            return []
