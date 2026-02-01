import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Researcher Profile",
    page_icon="🧬",
    layout="wide"
)

st.title("Dr Tsireledzo Goodwill Makwarela")
st.caption("Researcher profile built with Streamlit")

col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("About")
    st.write(
        "I am a molecular biologist with expertise in genomics, parasitology, and epidemiology. "
        "My research focuses on tick ecology and tick borne pathogens at wildlife livestock human interfaces, "
        "supporting One Health oriented disease surveillance and risk assessment."
    )

    st.subheader("Research interests")
    st.write("Tick ecology and tick borne diseases")
    st.write("One Health strategies for zoonotic disease prevention")
    st.write("Parasite genomics and molecular epidemiology")
    st.write("Vector host environment interactions")
    st.write("Participatory research and conservation governance")

with col2:
    st.subheader("Contact")
    st.write("makwarelatg@tut.ac.za")
    st.write("tgmakwarela@gmail.com")
    st.write("Gauteng, South Africa")
    st.write("ORCID 0000 0001 9929 1722")
    st.write("Google Scholar shorturl.at/FGYcc")

st.divider()

st.subheader("Selected publications")
publications = [
    {"Year": 2025, "Title": "Distribution and prevalence of ticks and tick borne pathogens at the wildlife livestock interface in Africa", "Journal": "Veterinary Sciences"},
    {"Year": 2025, "Title": "Vegetation change impacts on tick populations in savanna ecosystems", "Journal": "Diversity"},
    {"Year": 2025, "Title": "Integrated tick control strategies for effective management", "Journal": "Veterinary Sciences"},
    {"Year": 2024, "Title": "Morphological and molecular characterisation of ticks infesting cattle in South Africa", "Journal": "Veterinary Sciences"}
]

st.dataframe(publications, use_container_width=True)

st.divider()

st.subheader("Curriculum vitae")
cv = st.file_uploader("Upload CV PDF", type=["pdf"])
if cv is not None:
    st.download_button(
        "Download CV",
        cv.getvalue(),
        file_name="CV.pdf",
        mime="application/pdf"
    )

st.caption(f"Last updated {date.today().isoformat()}")
