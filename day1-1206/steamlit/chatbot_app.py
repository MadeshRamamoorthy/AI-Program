import streamlit as st
import anthropic
import os

# Page configuration
st.set_page_config(page_title="Claude Chatbot", page_icon="🤖")

# Title
st.title("🤖 Claude Chatbot")

# Initialize the Anthropic client
# Using Streamlit secrets for API key (secure method)
try:
    api_key = st.secrets["ANTHROPIC_API_KEY"]
except:
    # Fallback to environment variable
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    
if not api_key:
    st.error("⚠️ Please add your ANTHROPIC_API_KEY to Streamlit secrets or environment variables")
    st.stop()

client = anthropic.Anthropic(api_key=api_key)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to count words
def count_words(text):
    return len(text.split())

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Check word count
    word_count = count_words(prompt)
    
    if word_count > 200:
        st.error(f"❌ Your question has {word_count} words. Please keep it under 200 words.")
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get Claude's response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            try:
                # Call Claude API
                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=1000,
                    system="You are a helpful assistant. Always keep your responses under 500 words. Be concise and clear.",
                    messages=[
                        {"role": m["role"], "content": m["content"]} 
                        for m in st.session_state.messages
                    ]
                )
                
                # Extract response text
                full_response = response.content[0].text
                
                # Check if response exceeds 500 words (shouldn't happen with system prompt, but double-check)
                response_word_count = count_words(full_response)
                if response_word_count > 500:
                    words = full_response.split()
                    full_response = ' '.join(words[:500]) + "..."
                
                message_placeholder.markdown(full_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Sidebar with info
with st.sidebar:
    st.header("ℹ️ Information")
    st.markdown("""
    **Usage Limits:**
    - Your questions: Max 200 words
    - Claude's responses: Max 500 words
    
    **Model:** Claude Sonnet 4
    """)
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.caption("Powered by Claude AI")
