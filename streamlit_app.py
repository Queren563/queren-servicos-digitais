import streamlit as st
import requests

st.set_page_config(
    page_title="Queren Serviços Digitais",
    page_icon="💻",
    layout="wide"
)

# =========================
# CONTATOS
# =========================

WHATSAPP = "Seu WhatsApp"
EMAIL = "seuemail@email.com"
INSTAGRAM = "@seuinstagram"


# =========================
# SERVIÇOS
# =========================

SERVICOS = [
    "🎬 Edição de vídeos — a partir de R$ 100,00",
    "📊 Excel/Planilhas — a partir de R$ 45,00",
    "📝 Digitação e formatação — a partir de R$ 45,00",
    "📄 Currículos — a partir de R$ 15,00",
    "📊 PowerPoint/Apresentações — a partir de R$ 25,00"
]


# =========================
# CABEÇALHO
# =========================

st.title("💻 Queren Serviços Digitais")

st.subheader(
    "Serviços digitais simples, organizados e profissionais."
)

st.write(
    "Soluções para pessoas, estudantes e pequenos negócios."
)

st.divider()


# =========================
# SERVIÇOS
# =========================

st.header("✨ Meus serviços")

st.write(
    "Escolha o serviço que você precisa e solicite um orçamento."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🎬 Edição de vídeos")
    st.write(
        "Edição de vídeos para redes sociais, trabalhos e conteúdos digitais."
    )
    st.success("A partir de R$ 100,00")

    st.subheader("📊 Excel / Planilhas")
    st.write(
        "Organização de planilhas, tabelas, cálculos e apresentação de dados."
    )
    st.success("A partir de R$ 45,00")


with col2:
    st.subheader("📝 Digitação e formatação")
    st.write(
        "Digitação, organização e formatação de documentos."
    )
    st.success("A partir de R$ 45,00")

    st.subheader("📄 Currículos")
    st.write(
        "Criação e organização de currículos com visual profissional."
    )
    st.success("A partir de R$ 15,00")


with col3:
    st.subheader("📊 PowerPoint / Apresentações")
    st.write(
        "Criação e organização de apresentações claras e profissionais."
    )
    st.success("A partir de R$ 25,00")


st.divider()


# =========================
# SOBRE
# =========================

st.header("✨ Sobre o serviço")

st.write(
    "Cada solicitação é analisada individualmente para entender exatamente o que você precisa."
)

st.write(
    "O objetivo é entregar arquivos organizados, claros e com um visual profissional."
)

st.write(
    "Os valores apresentados são preços iniciais e podem variar de acordo com "
    "a quantidade e a complexidade do serviço."
)

st.divider()


# =========================
# FORMULÁRIO
# =========================

st.header("📩 Solicite um orçamento")

st.write(
    "Preencha os dados abaixo para enviar sua solicitação."
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

servico = st.selectbox(
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
        "Cartão via link de pagamento",
        "Transferência"
    ]
)

enviar = st.button(
    "📩 Enviar solicitação de orçamento"
)


# =========================
# BANCO DE DADOS
# =========================

def salvar_pedido(pedido):

    try:

        supabase_url = st.secrets["SUPABASE_URL"]

        supabase_key = st.secrets["SUPABASE_ANON_KEY"]

        url = (
            supabase_url.rstrip("/")
            + "/rest/v1/pedidos"
        )

        headers = {
            "apikey": supabase_key,
            "Authorization": "Bearer " + supabase_key,
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        }

        resposta = requests.post(
            url,
            headers=headers,
            json=pedido,
            timeout=20
        )

        return resposta.status_code in [200, 201, 204]

    except Exception:

        return False


# =========================
# ENVIO DO PEDIDO
# =========================

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

            "servico": servico,

            "descricao": descricao,

            "prazo": prazo,

            "forma_pagamento": pagamento,

            "status": "Novo"
        }

        sucesso = salvar_pedido(pedido)

        if sucesso:

            st.success(
                "✅ Solicitação enviada com sucesso!"
            )

            st.write(
                "Entraremos em contato para conversar sobre o orçamento."
            )

        else:

            st.error(
                "⚠️ Não foi possível enviar a solicitação. "
                "A configuração do banco de dados ainda precisa ser concluída."
            )


st.divider()


# =========================
# PAGAMENTO
# =========================

st.header("💳 Formas de pagamento")

st.info(
    "Pix disponível após aprovação do orçamento."
)

st.write(
    "O pagamento somente será solicitado depois que "
    "o serviço, o prazo e o valor forem combinados."
)

st.write(
    "Para pagamentos com cartão, será enviado um link de pagamento."
)

st.write(
    "Também é possível combinar transferência."
)

st.divider()


# =========================
# CONTATO
# =========================

st.header("🤝 Vamos trabalhar juntos?")

st.write(
    "Envie sua solicitação pelo formulário ou entre em contato "
    "para conversar sobre seu projeto."
)

col1, col2, col3 = st.columns(3)

with col1:

    st.write("📱 WhatsApp")

    st.write(WHATSAPP)


with col2:

    st.write("📧 E-mail")

    st.write(EMAIL)


with col3:

    st.write("📸 Instagram")

    st.write(INSTAGRAM)


st.divider()


# =========================
# RODAPÉ
# =========================

st.caption(
    "© 2026 Queren Serviços Digitais · Todos os direitos reservados."
)
