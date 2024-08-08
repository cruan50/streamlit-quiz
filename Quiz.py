import streamlit as st
import random

# Definir perguntas e respostas
questions = [
    {"question": "Qual a inclinação mínima recomendada para um telhado com telhas cerâmicas?", "options": ["10%", "15%", "30%", "45%"], "answer": "30%"},
    {"question": "Qual é a espessura recomendada do reboco interno?", "options": ["0.5cm", "1cm", "1.5cm", "2cm"], "answer": "1cm"},
    {"question": "Qual é o tipo de estaca indicado para terrenos sem presença de água e sem pedras ou pedriscos?", "options": ["Estaca hélice contínua", "Estaca pré-moldada", "Estaca escavada", "Estaca trado mecanizado"], "answer": "Estaca trado mecanizado"},
    {"question": "Quando é recomendada a aplicação do selador durante o processo de pintura interna?", "options": ["Antes do chapisco", "Depois do gesso", "Antes do reboco", "Depois da massa corrida"], "answer": "Depois do gesso"},
    {"question": "Qual é a altura ideal para instalar uma bancada de cozinha ou banheiro?", "options": ["70cm", "80cm", "90cm", "100cm"], "answer": "90cm"},
    {"question": "Qual é o tipo de argamassa recomendada para assentar porcelanatos de piso?", "options": ["AC1", "AC2", "AC3", "AC4"], "answer": "AC2"},
    {"question": "Qual deve ser a inclinação do telhado para telhas metálicas?", "options": ["5% a 10%", "10% a 15%", "15% a 20%", "20% a 25%"], "answer": "10% a 15%"},
    {"question": "Quando deve ser realizada a concretagem de uma laje?", "options": ["Antes das 7h da manhã", "Após as 8h da manhã", "No final da tarde", "A qualquer hora do dia"], "answer": "Após as 8h da manhã"},
    {"question": "Quantos furos de sondagem são recomendados para um terreno de 400m²?", "options": ["1 furo", "2 furos", "3 furos", "4 furos"], "answer": "2 furos"},
    {"question": "Qual o espaçamento recomendado do gabarito em relação aos eixos externos?", "options": ["1m", "1.5m", "2m", "2.5m"], "answer": "1.5m"},
    {"question": "O que deve ser feito antes da concretagem de lajes?", "options": ["Calcular o volume do concreto", "Conferir armadura", "Utilizar espaçador de armadura", "Todas as alternativas anteriores"], "answer": "Todas as alternativas anteriores"},
    {"question": "Qual material é recomendado para instalações de água fria?", "options": ["PVC soldável", "PPR", "PEX", "Cobre"], "answer": "PVC soldável"},
    {"question": "Em qual etapa deve-se instalar o forro de gesso?", "options": ["Após a instalação elétrica", "Antes do selador", "Antes do reboco", "Após o reboco"], "answer": "Após a instalação elétrica"},
    {"question": "Qual a espessura recomendada do reboco externo?", "options": ["1cm", "1.5cm", "2cm", "2.5cm"], "answer": "1.5cm"},
    {"question": "Qual é o primeiro passo para executar a pintura?", "options": ["Aplicar selador", "Aplicar massa corrida", "Lixar a parede", "Aplicar a tinta"], "answer": "Lixar a parede"},
    {"question": "Qual o consumo médio de argamassa AC2 para assentar porcelanato de piso?", "options": ["2kg/m²", "3kg/m²", "5kg/m²", "7kg/m²"], "answer": "5kg/m²"},
    {"question": "Qual é a altura mínima do gabarito?", "options": ["30cm", "40cm", "50cm", "60cm"], "answer": "50cm"},
    {"question": "Para que serve a sondagem do solo?", "options": ["Verificar a resistência do solo", "Identificar o tipo de solo", "Planejar as fundações", "Todas as alternativas anteriores"], "answer": "Todas as alternativas anteriores"},
    {"question": "O que é recomendado fazer antes da concretagem de uma laje?", "options": ["Calcular o volume do concreto", "Conferir armadura", "Utilizar espaçador de armadura", "Todas as alternativas anteriores"], "answer": "Todas as alternativas anteriores"},
    {"question": "Qual material é recomendado para instalações de esgoto?", "options": ["PVC esgoto série normal", "PVC esgoto série reforçada", "PPR", "Cobre"], "answer": "PVC esgoto série reforçada"},
    {"question": "Em qual etapa deve-se instalar as portas?", "options": ["Após o forro de gesso", "Antes do selador", "Antes do reboco", "Após o reboco"], "answer": "Após o forro de gesso"},
    {"question": "Qual é a primeira etapa da mobilização de uma obra?", "options": ["Placa de obra", "Fechamento da obra", "Limpeza do terreno", "Montar o canteiro de obras"], "answer": "Limpeza do terreno"},
    {"question": "Quando deve ser aplicada a massa corrida?", "options": ["Antes do selador", "Após o selador", "Antes da tinta", "Após a tinta"], "answer": "Após o selador"},
    {"question": "Qual a espessura recomendada do reboco interno?", "options": ["0.5cm", "1cm", "1.5cm", "2cm"], "answer": "1cm"},
    {"question": "Qual o tipo de telha recomendado para inclinações de telhado de 10% a 15%?", "options": ["Telhas metálicas", "Telhas cerâmicas", "Telhas de fibrocimento", "Telhas de vidro"], "answer": "Telhas metálicas"},
    {"question": "Qual o espaçamento recomendado entre furos de sondagem?", "options": ["1m", "1.5m", "2m", "2.5m"], "answer": "2m"},
    {"question": "Em qual etapa deve-se aplicar o selador?", "options": ["Antes do reboco", "Após o reboco", "Antes da massa corrida", "Após a massa corrida"], "answer": "Após o reboco"},
    {"question": "Qual o consumo de argamassa para assentar porcelanatos de parede?", "options": ["2kg/m²", "3kg/m²", "5kg/m²", "7kg/m²"], "answer": "5kg/m²"},
    {"question": "Qual material é recomendado para instalações de gás?", "options": ["PVC soldável", "PPR", "Cobre", "PEAD"], "answer": "Cobre"},
]

