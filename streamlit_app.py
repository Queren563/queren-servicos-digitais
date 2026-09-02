import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Queren Serviços Digitais",
    page_icon="💻",
    layout="centered"
)

# Título
st.title("💻 Queren Serviços Digitais")
st.subheader("Serviços digitais para facilitar o seu dia a dia!")

st.write(
    "Olá! Sou Queren, estudante de Engenharia Civil em uma universidade federal, "
    "e ofereço serviços digitais, administrativos e de edição."
)

st.divider()

# Serviços
st.header("📌 Serviços oferecidos")

servicos = {
    "🎬 Edição de vídeo": [
        "Cortes de vídeos",
        "Legendas",
        "Organização de vídeos",
        "Edições para redes sociais"
    ],
    "📊 Excel": [
        "Preenchimento de planilhas",
        "Organização de dados",
        "Tabelas",
        "Fórmulas básicas"
    ],
    "📝 Digitação e formatação": [
        "Digitação de documentos",
        "Formatação de textos",
        "Organização de documentos"
    ],
    "📄 Currículos": [
        "Criação de currículo",
        "Organização das informações",
        "Formatação profissional"
    ],
    "📽️ PowerPoint": [
        "Criação de apresentações",
        "Organização dos slides",
        "Formatação visual"
    ],
    "🏗️ AutoCAD": [
        "Desenhos técnicos",
        "Auxílio em projetos",
        "Desenhos em 2D"
    ],
    "🐍 Python": [
        "Programas simples",
        "Automação de tarefas",
        "Organização de dados"
    ]
}

for nome, detalhes in servicos.items():
    with st.expander(nome):
        for item in detalhes:
            st.write("• " + item)

st.divider()

# Solicitação de orçamento
st.header("📩 Solicite um orçamento")

nome = st.text_input("Seu nome")
email = st.text_input("Seu e-mail")
servico = st.selectbox(
    "Qual serviço você deseja?",
    list(servicos.keys())
)

descricao = st.text_area(
    "Conte um pouco sobre o que você precisa:"
)

if st.button("📨 Solicitar orçamento"):
    if nome and email and descricao:
        st.success(
            "Solicitação preenchida com sucesso! "
            "Entre em contato comigo para combinarmos os detalhes."
        )
    else:
        st.warning("Preencha seu nome, e-mail e descreva o serviço desejado.")

st.divider()

# Sobre
st.header("👩‍💻 Sobre mim")

st.write(
    "Sou estudante de Engenharia Civil em uma universidade federal e "
    "tenho interesse em serviços administrativos, tecnologia, edição de "
    "vídeos e organização de documentos."
)

st.write(
    "Busco oferecer um atendimento organizado, responsável e de qualidade."
)

st.divider()

st.caption("© 2026 Queren Serviços Digitais")
