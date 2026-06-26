import streamlit as st

# ============================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================

st.set_page_config(
    page_title="99 Campaign Intelligence",
    page_icon="🚕",
    layout="wide"
)

# ============================================
# CABEÇALHO
# ============================================

st.title("🚕 99 Campaign Intelligence")
st.caption(
    "Assistente inteligente para análise de campanhas de CRM Mobility"
)

st.divider()

# ============================================
# FORMULÁRIO
# ============================================

col1, col2 = st.columns([1.3,1])

with col1:

    st.subheader("Campanha")

    tipo = st.selectbox(
        "Tipo de comunicação",
        [
            "Push",
            "Email",
            "Banner",
            "Pop Up",
            "XPanel"
        ]
    )

    texto = st.text_area(
        "Copy da comunicação",
        placeholder="Cole aqui a copy da comunicação...",
        height=180
    )

    # Apenas comunicações visuais precisam de imagem
    if tipo in ["Banner", "Pop Up", "XPanel"]:

        imagem = st.file_uploader(
            "Criativo da campanha",
            type=["png", "jpg", "jpeg"]
        )

with col2:

    st.subheader("Informações")

    publico = st.selectbox(
        "Público",
        [
            "New",
            "Ativo",
            "Backflow"
        ]
    )

    objetivo = st.selectbox(
        "Objetivo",
        [
            "Aquisição",
            "Reativação",
            "Retenção",
            "Frequência",
            "Fidelização",
            "Cupom",
            "Cashback"
        ]
    )

st.divider()

# ============================================
# BOTÃO
# ============================================

if st.button("🚀 Analisar Campanha", use_container_width=True):

    st.success("Sua campanha foi enviada para análise.")

    st.info(
        """
        Em breve esta tela será preenchida pela IA com:

        • Campaign Score

        • DNA 99

        • Previsão de CTR

        • Comparação com campanhas históricas

        • Pontos fortes

        • Pontos de melhoria

        • Sugestão de nova copy
        """
    )
