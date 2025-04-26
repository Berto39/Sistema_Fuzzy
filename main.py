import streamlit as st
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from funcoes_fuzzy import criar_variaveis, criar_funcoes_pertinencia
from regras_fuzzy import carregar_regras, calcular_eficiencia

# Configuração da página
st.set_page_config(
    page_title="Sistema de Eficiência Fuzzy",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Adicionar CSS para melhorar a aparência
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid #E5E7EB;
    }
    .subheader {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2563EB;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .card {
        background-color: #F9FAFB;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
    }
    .metric-value {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
    }
    .metric-label {
        font-size: 1rem;
        text-align: center;
        color: #6B7280;
    }
    .input-section {
        background-color: #F3F4F6;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #E5E7EB;
        color: #6B7280;
    }
</style>
""", unsafe_allow_html=True)


# Função para criar variáveis e funções de pertinência
@st.cache_data
def criar_variaveis_e_funcoes():
    Quantidade_produtos, Quantidade_pessoas, Quantidade_horas, Qualidade_servico_nota, eficiencia = criar_variaveis()
    Quantidade_baixa, Quantidade_media, Quantidade_alta, pesoas_baixa, pesoas_media, pesoas_alta, Quantidade_horas_insuficiente, Quantidade_horas_baixa, Quantidade_horas_media, Quantidade_horas_alta, Quantidade_horas_excessiva, Qualidade_pessima, Qualidade_baixa, Qualidade_mediana, Qualidade_boa, Qualidade_otima, eficiencia_pessima, eficiencia_baixa, eficiencia_media, eficiencia_alta, eficiencia_excelente = criar_funcoes_pertinencia(
        Quantidade_produtos, Quantidade_pessoas, Quantidade_horas, Qualidade_servico_nota, eficiencia
    )
    return Quantidade_produtos, Quantidade_pessoas, Quantidade_horas, Qualidade_servico_nota, eficiencia, Quantidade_baixa, Quantidade_media, Quantidade_alta, pesoas_baixa, pesoas_media, pesoas_alta, Quantidade_horas_insuficiente, Quantidade_horas_baixa, Quantidade_horas_media, Quantidade_horas_alta, Quantidade_horas_excessiva, Qualidade_pessima, Qualidade_baixa, Qualidade_mediana, Qualidade_boa, Qualidade_otima, eficiencia_pessima, eficiencia_baixa, eficiencia_media, eficiencia_alta, eficiencia_excelente


# Função para classificar a eficiência
def classificar_eficiencia(valor):
    if valor < 2:
        return "Péssima", "#FF0000", "Desempenho crítico que requer intervenção imediata."
    elif valor < 4:
        return "Baixa", "#FF8C00", "Abaixo do esperado. Melhorias significativas são necessárias."
    elif valor < 6:
        return "Média", "#FFD700", "Desempenho aceitável, mas com espaço para melhorias."
    elif valor < 8:
        return "Alta", "#4CAF50", "Bom desempenho com poucos ajustes necessários."
    else:
        return "Excelente", "#008000", "Desempenho excepcional. Mantenha e compartilhe as boas práticas."


# Função para criar gráfico de medidor (gauge)
def criar_gauge(valor, classificacao, cor):
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=valor,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Eficiência", 'font': {'size': 24}},
        delta={'reference': 5, 'increasing': {'color': "#008000"}, 'decreasing': {'color': "#FF0000"}},
        gauge={
            'axis': {'range': [0, 10], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': cor},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 2], 'color': '#FF0000'},
                {'range': [2, 4], 'color': '#FF8C00'},
                {'range': [4, 6], 'color': '#FFD700'},
                {'range': [6, 8], 'color': '#4CAF50'},
                {'range': [8, 10], 'color': '#008000'}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': valor
            }
        }
    ))
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
    )
    return fig


# Função para criar gráfico radar
def criar_radar(quantidade, pessoas, horas, qualidade, eficiencia):
    categorias = ['Quantidade', 'Pessoas', 'Horas', 'Qualidade', 'Eficiência']

    # Normalizar valores para escala de 0-10
    valores = [
        quantidade * 10 / 40,  # Normalizar quantidade (0-40 → 0-10)
        pessoas * 10 / 20,  # Normalizar pessoas (0-20 → 0-10)
        horas,  # Horas já estão em escala 0-10
        qualidade,  # Qualidade já está em escala 0-10
        eficiencia  # Eficiência já está em escala 0-10
    ]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=valores,
        theta=categorias,
        fill='toself',
        name='Valores Atuais',
        line_color='#2563EB',
        fillcolor='rgba(59, 130, 246, 0.5)'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )
        ),
        showlegend=False,
        height=350,
        margin=dict(l=20, r=20, t=30, b=20),
    )
    return fig


# Função para criar gráfico de pertinência
def criar_grafico_pertinencia(universo, funcoes, labels, valor_atual, titulo):
    fig, ax = plt.subplots(figsize=(10, 4))

    for i, (funcao, label) in enumerate(zip(funcoes, labels)):
        ax.plot(universo, funcao, label=label)

    # Linha vertical para o valor atual
    ax.axvline(x=valor_atual, color='k', linestyle='--', label=f'Valor: {valor_atual}')

    ax.set_title(titulo)
    ax.legend(loc='upper right')
    ax.set_ylim([0, 1.1])
    ax.grid(True, linestyle='--', alpha=0.7)

    return fig


# Título principal e descrição
st.markdown('<div class="main-header">Sistema Inteligente de Análise de Eficiência</div>', unsafe_allow_html=True)

st.markdown("""
Este sistema utiliza lógica fuzzy (conjuntos difusos) para avaliar a eficiência de processos com base em quatro variáveis-chave:
quantidade de produção, número de pessoas, horas trabalhadas e qualidade do serviço/produto.
""")

# Criar abas para organizar a interface
tab1, tab2, tab3 = st.tabs(["📝 Entrada de Dados", "📊 Resultados", "ℹ️ Análise Detalhada"])

# Tab 1: Entrada de Dados
with tab1:
    st.markdown('<div class="subheader">Inserir Parâmetros</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
        # Opção para escolher entre slider ou input numérico
        input_method = st.radio("Método de entrada:", ["Sliders", "Campos numéricos"])

        if input_method == "Sliders":
            Quantidade_digitada = st.slider('Quantidade de Produtos', 0, 40, 20,
                                            help="Quantidade de produtos produzidos (0-40)")
            pessoas_digitada = st.slider('Quantidade de Pessoas', 0, 20, 10,
                                         help="Número de pessoas envolvidas no processo (0-20)")
            horas_digitada = st.slider('Quantidade de Horas', 0.0, 10.0, 5.0, help="Horas trabalhadas (0-10)")
            qualidade_digitada = st.slider('Qualidade do Serviço', 0.0, 10.0, 7.0,
                                           help="Nota da qualidade do serviço ou produto (0-10)")
        else:
            Quantidade_digitada = st.number_input('Quantidade de Produtos', 0, 40, 20,
                                                  help="Quantidade de produtos produzidos (0-40)")
            pessoas_digitada = st.number_input('Quantidade de Pessoas', 0, 20, 10,
                                               help="Número de pessoas envolvidas no processo (0-20)")
            horas_digitada = st.number_input('Quantidade de Horas', 0.0, 10.0, 5.0, help="Horas trabalhadas (0-10)")
            qualidade_digitada = st.number_input('Qualidade do Serviço', 0.0, 10.0, 7.0,
                                                 help="Nota da qualidade do serviço ou produto (0-10)")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Orientações para os Parâmetros")
        st.markdown("""
        - **Quantidade de Produtos**: Número total de unidades produzidas no período
        - **Quantidade de Pessoas**: Tamanho da equipe envolvida no processo
        - **Quantidade de Horas**: Tempo total gasto no processo produtivo
        - **Qualidade do Serviço**: Avaliação da qualidade do produto final
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Botão de calcular com estilo personalizado
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #2563EB;
        color: white;
        font-size: 16px;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 8px;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #1E40AF;
    }
    </style>
    """, unsafe_allow_html=True)

    calcular = st.button("CALCULAR EFICIÊNCIA")

# Tab 2: Resultados
with tab2:
    if calcular or 'eficiencia_resultado' in st.session_state:
        # Criar variáveis e funções de pertinência
        Quantidade_produtos, Quantidade_pessoas, Quantidade_horas, Qualidade_servico_nota, eficiencia, Quantidade_baixa, Quantidade_media, Quantidade_alta, pesoas_baixa, pesoas_media, pesoas_alta, Quantidade_horas_insuficiente, Quantidade_horas_baixa, Quantidade_horas_media, Quantidade_horas_alta, Quantidade_horas_excessiva, Qualidade_pessima, Qualidade_baixa, Qualidade_mediana, Qualidade_boa, Qualidade_otima, eficiencia_pessima, eficiencia_baixa, eficiencia_media, eficiencia_alta, eficiencia_excelente = criar_variaveis_e_funcoes()

        # Calculando pertinências
        per_quantidade_baixa = fuzz.interp_membership(Quantidade_produtos, Quantidade_baixa, Quantidade_digitada)
        per_quantidade_media = fuzz.interp_membership(Quantidade_produtos, Quantidade_media, Quantidade_digitada)
        per_quantidade_alta = fuzz.interp_membership(Quantidade_produtos, Quantidade_alta, Quantidade_digitada)

        per_pesoas_baixa = fuzz.interp_membership(Quantidade_pessoas, pesoas_baixa, pessoas_digitada)
        per_pesoas_media = fuzz.interp_membership(Quantidade_pessoas, pesoas_media, pessoas_digitada)
        per_pesoas_alta = fuzz.interp_membership(Quantidade_pessoas, pesoas_alta, pessoas_digitada)

        per_quantidade_horas_insuficiente = fuzz.interp_membership(Quantidade_horas, Quantidade_horas_insuficiente,
                                                                   horas_digitada)
        per_quantidade_horas_baixa = fuzz.interp_membership(Quantidade_horas, Quantidade_horas_baixa, horas_digitada)
        per_quantidade_horas_media = fuzz.interp_membership(Quantidade_horas, Quantidade_horas_media, horas_digitada)
        per_quantidade_horas_alta = fuzz.interp_membership(Quantidade_horas, Quantidade_horas_alta, horas_digitada)
        per_quantidade_horas_excessiva = fuzz.interp_membership(Quantidade_horas, Quantidade_horas_excessiva,
                                                                horas_digitada)

        per_qualidade_pesssima = fuzz.interp_membership(Qualidade_servico_nota, Qualidade_pessima, qualidade_digitada)
        per_qualidade_baixa = fuzz.interp_membership(Qualidade_servico_nota, Qualidade_baixa, qualidade_digitada)
        per_qualidade_mediana = fuzz.interp_membership(Qualidade_servico_nota, Qualidade_mediana, qualidade_digitada)
        per_qualidade_boa = fuzz.interp_membership(Qualidade_servico_nota, Qualidade_boa, qualidade_digitada)
        per_qualidade_otima = fuzz.interp_membership(Qualidade_servico_nota, Qualidade_otima, qualidade_digitada)

        # Aplicar regras
        agregacao_total = carregar_regras(
            per_quantidade_baixa, per_quantidade_media, per_quantidade_alta,
            per_pesoas_baixa, per_pesoas_media, per_pesoas_alta,
            per_quantidade_horas_insuficiente, per_quantidade_horas_baixa, per_quantidade_horas_media,
            per_quantidade_horas_alta, per_quantidade_horas_excessiva,
            per_qualidade_pesssima, per_qualidade_baixa, per_qualidade_mediana,
            per_qualidade_boa, per_qualidade_otima,
            eficiencia_pessima, eficiencia_baixa, eficiencia_media, eficiencia_alta, eficiencia_excelente
        )

        # Defuzzificação
        eficiencia_resultado = calcular_eficiencia(agregacao_total, eficiencia)
        st.session_state.eficiencia_resultado = eficiencia_resultado

        # Classificar resultado
        classificacao, cor, descricao = classificar_eficiencia(eficiencia_resultado)

        # Exibir resultados
        st.markdown('<div class="subheader">Resultados da Avaliação</div>', unsafe_allow_html=True)

        # Mostrar resultados em colunas
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            # Medidor de eficiência
            gauge_chart = criar_gauge(eficiencia_resultado, classificacao, cor)
            st.plotly_chart(gauge_chart, use_container_width=True)

            # Classificação
            st.markdown(f"""
            <p style='text-align:center; font-size:1.8rem; font-weight:bold; color:{cor};'>{classificacao}</p>
            <p style='text-align:center;'>{descricao}</p>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            # Gráfico radar
            radar_chart = criar_radar(Quantidade_digitada, pessoas_digitada, horas_digitada, qualidade_digitada,
                                      eficiencia_resultado)
            st.plotly_chart(radar_chart, use_container_width=True)

            # Resumo dos valores
            st.markdown("### Resumo dos Parâmetros")
            dados = {
                "Parâmetro": ["Quantidade", "Pessoas", "Horas", "Qualidade", "Eficiência"],
                "Valor": [Quantidade_digitada, pessoas_digitada, horas_digitada, qualidade_digitada,
                          f"{eficiencia_resultado:.2f}"]
            }
            st.table(dados)
            st.markdown('</div>', unsafe_allow_html=True)

        # Gráfico de área de agregação
        st.markdown('<div class="subheader">Gráfico de Defuzzificação</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">', unsafe_allow_html=True)
        fig_agg, ax_agg = plt.subplots(figsize=(10, 4))
        ax_agg.plot(eficiencia, agregacao_total, 'b', linewidth=1.5, label='Agregação')
        # Linha vertical para o valor de eficiência
        ax_agg.axvline(x=eficiencia_resultado, color='r', linestyle='--',
                       label=f'Eficiência: {eficiencia_resultado:.2f}')
        ax_agg.set_title('Resultado da Agregação e Defuzzificação')
        ax_agg.legend()
        ax_agg.grid(True, linestyle='--', alpha=0.7)
        st.pyplot(fig_agg)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info(
            "Por favor, insira os parâmetros na aba 'Entrada de Dados' e clique em Calcular Eficiência para ver os resultados.")

