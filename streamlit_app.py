import streamlit as st
import requests

st.set_page_config(
    page_title="Queren Serviços Digitais",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# CONFIGURAÇÕES
# =========================

WHATSAPP = "SEU_WHATSAPP"
EMAIL = "SEU_EMAIL"
INSTAGRAM = "SEU_INSTAGRAM"

SERVICOS = [
    "🎬 Edição de vídeos",
    "📊 Excel",
    "📝 Digitação e formatação",
    "📄 Currículos",
    "📊 PowerPoint / Apresentações",
    "📁 Organização de arquivos/documentos"
]

# =========================
# ESTILO
# =========================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}

.stApp {
    background: #080b0a;
    color: #ffffff;
}

.block-container {
    max-width: 1180px;
    padding-top: 35px;
    padding-bottom: 50px;
}

/* TÍTULOS */

h1, h2, h3, p, label {
    color: #ffffff !important;
}

/* HERO */

.hero {
    background: linear-gradient(135deg, #111614, #18211e);
    border: 1px solid #26342f;
    border-radius: 30px;
    padding: 60px 45px;
    margin-bottom: 45px;
    box-shadow: 0 15px 45px rgba(0,0,0,0.35);
}

.badge {
    display: inline-block;
    background: #c8f36a;
    color: #101510 !important;
    padding: 8px 16px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: bold;
    margin-bottom: 18px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    margin: 0;
}

.hero p {
    color: #cbd4d0 !important;
    font-size: 18px;
    line-height: 1.7;
    max-width: 720px;
}

/* SEÇÕES */

.section-title {
    color: #ffffff !important;
    font-size: 32px;
    font-weight: 800;
    margin-top: 45px;
    margin-bottom: 8px;
}

.section-subtitle {
    color: #aab5b0 !important;
    margin-bottom: 25px;
}

/* CARDS */

.card {
    background: #111614;
    border: 1px solid #26342f;
    border-radius: 22px;
    padding: 25px;
    min-height: 190px;
    margin-bottom: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.20);
}

.card h3 {
    color: #ffffff !important;
    font-size: 20px;
}

.card p {
    color: #aab5b0 !important;
    line-height: 1.6;
}

/* FORMULÁRIO */

.form-box {
    background: #111614;
    border: 1px solid #26342f;
    border-radius: 25px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}

/* CAMPOS */

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    background-color: #1a211e !important;
    color: #ffffff !important;
    border: 1px solid #34443e !important;
    border-radius: 12px !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #8d9994 !important;
}

/* SELECT */

div[data-baseweb="select"] span {
    color: #ffffff !important;
}

/* BOTÃO */

.stButton > button {
    background: #c8f36a !important;
    color: #101510 !important;
    border: none !important;
    border-radius: 13px !important;
    font-weight: 800 !important;
    min-height: 50px;
}

.stButton > button:hover {
    background: #d8ff82 !important;
    color: #101510 !important;
}

/* PAGAMENTO */

.payment-box {
    background: #172016;
    border: 1px solid #3d5131;
    border-radius: 23px;
    padding: 28px;
    margin-top: 30px;
}

.payment-box h3 {
    color: #c8f36a !important;
}

.payment-box p {
    color: #c4cec8 !important;
}

/* CONTATO */

