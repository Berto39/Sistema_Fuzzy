import numpy as np
import skfuzzy as fuzz

def criar_variaveis():
    Quantidade_produtos = np.arange(0, 41, 1)
    Quantidade_pessoas = np.arange(0, 21, 1)
    Quantidade_horas = np.arange(0, 11, 1)
    Qualidade_servico_nota = np.arange(0, 11, 1)
    eficiencia = np.arange(0, 11, 1)
    return Quantidade_produtos, Quantidade_pessoas, Quantidade_horas, Qualidade_servico_nota, eficiencia

def criar_funcoes_pertinencia(Quantidade_produtos, Quantidade_pessoas, Quantidade_horas, Qualidade_servico_nota, eficiencia):
    # Quantidade de produtos
    Quantidade_baixa = fuzz.trapmf(Quantidade_produtos, [0, 0, 10, 20])
    Quantidade_media = fuzz.trimf(Quantidade_produtos, [10, 20, 30])
    Quantidade_alta = fuzz.trapmf(Quantidade_produtos, [20, 30, 40, 40])

    # Quantidade de pessoas
    pesoas_baixa = fuzz.trapmf(Quantidade_pessoas, [0, 0, 5, 10])
    pesoas_media = fuzz.trimf(Quantidade_pessoas, [5, 10, 15])
    pesoas_alta = fuzz.trapmf(Quantidade_pessoas, [10, 15, 20, 20])

    # Quantidade de horas
    Quantidade_horas_insuficiente = fuzz.trapmf(Quantidade_horas, [0, 0, 1, 3])
    Quantidade_horas_baixa = fuzz.trapmf(Quantidade_horas, [1, 2, 3, 4])
    Quantidade_horas_media = fuzz.trapmf(Quantidade_horas, [3, 4, 5, 6])
    Quantidade_horas_alta = fuzz.trapmf(Quantidade_horas, [5, 6, 7, 8])
    Quantidade_horas_excessiva = fuzz.trapmf(Quantidade_horas, [7, 9, 10, 10])

    # Qualidade do serviço
    Qualidade_pessima = fuzz.trapmf(Qualidade_servico_nota, [0, 0, 1, 3])
    Qualidade_baixa = fuzz.trapmf(Qualidade_servico_nota, [1, 2, 3, 4])
    Qualidade_mediana = fuzz.trapmf(Qualidade_servico_nota, [3, 4, 5, 6])
    Qualidade_boa = fuzz.trapmf(Qualidade_servico_nota, [5, 6, 7, 8])
    Qualidade_otima = fuzz.trapmf(Qualidade_servico_nota, [7, 9, 10, 10])

    # Eficiência (atualizado para intervalo de 0 a 10)
    eficiencia_pessima = fuzz.trapmf(eficiencia, [0, 0, 1, 3])
    eficiencia_baixa = fuzz.trapmf(eficiencia, [1, 2, 3, 4])
    eficiencia_media = fuzz.trapmf(eficiencia, [3, 4, 5, 6])
    eficiencia_alta = fuzz.trapmf(eficiencia, [5, 6, 7, 8])
    eficiencia_excelente = fuzz.trapmf(eficiencia, [7, 9, 10, 10])

    return (Quantidade_baixa, Quantidade_media, Quantidade_alta,
            pesoas_baixa, pesoas_media, pesoas_alta,
            Quantidade_horas_insuficiente, Quantidade_horas_baixa, Quantidade_horas_media, 
            Quantidade_horas_alta, Quantidade_horas_excessiva,
            Qualidade_pessima, Qualidade_baixa, Qualidade_mediana, 
            Qualidade_boa, Qualidade_otima,
            eficiencia_pessima, eficiencia_baixa, eficiencia_media,
            eficiencia_alta, eficiencia_excelente)
