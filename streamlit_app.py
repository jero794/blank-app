import streamlit as st

# Título de la aplicación
st.title("Curriculum Vitae")

# Texto del currículum en formato Markdown
markdown_text = """
# Jeronimo Ramirez Pujol

**Dirección:** Av. Vallarta Eje Poniente 2701, Los Sueños Residencial, 45222, Zapopan  
**Teléfono:** (33) 1131 5020  
**Email:** jeronimo.ramirezprc@gmail.com  

## Personal Statement
I am currently a student of the bachelor's degree in Finance and Administration. I am deeply interested in developing my professional career in the financial sector, specifically in asset management. I am looking for a job where I can constantly learn new investment strategies, gain experience, and apply my knowledge.

## Experience

### A&J Maquinas Expendedoras - 2022
I was a co-founder of A&J, a company focused on comprehensive service with state-of-the-art vending machines. The main activities I performed included:
- Monitoring purchases made in the machines
- Inventory management
- Creating income statements for the machines
- Overall financial statements for the company

### Universidad Panamericana de Guadalajara - 2023
I worked in the public relations field. My main activities included:
- Attending events both within and outside the city to promote the university
- Giving promotional talks about the university
- Providing guidance to students on admission processes

### CAPX - 2023
I am a co-founder of CAPX, a company focused on creating profitability for its clients through digital marketing strategies. The main activities I perform include:
- Operations management
- Customer service oversight
- Overall administration of the company

## Education

### Universidad Panamericana de Guadalajara
Current student of the Bachelor’s Degree in Finance and Administration

## Certificates
- TOEFL ITP

## Languages
- **Spanish**: Native Language
- **English**: Upper Advanced

## Skills
- Strong leadership and strategic planning skills
- Excellent customer service skills
- Proficient in Microsoft Office Suite (Proficiency in creating and automating macros)
- Experience with marketing software
- Strong analytical and problem-solving skills
- Experience with accounting software
"""

# Mostrar el contenido del markdown en la aplicación de Streamlit
st.markdown(markdown_text)


# Barra lateral con información adicional
st.sidebar.title("Sobre mí")
st.sidebar.info("Soy un estudiante que se esta capacitando en Python")


st.subheader("Contáctame")
# Formulario simple
nombre = st.text_input("Nombre")
email = st.text_input("Correo electrónico")
mensaje = st.text_area("Mensaje")
if st.button("Enviar"):
    st.success(f"Gracias por tu mensaje, {nombre}!")