# Tab 3: Análise Detalhada
with tab3:
    if calcular or 'eficiencia_resultado' in st.session_state:
        st.markdown('<div class="subheader">Análise de Pertinência</div>', unsafe_allow_html=True)
        st.markdown("""
        Esta seção mostra como os valores de entrada se relacionam com as funções de pertinência fuzzy para cada variável.
        A linha tracejada representa o valor atual inserido.
        """)

        # Gráficos de pertinência para cada variável
        st.markdown('<div class="card">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            # Gráfico de pertinência da quantidade
            fig_quantidade = criar_grafico_pertinencia(
                Quantidade_produtos,
                [Quantidade_baixa, Quantidade_media, Quantidade_alta],
                ["Baixa", "Média", "Alta"],
                Quantidade_digitada,
                "Funções de Pertinência - Quantidade"
            )
            st.pyplot(fig_quantidade)

            # Gráfico de pertinência das horas
            fig_horas = criar_grafico_pertinencia(
                Quantidade_horas,
                [Quantidade_horas_insuficiente, Quantidade_horas_baixa, Quantidade_horas_media, Quantidade_horas_alta,
                 Quantidade_horas_excessiva],
                ["Insuficiente", "Baixa", "Média", "Alta", "Excessiva"],
                horas_digitada,
                "Funções de Pertinência - Horas"
            )
            st.pyplot(fig_horas)

        with col2:
            # Gráfico de pertinência das pessoas
            fig_pessoas = criar_grafico_pertinencia(
                Quantidade_pessoas,
                [pesoas_baixa, pesoas_media, pesoas_alta],
                ["Baixa", "Média", "Alta"],
                pessoas_digitada,
                "Funções de Pertinência - Pessoas"
            )
            st.pyplot(fig_pessoas)

            # Gráfico de pertinência da qualidade
            fig_qualidade = criar_grafico_pertinencia(
                Qualidade_servico_nota,
                [Qualidade_pessima, Qualidade_baixa, Qualidade_mediana, Qualidade_boa, Qualidade_otima],
                ["Péssima", "Baixa", "Mediana", "Boa", "Ótima"],
                qualidade_digitada,
                "Funções de Pertinência - Qualidade"
            )
            st.pyplot(fig_qualidade)
        st.markdown('</div>', unsafe_allow_html=True)

        # Valores de pertinência
        st.markdown('<div class="subheader">Valores de Pertinência</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">', unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown("#### Quantidade")
            st.write(f"Baixa: {per_quantidade_baixa:.2f}")
            st.write(f"Média: {per_quantidade_media:.2f}")
            st.write(f"Alta: {per_quantidade_alta:.2f}")

        with col2:
            st.markdown("#### Pessoas")
            st.write(f"Baixa: {per_pesoas_baixa:.2f}")
            st.write(f"Média: {per_pesoas_media:.2f}")
            st.write(f"Alta: {per_pesoas_alta:.2f}")

        with col3:
            st.markdown("#### Horas")
            st.write(f"Insuficiente: {per_quantidade_horas_insuficiente:.2f}")
            st.write(f"Baixa: {per_quantidade_horas_baixa:.2f}")
            st.write(f"Média: {per_quantidade_horas_media:.2f}")
            st.write(f"Alta: {per_quantidade_horas_alta:.2f}")
            st.write(f"Excessiva: {per_quantidade_horas_excessiva:.2f}")

        with col4:
            st.markdown("#### Qualidade")
            st.write(f"Péssima: {per_qualidade_pesssima:.2f}")
            st.write(f"Baixa: {per_qualidade_baixa:.2f}")
            st.write(f"Mediana: {per_qualidade_mediana:.2f}")
            st.write(f"Boa: {per_qualidade_boa:.2f}")
            st.write(f"Ótima: {per_qualidade_otima:.2f}")

        st.markdown('</div>', unsafe_allow_html=True)

        # Gráfico das funções de pertinência de eficiência
        st.markdown('<div class="subheader">Funções de Pertinência - Eficiência</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">', unsafe_allow_html=True)

        fig_eficiencia, ax_efi = plt.subplots(figsize=(10, 4))
        ax_efi.plot(eficiencia, eficiencia_pessima, 'r', label='Péssima')
        ax_efi.plot(eficiencia, eficiencia_baixa, 'orange', label='Baixa')
        ax_efi.plot(eficiencia, eficiencia_media, 'y', label='Média')
        ax_efi.plot(eficiencia, eficiencia_alta, 'g', label='Alta')
        ax_efi.plot(eficiencia, eficiencia_excelente, 'b', label='Excelente')
        ax_efi.axvline(x=eficiencia_resultado, color='k', linestyle='--',
                       label=f'Resultado: {eficiencia_resultado:.2f}')
        ax_efi.set_title('Funções de Pertinência - Eficiência')
        ax_efi.legend()
        ax_efi.grid(True, linestyle='--', alpha=0.7)

        st.pyplot(fig_eficiencia)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info(
            "Por favor, insira os parâmetros na aba 'Entrada de Dados' e clique em Calcular Eficiência para ver a análise detalhada.")

# Rodapé
st.markdown('<div class="footer">Sistema de Avaliação de Eficiência baseado em Lógica Fuzzy</div>',
            unsafe_allow_html=True)

# Adicionar requisitos de pacotes
# Lembre-se de instalar: pip install streamlit numpy matplotlib skfuzzy plotly
