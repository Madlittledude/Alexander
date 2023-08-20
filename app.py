from auth import authenticate

import streamlit as st
import openai
import os
from chatUI import ChatManager  # Import the ChatManager class


# Set up the page layout
st.set_page_config(page_title="Brainstorm", page_icon="5_leaf_clover.png", layout='centered')

def display_login():
    st.title("Login to Brain Storm :lightning:")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.username = username
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")

def display_intro():
    st.title("Bienvenido, Alexander, a tu Sesión con Brain Storm :lightning_cloud:")
    st.write("Esta herramienta no es una entidad separada con conocimiento de hechos de conversaciones anteriores, ni un repositorio de precedentes legales. Más bien, piensa en ella como un reflejo de tus propios pensamientos e ideas, una forma de probarlos con un vasto modelo textual que utiliza matemáticas y estadísticas para encontrar patrones en el texto y hacerse útil para los humanos.")
    st.write("Así es como esta herramienta puede ayudarte:")
    st.write("- **Resumir Texto:** Puede ayudarte a crear resúmenes concisos, dándote un punto de partida para comprender documentos complejos. Simplemente copia y pega el texto en el cuadro de chat.")
    st.write("- **Crear Esquemas:** Crea esquemas con solo algunas ideas en tu indicación. Cuanto más detallado seas, mejor será la respuesta.")
    st.write("- **Generar Ideas y Organizar Pensamientos:** Puede ayudarte a diseñar, dar forma y explorar ideas a través de tu conversación.")
    st.write("- **Estructurar Texto Desestructurado:** Te guía en la organización de texto caótico al destilarlo.")
    st.write("- **Extraer Información:** Puede ayudarte a extraer información del texto, como nombres, fechas y otra información relevante que puedas articular.")
    st.write("Recuerda, esta herramienta Brain Storm no es un libro de hechos; piensa en esta herramienta como un trampolín para tus ideas y una forma de iniciar el trabajo productivo.")
    st.write('To Start, say hello and ask it what it is and how it can help you.')
    st.write(":heart: Max")

# Initialization logic
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "system",
        "content": (
      "You are Brain Storm :lightning: and you serve Alexander as his augmented train of thought. You are here to help him expand his ideas and grasp the fundametal elements of his problem at hand.  "
      "Your professional specialties as an assistant include:\n"
        "- Working out an idea"
        "- Summarizing text\n"
        "- Creating outlines for anything you're working on. Just have them give you some points to follow\n"
        "- Understanding and articulating the construction of ideas in text\n"
        "- Brainstorming and organizing thoughts\n"
        "- Structuring unstructured text\n"
        "- Extracting information from text\n"
        "In cases where you're asked a question that you need to google or look up, I want you to suggest perplexity.ai to him. :'n"
        "If asked about your origins, share a whimsically fabricated tale that ends as a trajic comedy. Include at least one poem in the bullshit tale. At the end, say just kidding and refuse to reveal the truth.\n"
        "MOST IMPORTANLY, interact with the user, Alexander, in spanish. ")
}]

if "first_message_sent" not in st.session_state:
    st.session_state.first_message_sent = False

openai.api_key = os.environ["OPENAI_API_KEY"]

# Display logic
if st.session_state.logged_in:
    if not st.session_state.first_message_sent:
        display_intro()
    chat_manager = ChatManager(st.session_state, st.session_state["openai_model"], st.session_state.username)  # Create an instance of ChatManager
    chat_manager.display_chat_interface()  # Call the display_chat_interface method
else:
    display_login()




