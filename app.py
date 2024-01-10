# app.py
import streamlit as st
import pandas as pd
import numpy as np

# URL da imagem
imagem_url = "https://scontent-iad3-2.xx.fbcdn.net/v/t1.6435-9/58968067_1031332203722900_3181178243449356288_n.jpg?stp=cp0_dst-jpg_e15_p75x225_q65&_nc_cat=103&ccb=1-7&_nc_sid=947906&_nc_ohc=yDzP2UR5kpYAX_3g2NW&_nc_ht=scontent-iad3-2.xx&oh=00_AfA8nnyzZ8mfS9zpT_uksNvwanMyxbWtiomABbe-oGUzZQ&oe=65C61727"

# Adicionar a div com imagem e aplicar estilos CSS
st.markdown(
    f"""
    <div style="margin-top: -25px; text-align: center;">
        <img src="{imagem_url}" alt="Imagem" width="150">
    </div>
    """,
    unsafe_allow_html=True)

# Adicionar o título
st.title('Igreja Presbiteriana do Caminho')


st.markdown("## <u>Palavra 📖</u>", unsafe_allow_html=True)
palavra_gravacao = "xxx"
st.markdown(f"[Gravação]({palavra_gravacao})")



abertura="""
8 Pela fé Abraão, quando chamado, obedeceu e dirigiu-se a um lugar que mais tarde receberia como herança, embora não soubesse para onde estava indo. 9 Pela fé peregrinou na terra prometida como se estivesse em terra estranha; viveu em tendas, bem como Isaque e Jacó, co-herdeiros da mesma promessa. 10 Pois ele esperava a cidade que tem alicerces, cujo arquiteto e edificador é Deus.

11 Pela fé Abraão — e também a própria Sara, apesar de estéril e avançada em idade — recebeu poder para gerar um filho,[a] porque considerou fiel aquele que lhe havia feito a promessa. 12 Assim, daquele homem já sem vitalidade originaram-se descendentes tão numerosos como as estrelas do céu e tão incontáveis como a areia da praia do mar.

13 Todos estes viveram pela fé, e morreram sem receber o que tinha sido prometido; viram-no de longe e de longe o saudaram, reconhecendo que eram estrangeiros e peregrinos na terra. 14 Os que assim falam mostram que estão buscando uma pátria. 15 Se estivessem pensando naquela de onde saíram, teriam oportunidade de voltar. 16 Em vez disso, esperavam eles uma pátria melhor, isto é, a pátria celestial. Por essa razão Deus não se envergonha de ser chamado o Deus deles, e lhes preparou uma cidade.

17 Pela fé Abraão, quando Deus o pôs à prova, ofereceu Isaque como sacrifício. Aquele que havia recebido as promessas estava a ponto de sacrificar o seu único filho, 18 embora Deus lhe tivesse dito: “Por meio de Isaque a sua descendência[b] será considerada”[c]. 19 Abraão levou em conta que Deus pode ressuscitar os mortos e, figuradamente, recebeu Isaque de volta dentre os mortos.

20 Pela fé Isaque abençoou Jacó e Esaú com respeito ao futuro deles.

21 Pela fé Jacó, à beira da morte, abençoou cada um dos filhos de José e adorou a Deus, apoiado na extremidade do seu bordão.

22 Pela fé José, no fim da vida, fez menção do êxodo dos israelitas do Egito e deu instruções acerca dos seus próprios ossos.."
"""
confissao="""
Cântico de peregrinação. De Davi.
1 Senhor, o meu coração não é orgulhoso,
e os meus olhos não são arrogantes.
Não me envolvo com coisas grandiosas
nem maravilhosas demais para mim.
2Pelo contrário, acalmei e aquietei a minha alma.
Sou como uma criança desmamada pela sua mãe;
a minha alma é como essa criança.
3Ponha a sua esperança no Senhor, ó Israel,
desde agora e para sempre!
"""

