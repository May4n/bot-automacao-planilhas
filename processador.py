import logging
import pandas as pd
def analisar_contratacao(df):
    """
    ANALISA PADRES DE CONTRACAO POR NIVEL DE EXPERIENCIA E MODELO DE TRABALHO
    PARAMMETRO: DF - DataFrame LIMPO VINDO DO leitor.py
    RETORNA: DataFrame COM A CONTAGEM DE VAGAS POR COMBINACAO
    """

    resultado = (
        df.groupby(["experience_level", "work_mode"])
        .size() #CONTA LINHAS POR GRUPO
        .reset_index(name="total_vagas") #TRANSFORMA EM COLUNA LEGÍVEL
        .sort_values("total_vagas", ascending=False) #MAIOR PRIMEIRO
    )
    return resultado

def analisar_vagas_por_pais(df):
    """
    Soma total do job_openings por país
    retorna os 10 paises com mais vagas.
    """
    df['job_openings'] = pd.to_numeric(df['job_openings'], errors='coerce')
    resultado = (
        df.groupby("country")["job_openings"]
        .sum()
        .reset_index(name="total_vagas")
        .sort_values("total_vagas", ascending=False)
        .head(10)
    )
    logging.info("Analise de vagas por país concluída.")
    return resultado

def analisar_vagas_por_industria(df):
    """
    CONTA VAGSA POR SETOR DA INDÚSTRIA
    RETORNA OS 8 SETORES COM MAIS VAGAS
    """
    resultado = (
        df.groupby("industry")
        .size()
        .reset_index(name="total_vagas")
        .sort_values("total_vagas", ascending=False)
        .head(8)
    )
    logging.info("análise por industria concluída.")
    return resultado

def analisar_porte_empresa(df):
    """
    DISTRIBUIÇÃO DE VAGAS POR PARTE DA EMPRESA
    """
    resultado = (
        df.groupby("company_size")
        .size()
        .reset_index(name="total_vagas")
        .drop_duplicates(subset="company_size")
        .sort_values("total_vagas", ascending=False)
    )
    logging.info("Análise por porte de empresa concluída.")
    return resultado

def analisar_risco_automacao(df):
    """
    DISTRIBUIÇÃO DE VAGAS POR NIVEL DE RISCO DE AUTOMAÇÃO.
    """
    df = df.copy()
    df["automation_risk"] = pd.to_numeric(df["automation_risk"], errors="coerce")

    #DIVIDE A PONTUAÇÃO EM 3 FAIXAS
    df["risco_faixa"] = pd.cut(
        df["automation_risk"],
        bins=[0, 33, 66, 100],
        labels=["Baixo (0-33)", "Médio(34-66)", "Alto(67-100)"]
    )
    resultado = (
        df.groupby("risco_faixa", observed=True)
        .size()
        .reset_index(name="total_vagas")
        .sort_values("total_vagas", ascending=False)
    )
    logging.info("Ánalise de risco de automação concluída.")
    return resultado