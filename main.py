import streamlit as st
from embeddings import EmbeddingGenerator
from ai_search import AISearch
from llm import LLMResponseGenerator

def display_message(role, content, show_sources=False, sources=None):
    """Display a chat message with custom styling."""
    with st.container():
        if role == "user":
            st.markdown(f'<div class="chat-message user"><div class="avatar">👤</div><div class="message">{content}</div></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message assistant"><div class="avatar">🤖</div><div class="message">{content}</div></div>', unsafe_allow_html=True)
            if show_sources and sources:
                with st.expander("View Sources"):
                    for idx, source in enumerate(sources, 1):
                        st.markdown(f"**Source {idx}:**")
                        st.markdown(f"**Title:** {source.get('title', 'No title')}")
                        st.markdown(f"**Content:** {source.get('chunk', '')}")
                        st.markdown("---")

def main():
    st.set_page_config(page_title="Chat with Document", page_icon="🔍", layout="centered")
    st.title("Chat with Document 🤖")
    st.markdown("Ask me anything about the available information!")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        display_message(
            role=message["role"],
            content=message["content"],
            show_sources=message.get("show_sources", False),
            sources=message.get("sources", None)
        )

    # Chat input
    query = st.chat_input("Type your message here...")

    if query:
        embedding_generator = EmbeddingGenerator()
        ai_search = AISearch()
        llm_generator = LLMResponseGenerator()

        # Display user message
        display_message("user", query)
        st.session_state.messages.append({"role": "user", "content": query})

        # Generate embedding for the query
        embedding = embedding_generator.get_embedding(query)
        
        if embedding:
            # Perform hybrid search
            search_results = ai_search.hybrid_search(query, embedding)
            
            if search_results:
                # Generate and display AI response
                response = llm_generator.generate_response(query, search_results)
                if response:
                    display_message("assistant", response, show_sources=True, sources=search_results)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response,
                        "show_sources": True,
                        "sources": search_results
                    })
            else:
                error_msg = "No relevant documents found."
                display_message("assistant", error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
        else:
            error_msg = "Failed to process your query. Please try again."
            display_message("assistant", error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})

if __name__ == "__main__":
    main()