.contact-box {
    background: linear-gradient(135deg, #111614, #18211e);
    border: 1px solid #26342f;
    color: white;
    padding: 35px;
    border-radius: 25px;
    margin-top: 35px;
}

.contact-box h2 {
    color: #ffffff !important;
}

.contact-box p {
    color: #b8c2bd !important;
}

/* INFO */

div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* RODAPÉ */

.footer {
    text-align: center;
    color: #69746f !important;
    padding: 40px 0 10px;
    font-size: 14px;
}

/* MOBILE */

@media (max-width: 700px) {

    .hero {
        padding: 40px 25px;
    }

    .hero h1 {
        font-size: 35px;
    }

    .section-title {
        font-size: 27px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================
# HERO
# =========================

st.markdown("""
<div class="hero">

<div class="badge">SERVIÇOS DIGITAIS</div>

<h1>Queren Serviços Digitais</h1>

<p>
Soluções digitais simples, organizadas e profissionais
para pessoas, estudantes e pequenos negócios.
</p>

</div>
""", unsafe_allow_html=True)


# =========================
# SERVIÇOS
# =========================

st.markdown(
    '<div class="section-title">Meus serviços</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Serviços digitais feitos de forma personalizada e profissional.'
    '</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

cards = [
    ("🎬", "Edição de vídeos",
     "Edição de vídeos para redes sociais, trabalhos e conteúdos digitais."),

    ("📊", "Excel",
     "Organização de planilhas, tabelas, cálculos e apresentação de dados."),

    ("📝", "Digitação e formatação",
     "Digitação, organização e formatação de documentos."),

    ("📄", "Currículos",
     "Criação e organização de currículos com visual profissional."),

    ("📊", "PowerPoint",
     "Criação e organização de apresentações claras e profissionais."),

    ("📁", "Organização de arquivos",
     "Organização e padronização de arquivos e documentos digitais.")
]

for i, (icone, titulo, descricao) in enumerate(cards):

    coluna = [col1, col2, col3][i % 3]

    with coluna:

        st.markdown(
            f"""
            <div class="card">

                <div style="font-size:34px">
                    {icone}
                </div>

                <h3>{titulo}</h3>

                <p>{descricao}</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================
# SOBRE
# =========================

st.markdown(
    '<div class="section-title">Sobre o serviço</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">

<h3>✨ Trabalho organizado e personalizado</h3>

<p>
Cada solicitação é analisada individualmente para entender
exatamente o que você precisa.
</p>

<p>
O objetivo é entregar arquivos organizados, claros e com
um visual profissional.
</p>

</div>
""", unsafe_allow_html=True)


# =========================
# ORÇAMENTO
# =========================

st.markdown(
    '<div class="section-title">Solicite um orçamento</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Preencha os dados abaixo e envie sua solicitação.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="form-box">', unsafe_allow_html=True)

nome = st.text_input(
    "Seu nome *",
    placeholder="Digite seu nome"
)

whatsapp = st.text_input(
    "WhatsApp *",
    placeholder="Digite seu WhatsApp"
)

email = st.text_input(
    "E-mail",
    placeholder="Digite seu e-mail"
)

servico = st.selectbox(
    "Qual serviço você precisa? *",
    SERVICOS
)

descricao = st.text_area(
    "Explique o que você precisa *",
    placeholder="Conte um pouco sobre o seu projeto...",
    height=160
)

prazo = st.text_input(
    "Prazo desejado",
    placeholder="Ex.: até sexta-feira"
)

pagamento = st.selectbox(
    "Forma de pagamento",
    [
        "Pix após aprovação do orçamento",
        "Cartão",
        "Transferência"
    ]
)

enviar = st.button(
    "📩 Enviar solicitação de orçamento",
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================
# BANCO DE DADOS
# =========================

def salvar_pedido(dados):

    try:

        supabase_url = st.secrets["SUPABASE_URL"]
        supabase_key = st.secrets["SUPABASE_ANON_KEY"]

        url = f"{supabase_url}/rest/v1/pedidos"

        headers = {
            "apikey": supabase_key,
            "Authorization": f"Bearer {supabase_key}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        }

        resposta = requests.post(
            url,
            headers=headers,
            json=dados,
            timeout=20
        )

        return resposta.status_code in [200, 201, 204]

    except Exception:
        return False


# =========================
# ENVIO
# =========================

if enviar:

    if not nome or not whatsapp or not descricao:

        st.error(
            "⚠️ Preencha seu nome, WhatsApp e explique o que você precisa."
        )

    else:

        pedido = {
            "nome": nome,
            "whatsapp": whatsapp,
            "email": email,
            "servico": servico,
            "descricao": descricao,
            "prazo": prazo,
            "forma_pagamento": pagamento,
            "status": "Novo"
        }

        sucesso = salvar_pedido(pedido)

        if sucesso:

            st.success(
                "✅ Solicitação enviada com sucesso! "
                "Entraremos em contato para conversar sobre o orçamento."
            )

        else:

            st.error(
                "⚠️ Não foi possível enviar a solicitação. "
                "Verifique a configuração do banco de dados."
            )


# =========================
# PAGAMENTO
# =========================

st.markdown("""
<div class="payment-box">

<h3>💳 Formas de pagamento</h3>

<p>
<strong>Pix disponível após aprovação do orçamento.</strong>
</p>

<p>
O pagamento somente será solicitado depois que o serviço,
o prazo e o valor forem combinados.
</p>

<p>
Também é possível combinar outras formas de pagamento.
</p>

</div>
""", unsafe_allow_html=True)


# =========================
# CONTATO
# =========================

st.markdown("""
<div class="contact-box">

<h2>Vamos trabalhar juntos?</h2>

<p>
Envie sua solicitação pelo formulário ou entre em contato
para conversar sobre o seu projeto.
</p>

</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📱 WhatsApp\n\n" + WHATSAPP)

with col2:
    st.info("📧 E-mail\n\n" + EMAIL)

with col3:
    st.info("📸 Instagram\n\n" + INSTAGRAM)


# =========================
# RODAPÉ
# =========================

st.markdown("""
<div class="footer">

© 2026 Queren Serviços Digitais · Todos os direitos reservados.

</div>
""", unsafe_allow_html=True)
