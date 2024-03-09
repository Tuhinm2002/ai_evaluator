import streamlit as st
import os
import pypdf
from llama_index.llms import GradientBaseModelLLM
from llama_index import VectorStoreIndex,SimpleDirectoryReader
from llama_index.embeddings import GradientEmbedding
from dotenv import load_dotenv
from llama_index import ServiceContext,set_global_service_context
from streamlit_extras.stylable_container import stylable_container

with open("app.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>",unsafe_allow_html=True)

st.markdown("""### Smart evaluator here """,unsafe_allow_html=False)
def configure():
    load_dotenv()

configure()

with stylable_container(
    key="navbar",
    css_styles="""
      div[data-testid="stDecoration"]{
        color:red
      }
    """
):
    side_bar = st.sidebar.selectbox(
        "Navigate",
        ("Home","About us")
    )

if side_bar == "Home":
    try:
        uploadedfile = st.file_uploader("Upload your answer script")

        if not os.path.exists("tempDir"):
            os.mkdir("tempDir")


        with open(os.path.join("tempDir", uploadedfile.name), "wb") as f:
            f.write(uploadedfile.getbuffer())

        with stylable_container(
            key="input_area",
            css_styles="""
                 color: yellow;
            """
        ):
            inp = st.text_input("input")

        llm = GradientBaseModelLLM(
            base_model_slug="llama2-7b-chat",
            max_tokens=400
        )

        embed_model = GradientEmbedding(
            gradient_access_token=os.getenv('GRADIENT_ACCESS_TOKEN'),
            gradient_workspace_id=os.getenv('GRADIENT_WORKSPACE_ID'),
            gradient_model_slug="bge-large"
        )

        service_context = ServiceContext.from_defaults(llm=llm,
                                                       embed_model=embed_model,
                                                       chunk_size=256
                                                       )
        set_global_service_context(service_context=service_context)


        doc = SimpleDirectoryReader("tempDir").load_data()

        index = VectorStoreIndex.from_documents(doc,service_context=service_context)
        query_engine = index.as_query_engine()
        response = query_engine.query(inp)
        st.write(response.response)
        with stylable_container(
            key="del_btn",
            css_styles="""
            
            """
        ):
            del_btn = st.button("Delete your data button")
        if del_btn:
            for d in os.listdir("tempDir")[:]:
                os.remove(os.path.join("tempDir",d))
    except:
        pass
elif side_bar == "About us":
    st.write(""" this is About us""")

st.write("\n")
st.write("\n") 
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")