# Função para calcular o resultado
def calculate_score(responses, selected_questions):
    score = 0
    for i, response in enumerate(responses):
        if response == selected_questions[i]["answer"]:
            score += 1
    return score

# Função principal
def main():
    st.title("Quiz de Engenharia de Construção")
    st.write("""
        Bem-vindo ao Quiz de Engenharia de Construção! 
        Responda as perguntas abaixo para testar seus conhecimentos sobre diferentes aspectos da construção civil.
    """)

    if 'selected_questions' not in st.session_state:
        st.session_state.selected_questions = random.sample(questions, 10)
        st.session_state.responses = [None] * 10
        st.session_state.submitted = False

    selected_questions = st.session_state.selected_questions
    responses = st.session_state.responses

    if not st.session_state.submitted:
        for i, question in enumerate(selected_questions):
            responses[i] = st.radio(f"Q{i+1}: {question['question']}", question['options'], index=None, key=f"q{i}")

        if st.button("Enviar"):
            st.session_state.submitted = True
            st.experimental_rerun()

    if st.session_state.submitted:
        score = calculate_score(responses, selected_questions)
        st.write(f"Você acertou {score} de {len(selected_questions)} perguntas.")
        for i, question in enumerate(selected_questions):
            st.write(f"**Q{i+1}: {question['question']}**")
            st.write(f"Resposta correta: {question['answer']}")
            st.write(f"Sua resposta: {responses[i]}")
            if responses[i] == question['answer']:
                st.success("Correto!")
            else:
                st.error("Incorreto.")

        if st.button("Resetar"):
            st.session_state.selected_questions = random.sample(questions, 10)
            st.session_state.responses = [None] * 10
            st.session_state.submitted = False

    st.write("Desenvolvido por [CR Engenharia](https://www.instagram.com/cr_engenhariaaa/)")

if __name__ == "__main__":
    main()
