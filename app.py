import streamlit as st
from typing import List
from openai import OpenAI
from toolhouse import Toolhouse
import json
import re
import validators

# Helper function to extract image URLs from tool response
def extract_image_urls(tool_response):
    """
    Extracts and validates image URLs from the tool response.

    Args:
        tool_response (list): The response list from th.run_tools(response).

    Returns:
        list: A list of valid image URLs extracted from the response.
    """
    image_urls = []
    for item in tool_response:
        if item.get('role') == 'tool' and 'content' in item:
            try:
                content = json.loads(item['content'])
                result_markdown = content.get('result', '')
                # Use regex to extract URLs from markdown
                urls = re.findall(r'!\[.*?\]\((.*?)\)', result_markdown)
                # Validate each URL
                valid_urls = [url for url in urls if validators.url(url)]
                image_urls.extend(valid_urls)
            except json.JSONDecodeError:
                # Handle invalid JSON
                st.warning("Received invalid JSON in tool response.")
                continue
    return image_urls

# Initialize OpenAI and Toolhouse clients using Streamlit secrets
client = OpenAI(api_key='YOUR_OPENAI_API_KEY')
th = Toolhouse(access_token='YOUR_TOOLHOUSE_API_KEY',
provider="openai")

# Constants
MODEL = 'gpt-3.5-turbo'

# Initialize session state for room_state
if 'room_state' not in st.session_state:
    st.session_state.room_state = {
        "description": "",
        "components": [],
        "image": None
    }

# Predefined mapping of components to Amazon URLs (example)
AMAZON_LINKS = {
    "green plant": "https://www.amazon.com/s?k=green+plant",
    "queen bed": "https://www.amazon.com/s?k=queen+bed",
    "wooden nightstand": "https://www.amazon.com/s?k=wooden+nightstand",
    "colorful rug": "https://www.amazon.com/s?k=colorful+rug",
    "desk": "https://www.amazon.com/s?k=desk",
    # Add more mappings as needed
}

def initialize_room(client, initial_description):
    messages = [{
        "role": "user",
        "content": initial_description
    }]
   
    # Save initial state
    st.session_state.room_state = {
        "description": initial_description,
        "components": []
    }
   
    try:
        # Generate initial image based on user's description
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=th.get_tools('my-app')
        )
       
        # Run tools and get the image output
        tool_response = th.run_tools(response)
       
        # Extract image URLs from the tool response
        image_urls = extract_image_urls(tool_response)
       
        if image_urls:
            st.session_state.room_state["image"] = image_urls
            return image_urls
        else:
            st.error("No image URLs found in the tool response.")
            return None
    except Exception as e:
        st.error(f"An error occurred during initialization: {e}")
        return None

def update_room(client, new_description):
    # Update room state with the new component or change
    st.session_state.room_state["components"].append(new_description)
   
    # Regenerate image based on updated room description
    cumulative_description = st.session_state.room_state["description"] + " " + " ".join(st.session_state.room_state["components"])
   
    messages = [{
        "role": "user",
        "content": cumulative_description
    }]
   
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=th.get_tools('my-app')
        )
       
        # Run tools and get the image output
        tool_response = th.run_tools(response)
       
        # Extract image URLs from the tool response
        image_urls = extract_image_urls(tool_response)
       
        if image_urls:
            st.session_state.room_state["image"] = image_urls
            return image_urls
        else:
            st.error("No image URLs found in the tool response.")
            return None
    except Exception as e:
        st.error(f"An error occurred during update: {e}")
        return None

def get_amazon_link(component):
    """Return the Amazon shopping link for a given component."""
    return AMAZON_LINKS.get(component.lower(), None)

# Streamlit App Layout
st.title("Interactive Room Designer")

# Sidebar for Initialization
st.sidebar.header("Initialize Room")
initial_description = st.sidebar.text_area(
    "Enter the initial description of the room:",
    value="Generate an image of a cozy bedroom with soft blue walls, a queen-sized bed with white linens, a wooden nightstand with a small lamp, and a colorful rug on the floor."
)

if st.sidebar.button("Initialize Room"):
    if initial_description.strip() == "":
        st.sidebar.warning("Please enter a valid room description.")
    else:
        with st.spinner("Generating initial room image..."):
            initial_image = initialize_room(client, initial_description)
        if initial_image:
            st.sidebar.success("Room initialized!")
            
            # Handle single or multiple images
            if isinstance(initial_image, list):
                captions = ["Initial Room Image"] * len(initial_image)
                st.image(initial_image, caption=captions, use_column_width=True)
            else:
                st.image(initial_image, caption="Initial Room Image", use_column_width=True)

# Main Area for Updates
st.header("Update Room")

new_component = st.text_input("Add a new component to the room:")

if st.button("Add Component"):
    if st.session_state.room_state["description"] == "":
        st.warning("Please initialize the room first.")
    elif new_component.strip() == "":
        st.warning("Please enter a valid component description.")
    else:
        with st.spinner("Updating room image..."):
            updated_image = update_room(client, new_component)
        if updated_image:
            st.success("Room updated!")
            
            # Handle single or multiple images
            if isinstance(updated_image, list):
                captions = ["Updated Room Image"] * len(updated_image)
                st.image(updated_image, caption=captions, use_column_width=True)
            else:
                st.image(updated_image, caption="Updated Room Image", use_column_width=True)
        
        # Check if an Amazon link is available for the component
        amazon_link = get_amazon_link(new_component)
        if amazon_link:
            st.markdown(f"**Shop for {new_component}:** [Amazon Link]({amazon_link})")
        else:
            st.warning(f"No Amazon link available for '{new_component}'.")

# Display Current Room State
st.subheader("Current Room Description")
cumulative_description = st.session_state.room_state["description"] + " " + " ".join(st.session_state.room_state["components"])
st.write(cumulative_description)

if st.session_state.room_state["image"]:
    st.subheader("Current Room Image")
    current_image = st.session_state.room_state["image"]
    
    if isinstance(current_image, list):
        captions = ["Current Room Image"] * len(current_image)
        st.image(current_image, caption=captions, use_column_width=True)
    else:
        st.image(current_image, caption="Current Room Image", use_column_width=True)
