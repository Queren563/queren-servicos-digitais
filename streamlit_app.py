import streamlit as st
import requests
from datetime import datetime

# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="Queren Serviços Digitais",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CONTATOS
# =========================================================

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

# =========================================================
# VISUAL DO SITE
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f7f8f8;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

h1, h2, h3 {
    color: #101414;
}

.hero {
    background: linear-gradient(135deg, #101414 0%, #17201e 100%);
    border-radius: 28px;
    padding: 55px 45px;
    margin-bottom: 35px;
    color: white;
    box-shadow: 0 15px 40px rgba(0,0,0,0.10);
}

.hero h1 {
    color: white;
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 12px;
}

.hero p {
    color: #d8dfdc;
    font-size: 18px;
    line-height: 1.7;
    max-width: 700px;
}

.badge {
    display: inline-block;
    background: #d9f99d;
    color: #18220f;
    padding: 8px 14px;
    border-radius: 999px;
    font-weight: 700;
    font-size: 13px;
    margin-bottom: 18px;
}

.card {
    background: white;
    border-radius: 20px;
    padding: 25px;
    min-height: 170px;
    border: 1px solid #e8ecea;
    box-shadow: 0 8px 25px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

.card h3 {
    margin-top: 10px;
    font-size: 20px;
}

.card p {
    color: #626b68;
    line-height: 1.6;
}

.section-title {
    font-size: 32px;
    font-weight: 800;
    margin-top: 45px;
    margin-bottom: 8px;
}

.section-subtitle {
    color: #66706d;
    margin-bottom: 25px;
}

.form-box {
    background: white;
    border-radius: 25px;
    padding: 30px;
    border: 1px solid #e7ebe9;
    box-shadow: 0 8px 25px rgba(0,0,0,0.05);
}

.payment-box {
    background: #eef7e5;
    border: 1px solid #d9e9c7;
    border-radius: 22px;
    padding: 28px;
    margin-top: 25px;
}

.payment-box h3 {
    color: #26351e;
}

.payment-box p {
    color: #52604b;
}

.contact-box {
    background: #101414;
    color: white;
    padding: 35px;
    border-radius: 25px;
    margin-top: 35px;
}

.contact-box h2 {
    color: white;
}

.contact-box p {
    color: #d7ddda;
}

.stButton > button {
    border-radius: 12px;
    font-weight: 700;
    border: none;
    min-height: 45px;
}

.footer {
    text-align: center;
    color: #7a8380;
    padding: 35px 0 10px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TOPO
# =========================================================

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

col1, col2, col3 = st.columns(3)

cards = [
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

for i, (icone, titulo, descricao) in enumerate(cards):

    coluna = [col1, col2, col3][i % 3]

    with coluna:
        st.markdown(
            f"""
            <div class="card">
                <div style="font-size:32px">{icone}</div>
                <h3>{titulo}</h3>
                <p>{descricao}</p>
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

st.markdown("""
<div class="card">

<h3>✨ Trabalho organizado e personalizado</h3>

<p>
Cada solicitação é analisada individualmente para entender
o que você precisa e apresentar uma proposta adequada.
</p>

<p>
O objetivo é entregar arquivos organizados, claros e com
um visual profissional.
</p>

</div>
""", unsafe_allow_html=True)

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

st.markdown('<div class="form-box">', unsafe_allow_html=True)

nome = st.text_input("Seu nome *")

whatsapp = st.text_input("WhatsApp *")

email = st.text_input("E-mail")

servico = st.selectbox(
    "Qual serviço você precisa? *",
    SERVICOS
)

descricao = st.text_area(
    "Explique o que você precisa *",
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
    "📩 Enviar solicitação de orçamento",
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# FUNÇÃO DO BANCO DE DADOS
# =========================================================

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

        if resposta.status_code in [200, 201, 204]:
            return True

        return False

    except Exception:
        return False

# =========================================================
# ENVIO DO PEDIDO
# =========================================================

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
            "status": "Novo",
            "criado_em": datetime.now().isoformat()
        }

        sucesso = salvar_pedido(pedido)

        if sucesso:

            st.success(
                "✅ Solicitação enviada com sucesso! "
                "Entrarei em contato para conversar sobre o orçamento."
            )

        else:

            st.error(
                "⚠️ Não foi possível enviar a solicitação. "
                "Verifique a conexão com o banco de dados."
            )

# =========================================================
# PAGAMENTO
# =========================================================

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

# =========================================================
# CONTATO
# =========================================================

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

# =========================================================
# RODAPÉ
# =========================================================

st.markdown("""
<div class="footer">

© 2026 Queren Serviços Digitais · Todos os direitos reservados.

</div>
""", unsafe_allow_html=True)
