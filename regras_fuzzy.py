import numpy as np
import skfuzzy as fuzz


def carregar_regras(
        per_quantidade_baixa, per_quantidade_media, per_quantidade_alta,
        per_pessoas_baixa, per_pessoas_media, per_pessoas_alta,
        per_horas_insuficiente, per_horas_baixa, per_horas_media, per_horas_alta, per_horas_excessiva,
        per_qualidade_pessima, per_qualidade_baixa, per_qualidade_mediana, per_qualidade_boa, per_qualidade_otima,
        eficiencia_pessima, eficiencia_baixa, eficiencia_media, eficiencia_alta, eficiencia_excellente
):
    # Lista para armazenar todas as regras
    regras = []

    # ----- REGRAS PRINCIPAIS -----

    # Combinações de Quantidade Baixa
    regras.append(np.fmin(per_quantidade_baixa, eficiencia_baixa))  # Regra base para quantidade baixa

    regras.append(np.fmin(np.fmin(per_quantidade_baixa, per_pessoas_baixa), eficiencia_baixa))
    regras.append(np.fmin(np.fmin(per_quantidade_baixa, per_pessoas_media), eficiencia_baixa))
    regras.append(np.fmin(np.fmin(per_quantidade_baixa, per_pessoas_alta), eficiencia_media))

    regras.append(np.fmin(np.fmin(per_quantidade_baixa, per_horas_insuficiente), eficiencia_pessima))
    regras.append(np.fmin(np.fmin(per_quantidade_baixa, per_horas_baixa), eficiencia_baixa))
    regras.append(np.fmin(np.fmin(per_quantidade_baixa, per_horas_media), eficiencia_media))
    regras.append(np.fmin(np.fmin(per_quantidade_baixa, per_horas_alta), eficiencia_media))
    regras.append(np.fmin(np.fmin(per_quantidade_baixa, per_horas_excessiva), eficiencia_baixa))

    regras.append(np.fmin(np.fmin(per_quantidade_baixa, per_qualidade_pessima), eficiencia_pessima))
    regras.append(np.fmin(np.fmin(per_quantidade_baixa, per_qualidade_baixa), eficiencia_baixa))
    regras.append(np.fmin(np.fmin(per_quantidade_baixa, per_qualidade_mediana), eficiencia_baixa))
    regras.append(np.fmin(np.fmin(per_quantidade_baixa, per_qualidade_boa), eficiencia_media))
    regras.append(np.fmin(np.fmin(per_quantidade_baixa, per_qualidade_otima), eficiencia_media))

    # Combinações de Quantidade Média
    regras.append(np.fmin(per_quantidade_media, eficiencia_media))  # Regra base para quantidade média

    regras.append(np.fmin(np.fmin(per_quantidade_media, per_pessoas_baixa), eficiencia_media))
    regras.append(np.fmin(np.fmin(per_quantidade_media, per_pessoas_media), eficiencia_media))
    regras.append(np.fmin(np.fmin(per_quantidade_media, per_pessoas_alta), eficiencia_alta))

    regras.append(np.fmin(np.fmin(per_quantidade_media, per_horas_insuficiente), eficiencia_baixa))
    regras.append(np.fmin(np.fmin(per_quantidade_media, per_horas_baixa), eficiencia_media))
    regras.append(np.fmin(np.fmin(per_quantidade_media, per_horas_media), eficiencia_media))
    regras.append(np.fmin(np.fmin(per_quantidade_media, per_horas_alta), eficiencia_alta))
    regras.append(np.fmin(np.fmin(per_quantidade_media, per_horas_excessiva), eficiencia_media))

    regras.append(np.fmin(np.fmin(per_quantidade_media, per_qualidade_pessima), eficiencia_baixa))
    regras.append(np.fmin(np.fmin(per_quantidade_media, per_qualidade_baixa), eficiencia_baixa))
    regras.append(np.fmin(np.fmin(per_quantidade_media, per_qualidade_mediana), eficiencia_media))
    regras.append(np.fmin(np.fmin(per_quantidade_media, per_qualidade_boa), eficiencia_alta))
    regras.append(np.fmin(np.fmin(per_quantidade_media, per_qualidade_otima), eficiencia_alta))

    # Combinações de Quantidade Alta
    regras.append(np.fmin(per_quantidade_alta, eficiencia_alta))  # Regra base para quantidade alta

    regras.append(np.fmin(np.fmin(per_quantidade_alta, per_pessoas_baixa), eficiencia_media))
    regras.append(np.fmin(np.fmin(per_quantidade_alta, per_pessoas_media), eficiencia_alta))
    regras.append(np.fmin(np.fmin(per_quantidade_alta, per_pessoas_alta), eficiencia_excellente))

    regras.append(np.fmin(np.fmin(per_quantidade_alta, per_horas_insuficiente), eficiencia_baixa))
    regras.append(np.fmin(np.fmin(per_quantidade_alta, per_horas_baixa), eficiencia_media))
    regras.append(np.fmin(np.fmin(per_quantidade_alta, per_horas_media), eficiencia_alta))
    regras.append(np.fmin(np.fmin(per_quantidade_alta, per_horas_alta), eficiencia_alta))
    regras.append(np.fmin(np.fmin(per_quantidade_alta, per_horas_excessiva), eficiencia_media))

    regras.append(np.fmin(np.fmin(per_quantidade_alta, per_qualidade_pessima), eficiencia_baixa))
    regras.append(np.fmin(np.fmin(per_quantidade_alta, per_qualidade_baixa), eficiencia_media))
    regras.append(np.fmin(np.fmin(per_quantidade_alta, per_qualidade_mediana), eficiencia_alta))
    regras.append(np.fmin(np.fmin(per_quantidade_alta, per_qualidade_boa), eficiencia_alta))
    regras.append(np.fmin(np.fmin(per_quantidade_alta, per_qualidade_otima), eficiencia_excellente))

    # ----- REGRAS ESPECÍFICAS COM TRÊS VARIÁVEIS -----

    # Algumas das regras originais e outras novas
    regras.append(
        np.fmin(np.fmin(np.fmin(per_quantidade_baixa, per_pessoas_baixa), per_horas_insuficiente), eficiencia_pessima))
    regras.append(np.fmin(np.fmin(np.fmin(per_quantidade_media, per_pessoas_media), per_horas_media), eficiencia_media))
    regras.append(
        np.fmin(np.fmin(np.fmin(per_quantidade_alta, per_pessoas_alta), per_horas_alta), eficiencia_excellente))

    regras.append(
        np.fmin(np.fmin(np.fmin(per_quantidade_baixa, per_pessoas_baixa), per_qualidade_pessima), eficiencia_pessima))
    regras.append(
        np.fmin(np.fmin(np.fmin(per_quantidade_media, per_pessoas_media), per_qualidade_mediana), eficiencia_media))
    regras.append(
        np.fmin(np.fmin(np.fmin(per_quantidade_alta, per_pessoas_alta), per_qualidade_otima), eficiencia_excellente))

    # ----- REGRAS ESPECÍFICAS COM QUATRO VARIÁVEIS (como no código original) -----

    # Regra 1 - Pior cenário
    regras.append(np.fmin(np.fmin(np.fmin(np.fmin(per_quantidade_baixa, per_pessoas_baixa), per_horas_insuficiente),
                                  per_qualidade_pessima), eficiencia_pessima))

    # Regra 4 - Melhor cenário
    regras.append(
        np.fmin(np.fmin(np.fmin(np.fmin(per_quantidade_alta, per_pessoas_alta), per_horas_alta), per_qualidade_otima),
                eficiencia_excellente))

    # Outras regras importantes do código original
    regras.append(np.fmin(
        np.fmin(np.fmin(np.fmin(per_quantidade_media, per_pessoas_media), per_horas_media), per_qualidade_mediana),
        eficiencia_media))
    regras.append(np.fmin(
        np.fmin(np.fmin(np.fmin(per_quantidade_alta, per_pessoas_media), per_horas_alta), per_qualidade_mediana),
        eficiencia_alta))
    regras.append(
        np.fmin(np.fmin(np.fmin(np.fmin(per_quantidade_media, per_pessoas_alta), per_horas_alta), per_qualidade_boa),
                eficiencia_alta))

    # ----- REGRA DE FALLBACK (garantia contra erro de membership vazio) -----
    # Esta regra garante que sempre haverá pelo menos um valor mínimo de ativação
    fallback_level = 0.1  # Nível mínimo de ativação
    regras.append(np.ones_like(eficiencia_media) * fallback_level)

    # Agregação de todas as regras (máximo)
    agregacao_total = np.fmax.reduce(regras)

    return agregacao_total


def calcular_eficiencia(agregacao_total, universo_eficiencia):
    try:
        # Verifica se a agregação está vazia antes de tentar defuzzificar
        if np.all(agregacao_total == 0):
            print("Aviso: Agregação vazia - nenhuma regra foi ativada!")
            return 50  # Valor padrão como fallback

        # Tenta defuzzificar usando o método do centroide
        eficiencia_centroide = fuzz.defuzz(universo_eficiencia, agregacao_total, 'centroid')

        # Verifica se o resultado é NaN (pode acontecer mesmo com agregação não-vazia)
        if np.isnan(eficiencia_centroide):
            print("Aviso: Resultado da defuzzificação é NaN, usando método alternativo")
            # Tenta método alternativo
            eficiencia_centroide = fuzz.defuzz(universo_eficiencia, agregacao_total, 'bisector')

            # Se ainda for NaN, usa valor padrão
            if np.isnan(eficiencia_centroide):
                print("Aviso: Todos os métodos de defuzzificação falharam, usando valor padrão")
                return 50

        return eficiencia_centroide

    except Exception as e:
        print(f"Erro durante defuzzificação: {e}")
        return 50  # Valor padrão em caso de erro