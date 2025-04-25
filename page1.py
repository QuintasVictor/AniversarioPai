from operator import index

import streamlit as st
from PIL import Image
import time
import os
import math

# =========================
# CONFIGURAÇÃO INICIAL
# =========================

imagens_dir = "imagens"
lista_imagens = os.listdir(imagens_dir)
lista_imagens = [img for img in lista_imagens if img.endswith(('.png', '.jpg', '.jpeg'))]
qntd_imagens = len(lista_imagens)

frases = [
    "Você é um pai e um esposo maravilhoso, e merece ser celebrado!",
    "Somos muito sortudos por ter alguém tão incrível nas nossas vidas",
    "Você é um exemplo pra gente!",
    "Te desejamos muito vinho, almoços da mamãe e vitórias no xadrez!",
    "Temos muito orgulho de você",
    "Você nos inspira a ser melhor e almejar o melhor",
    "Feliz Aniversário, Pai! \nVocê é muito amado pela sua família ♥"
]
qntd_frases = len(frases)

img_por_frase = math.ceil(qntd_imagens/qntd_frases)
intervalo = 4


#=======================================
if "pagina" not in st.session_state:
    st.session_state.pagina = 1
if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0
if "finished" not in st.session_state:
    st.session_state.finished = False
#=======================================


if st.session_state.pagina == 1:
    st.title("Feliz Aniversário, Pai! 🎉")
    st.markdown("""
    <p style='font-size:22px;'>Hoje é o seu dia e queremos te mostrar algo especial...</p>
    """, unsafe_allow_html=True)

    if st.button("Vamos começar? 👉"):
        st.session_state.pagina = 2
        st.session_state.slide_idx = 0
        st.session_state.finished = False
        st.rerun()

if st.session_state.pagina == 2:

    placeholder_text = st.empty()
    placeholder_img = st.empty()
    audio_file = open("musica/IRA - envelheço na cidade.mp3", "rb")
    st.audio(audio_file.read(), format = "audio/mp3", start_time=48, loop=True, autoplay=True)

    if not st.session_state.finished:
        idx = st.session_state.slide_idx

        # Escolhe a frase a exibir para este índice
        frase_idx = min(idx // img_por_frase, qntd_imagens - 1)
        placeholder_text.markdown(
            f"<h2 style='text-align:center;'>{frases[frase_idx]}</h2>",
            unsafe_allow_html=True,
        )

        # Exibe a imagem correspondente
        img_path = os.path.join(imagens_dir, lista_imagens[idx])
        placeholder_img.image(Image.open(img_path), use_container_width=True)

        # Aguarda e avança para a próxima imagem
        time.sleep(intervalo)
        if st.session_state.slide_idx < qntd_imagens - 1:
            st.session_state.slide_idx += 1
            st.rerun()
        else:
            st.session_state.finished = True
            st.rerun()

    # 4) Quando terminar, mostra tela final + botão de reiniciar
    else:
        placeholder_text.markdown(
            "<h2 style='text-align:center;'>"
            "🎉 Fim da história! Te amo, pai! 🎉"
            "</h2>",
            unsafe_allow_html=True,
        )
        placeholder_img.empty()
        placeholder_img.empty()

        # cria 3 colunas: a do meio é maior
        col1, col2, col3 = st.columns([1, 6, 1])

        # coloca o botão só na coluna do meio
        with col2:
            if st.button("🔄 Reiniciar"):
                st.session_state.pagina = 1
                st.session_state.slide_idx = 0
                st.session_state.finished = False
                st.rerun()
