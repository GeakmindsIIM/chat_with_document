# 📄 Chat with PDF using LLM and RAG

This application combines **Azure AI Search** (for retrieving relevant document chunks using both keyword-based and vector search) with **Azure OpenAI** (for generating responses based on the retrieved context). It enables users to chat with a PDF document using **Retrieval Augmented Generation (RAG).**

##  Features
-  Upload a PDF document  
-  Ask questions about the content of the PDF  
-  Get accurate answers using **RAG** and **Azure OpenAI models**  
-  Uses **Azure AI Search** for efficient indexing and retrieval  

##  How to Get Started?

### 1️⃣ Clone the GitHub Repository  
```sh
git clone https://github.com/GeakmindsIIM/chat_with_document.git
cd chat_with_document
```

### 2️⃣ Install the Required Dependencies  
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up Azure Services  
- Sign up for an **Azure OpenAI** account and obtain API keys.  
- Set up **Azure AI Search** and index your PDF documents.
#### Create an Azure AI Search Index:
- Go to **Azure Portal** and open your **Azure AI Search** instance.
- Click on **Overview** → **Import and vectorize data**.  
    
##### Step 1: Vectorize your text

![Image](https://github.com/user-attachments/assets/4d6dba9f-b0f0-4d90-8e5d-1ad6352a5954)

##### Step 2: Vectorize and enrich your images

![Image](https://github.com/user-attachments/assets/bf36e2af-7da5-45cd-a16f-ad4eabcf359c)

##### Step 3: Advanced settings (Semantic Configuration)

![Image](https://github.com/user-attachments/assets/56970011-31c8-4b39-8df7-3f6178172864)

- Configure the credentials in the `.env` file as follows:  

```plaintext
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_ENDPOINT=your-endpoint
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
AZURE_SEARCH_ENDPOINT=your-search-endpoint
AZURE_SEARCH_KEY=your-search-key
AZURE_SEARCH_INDEX_NAME=your-index-name
```

### 4️⃣ Run the Streamlit App  
```sh
streamlit run main.py
```

##  Output  
![Image](https://github.com/user-attachments/assets/2974ef19-4a48-4d70-935b-083a950fcc5a)


---