palavra="""
A Torre de Babel
11 No mundo todo havia apenas uma língua, um só modo de falar.

2 Saindo os homens do[a] Oriente, encontraram uma planície em Sinear e ali se fixaram.

3 Disseram uns aos outros: “Vamos fazer tijolos e queimá-los bem”. Usavam tijolos em lugar de pedras, e piche em vez de argamassa. 4 Depois disseram: “Vamos construir uma cidade, com uma torre que alcance os céus. Assim nosso nome será famoso e não seremos espalhados pela face da terra”.

5 O Senhor desceu para ver a cidade e a torre que os homens estavam construindo. 6 E disse o Senhor: “Eles são um só povo e falam uma só língua, e começaram a construir isso. Em breve nada poderá impedir o que planejam fazer. 7 Venham, desçamos e confundamos a língua que falam, para que não entendam mais uns aos outros”.

8 Assim o Senhor os dispersou dali por toda a terra, e pararam de construir a cidade. 9 Por isso foi chamada Babel[b], porque ali o Senhor confundiu a língua de todo o mundo. Dali o Senhor os espalhou por toda a terra.

O Chamado de Abrão
12 Então o Senhor disse a Abrão: “Saia da sua terra, do meio dos seus parentes e da casa de seu pai, e vá para a terra que eu lhe mostrarei.

2 “Farei de você um grande povo,
    e o abençoarei.
Tornarei famoso o seu nome,
    e você será uma bênção.
3 Abençoarei os que o abençoarem
e amaldiçoarei os que o amaldiçoarem;
e por meio de você
    todos os povos da terra
    serão abençoados”.

"""

abertura_detalhes = st.checkbox("Abertura: Hebreus 11.8-22")
if abertura_detalhes:
    # Mostrar texto adicional quando o checkbox está marcado
    st.write(abertura)
confissao_detalhes = st.checkbox("Confissão: Salmos 131")
if confissao_detalhes:
    # Mostrar texto adicional quando o checkbox está marcado
    st.write(confissao)

palavra_detalhes = st.checkbox("Palavra: Gênesis 11.1-9; 12.1-3 (Pr. Bernardo Cho)")
if palavra_detalhes:
    # Mostrar texto adicional quando o checkbox está marcado
    st.write(palavra)


st.markdown("## <u>Louvor 🙌</u>", unsafe_allow_html=True)
louvor1 = "https:www.letras.mus.br/aline-barros/178166/"
louvor2 = "https://www.letras.com/carlinhos-felix/547794/"
louvor3 = "https://www.letras.mus.br/aline-barros/1343760/"
louvor4 = "https://www.letras.mus.br/diante-do-trono/1903147/"


st.markdown(f"[Ao Único]({louvor1})")
st.markdown(f"[Grande é o Senhor]({louvor2})")
st.markdown(f"[Renova me]({louvor3})")
st.markdown(f"[Quem nos separará]({louvor4})")


st.markdown("## <u>Aviso 📢</u>", unsafe_allow_html=True)
st.write("""- Para ofertas e dízimos, seguem os dados bancários da IPC:

		Santander - 033

		Ag. 0108

		Cc. 13007643-7

		Igreja Presbiteriana do Caminho

		pix CNPJ: 48.792.102/0001-13

		📣Por favor identifica dízimos com o final 👉,01 nos depósitos 📣
"""
)
st.write("""- Devocional Terças e Quintas às 21hs :

https://us04web.zoom.us/j/9507062229?pwd=OVFWY0JudTVIdklnazB1VUNsNGhDUT09""")

st.write("- Acampamento 13/02/2024, falar com a Sigrid")
st.write("- Confraternização 05/06/2024, Em breve")

st.markdown("## <u>Sugestão 💡</u>", unsafe_allow_html=True)
st.markdown(f"[Clique para enviar as sugestões]({"xxx"})")



# Adicionar uma barra lateral com controles interativos
st.sidebar.header('Data')
selected_variable = st.sidebar.selectbox('Selecione a data:', ['2024/01/07', '2024/01/14'])

# Executar o aplicativo usando o comando streamlit run
# Exemplo: streamlit run app.py
