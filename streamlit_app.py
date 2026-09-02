import streamlit as st
import requests

# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="Queren Serviços Digitais",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Troque depois pelos seus contatos
WHATSAPP = "Seu WhatsApp"
EMAIL = "seuemail@email.com"
INSTAGRAM = "@seuinstagram"

SERVICOS = [
    "Edição de vídeos",
    "Excel",
    "Digitação e formatação",
    "Currículos",
    "PowerPoint / Apresentações",
    "Organização de arquivos/documentos"
]

# =========================================================
# VISUAL
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #080b0a;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 35px;
        padding-bottom: 50px;
    }

    /* TEXTOS */
    h1, h2, h3 {
        color: #ffffff !important;
    }

    p {
        color: #b9c3be !important;
    }

    /* HERO */
    .hero {
        background: linear-gradient(135deg, #101513, #1a2420);
        border: 1px solid #2b3833;
        border-radius: 28px;
        padding: 55px 45px;
        margin-bottom: 40px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.35);
    }

    .badge {
        display: inline-block;
        background: #c9f36a;
        color: #101510 !important;
        padding: 8px 15px;
        border-radius: 30px;
        font-size: 13px;
        font-weight: 800;
        margin-bottom: 18px;
    }

    .hero-title {
        color: #ffffff !important;
        font-size: 48px;
        font-weight: 800;
        margin: 0 0 15px 0;
    }

    .hero-text {
        color: #c4ceca !important;
        font-size: 18px;
        line-height: 1.7;
        max-width: 700px;
    }

    /* TÍTULOS DAS SEÇÕES */
    .section-title {
        color: #ffffff !important;
        font-size: 32px;
        font-weight: 800;
        margin-top: 45px;
        margin-bottom: 8px;
    }

    .section-subtitle {
        color: #8f9b96 !important;
        margin-bottom: 25px;
        font-size: 16px;
    }

    /* CARTÕES */
    .service-card {
        background-color: #111614;
        border: 1px solid #293631;
        border-radius: 20px;
        padding: 25px;
        min-height: 180px;
        margin-bottom: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    }

    .service-icon {
        font-size: 34px;
        margin-bottom: 10px;
    }

    .service-title {
        color: #ffffff !important;
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .service-description {
        color: #aeb9b4 !important;
        font-size: 15px;
        line-height: 1.6;
    }

    /* CAIXA DO FORMULÁRIO */
    .form-intro {
        background-color: #111614;
        border: 1px solid #293631;
        border-radius: 24px;
        padding: 28px;
        margin-bottom: 15px;
    }

    /* CAMPOS DO STREAMLIT */
    label {
        color: #ffffff !important;
    }

    .stTextInput input,
    .stTextArea textarea {
        background-color: #171d1a !important;
        color: #ffffff !important;
        border: 1px solid #394740 !important;
        border-radius: 12px !important;
    }

    .stTextInput input::placeholder,
    .stTextArea textarea::placeholder {
        color: #7f8b86 !important;
    }

    /* SELECTBOX */
    div[data-baseweb="select"] > div {
        background-color: #171d1a !important;
        border-color: #394740 !important;
        color: #ffffff !important;
    }

    div[data-baseweb="select"] span {
        color: #ffffff !important;
    }

    /* BOTÃO */
    .stButton > button {
        width: 100%;
        background-color: #c9f36a !important;
        color: #101510 !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 800 !important;
        min-height: 50px;
    }

    .stButton > button:hover {
        background-color: #d9ff82 !important;
        color: #101510 !important;
    }

    /* PAGAMENTO */
    .payment-box {
        background-color: #151d13;
        border: 1px solid #405532;
        border-radius: 22px;
        padding: 28px;
        margin-top: 30px;
    }

    .payment-title {
        color: #c9f36a !important;
        font-size: 22px;
        font-weight: 800;
    }

    /* CONTATO */
    .contact-box {
        background: linear-gradient(135deg, #101513, #1a2420);
        border: 1px solid #293631;
        border-radius: 24px;
        padding: 35px;
        margin-top: 35px;
    }

    .contact-title {
        color: #ffffff !important;
        font-size: 28px;
        font-weight: 800;
    }

    /* RODAPÉ */
    .footer {
        text-align: center;
        color: #66736d !important;
        padding-top: 40px;
        font-size: 14px;
    }

    @media (max-width: 700px) {

        .hero {
            padding: 40px 25px;
        }

        .hero-title {
            font-size: 35px;
        }

        .section-title {
            font-size: 27px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# TOPO
# =========================================================

st.markdown(
    """
    <div class="hero">

        <div class="badge">SERVIÇOS DIGITAIS</div>

        <div class="hero-title">
            Queren Serviços Digitais
        </div>

        <div class="hero-text">
            Soluções digitais simples, organizadas e profissionais
            para pessoas, estudantes e pequenos negócios.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SERVIÇOS
# =========================================================

st.markdown(
    '<div class="section-title">Meus serviços</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Escolha o serviço que você precisa e solicite um orçamento.'
    '</div>',
    unsafe_allow_html=True
)

servicos = [
    (
        "🎬",
        "Edição de vídeos",
        "Edição de vídeos para redes sociais, trabalhos e conteúdos digitais."
    ),
    (
        "📊",
        "Excel",
        "Organização de planilhas, tabelas, cálculos e apresentação de dados."
    ),
    (
        "📝",
        "Digitação e formatação",
        "Digitação, organização e formatação de documentos."
    ),
    (
        "📄",
        "Currículos",
        "Criação e organização de currículos com visual profissional."
    ),
    (
        "📊",
        "PowerPoint",
        "Criação e organização de apresentações claras e profissionais."
    ),
    (
        "📁",
        "Organização de arquivos",
        "Organização e padronização de arquivos e documentos digitais."
    )
]

colunas = st.columns(3)

for indice, servico in enumerate(servicos):

    icone = servico[0]
    titulo = servico[1]
    descricao = servico[2]

    with colunas[indice % 3]:

        st.markdown(
            f"""
            <div class="service-card">

                <div class="service-icon">
                    {icone}
                </div>

                <div class="service-title">
                    {titulo}
                </div>

                <div class="service-description">
                    {descricao}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# SOBRE
# =========================================================

st.markdown(
    '<div class="section-title">Sobre o serviço</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="form-intro">

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
    """,
    unsafe_allow_html=True
)

# =========================================================
# FORMULÁRIO
# =========================================================

st.markdown(
    '<div class="section-title">Solicite um orçamento</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Preencha os dados abaixo para enviar sua solicitação.'
    '</div>',
    unsafe_allow_html=True
)

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

servico_escolhido = st.selectbox(
    "Qual serviço você precisa? *",
    SERVICOS
)

descricao = st.text_area(
    "Explique o que você precisa *",
    placeholder="Conte aqui o que você precisa...",
    height=150
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
    "📩 Enviar solicitação de orçamento"
)

# =========================================================
# FUNÇÃO DO SUPABASE
# =========================================================

def salvar_pedido(dados):

    try:

        supabase_url = st.secrets["SUPABASE_URL"]
        supabase_key = st.secrets["SUPABASE_ANON_KEY"]

        url = supabase_url.rstrip("/") + "/rest/v1/pedidos"

        headers = {
            "apikey": supabase_key,
            "Authorization": "Bearer " + supabase_key,
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        }

        resposta = requests.post(
            url,
            headers=headers,
            json=dados,
            timeout=20
        )

        if resposta.status_code in [200, 201, 204]:
            return True

        return False

    except Exception:
        return False

# =========================================================
# ENVIAR PEDIDO
# =========================================================

if enviar:

    if nome.strip() == "":
        st.error("⚠️ Digite seu nome.")

    elif whatsapp.strip() == "":
        st.error("⚠️ Digite seu WhatsApp.")

    elif descricao.strip() == "":
        st.error("⚠️ Explique o que você precisa.")

    else:

        pedido = {
            "nome": nome,
            "whatsapp": whatsapp,
            "email": email,
            "servico": servico_escolhido,
            "descricao": descricao,
            "prazo": prazo,
            "forma_pagamento": pagamento,
            "status": "Novo"
        }

        resultado = salvar_pedido(pedido)

        if resultado:

            st.success(
                "✅ Solicitação enviada com sucesso! "
                "Entraremos em contato para conversar sobre o orçamento."
            )

        else:

            st.error(
                "⚠️ Não foi possível enviar a solicitação. "
                "A configuração do banco de dados ainda precisa ser concluída."
            )

# =========================================================
# PAGAMENTO
# =========================================================

st.markdown(
    """
    <div class="payment-box">

        <div class="payment-title">
            💳 Formas de pagamento
        </div>

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
    """,
    unsafe_allow_html=True
)

# =========================================================
# CONTATO
# =========================================================

st.markdown(
    """
    <div class="contact-box">

        <div class="contact-title">
            Vamos trabalhar juntos?
        </div>

        <p>
        Envie sua solicitação pelo formulário ou entre em contato
        para conversar sobre o seu projeto.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📱 WhatsApp\n\n" + WHATSAPP)

with col2:
    st.info("📧 E-mail\n\n" + EMAIL)

with col3:
    st.info("📸 Instagram\n\n" + INSTAGRAM)

# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
    """
    <div class="footer">
        © 2026 Queren Serviços Digitais · Todos os direitos reservados.
    </div>
    """,
    unsafe_allow_html=True
)
