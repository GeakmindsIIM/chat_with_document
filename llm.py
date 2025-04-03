import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LLMResponseGenerator:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-02-15-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

    def generate_response(self, query, search_results):
        """Generate AI response using the search results as context."""
        try:
            # Prepare context from search results
            context = "\n".join([
                f"Title: {result.get('title', 'No title')}\nContent: {result.get('chunk', '')}" 
                for result in search_results
            ])
            
            # Create system and user messages with strict instructions
            messages = [
                {
                    "role": "system", 
                    "content": """You are an AI assistant that ONLY provides information found in the given document context.
                    Follow these rules strictly:
                    1. ONLY use information that is explicitly stated in the provided context.
                    2. If the information is not in the context, say 'I don't have enough information in the documents to answer that question.'
                    3. DO NOT make assumptions or provide information from outside the given context.
                    4. Keep responses focused and directly tied to the document content."""
                },
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
            ]
            
            # Generate response
            response = self.client.chat.completions.create(
                model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating response: {str(e)}")
            return None
