import logging
import pandas as pd

def analisar_vagas_por_pais(df):
    df["job_openings"] = pd.to_numeric(df["job_openings"], errors="coerce")
    resultado = (
        df.groupby("country")["job_openings"]
        .sum()
        .reset_index(name="total_vagas")
        .sort_values("total_vagas", ascending=False)
        .head(10)
    )
    return resultado

def analisar_vagas_por_industria(df):
    resultado = (
        df.groupby("industry")
        .size()
        .reset_index(name="total_vagas")
        .sort_values("total_vagas", ascending=False)
        .head(8)
        )
    return resultado    

def analisar_porte_empresa(df):
    resultado = (
        df.groupby("company_size")
        .size()
        .reset_index(name="total_vagas")
        .drop_duplicates(subset="company_size")
        .sort_values("total_vagas", ascending=False)
    )
    return resultado

def analisar_risco_automacao(df):
    df = df.copy()
    df["automation_risk"] = pd.to_numeric(df["automation_risk"], errors="coerce")
    df["risco_faixa"] = pd.cut(
        df["automation_risk"],
        bins=[0, 33, 66, 100],
        labels=["Baixo (0-33)", "Médio (34-66)", "Alto (67-100)"]
    )
    resultado = (
        df.groupby("risco_faixa", observed=True)
        .size()
        .reset_index(name="total_vagas")
        .sort_values("total_vagas", ascending=False)
    )
    return resultado

def analisar_custo_contratacao(df):
    """
    CALCULA SALÁRIO MÉDIO, BONUS MÉDIO E DIFICULDADE DE CONTRATAÇÃO
    PARAMMETRO: DF - DataFrame LIMPO VINDO DO leitor.py
    RETORNA: DataFrame COM A CONTAGEM DE VAGAS POR COMBINACAO
    """
    df["salary_usd"] = pd.to_numeric(df["salary_usd"], errors="coerce")
    df["bonus_usd"] = pd.to_numeric(df["bonus_usd"], errors="coerce")
    df["offer_acceptance_rate"] = pd.to_numeric(df["offer_acceptance_rate"], errors="coerce")

    resultado = (
        df.groupby("experience_level")[
            ["salary_usd", "bonus_usd", "offer_acceptance_rate"]
        ]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={
            "experience_level": "nivel_experiencia",
            "salary_usd": "salario_medio_usd",
            "bonus_usd": "media_bonus_usd",
            "offer_acceptance_rate": "taxa_aceitacao_oferta"
        })
        .sort_values("salario_medio_usd", ascending=False)
        .reset_index(drop=True)
        #O drop=True significa "descarta o índice antigo e cria um novo do zero" — sem ele o índice antigo viraria uma coluna extra no DataFrame.
    )
    logging.info("Análise de custo de contratação concluída.")
    return resultado


def analisar_qualidade_vida(df):
    """
    CALCULA HORAS MÉDIAS, FÉRIAS MÉDIAS E SATISFAÇÃO MÉDIA POR MODELO DE TRABALHO.
    """
    df["weekly_hours"] = pd.to_numeric(df["weekly_hours"], errors="coerce")
    df["weekly_hours"] = pd.to_numeric(df["vacation_days"], errors="coerce")
    df["weekly_hours"] = pd.to_numeric(df["employee_satisfaction"], errors="coerce")

    resultado = (
        df.groupby("work_mode")[
            ["weekly_hours", "vacation_days", "employee_satisfaction"]
        ]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={
            "work_mode": "modelo_trabalho",
            "weekly_hours": "horas_semanais_media",
            "vacation_days": "ferias_medias_dias",
            "employee_satisfaction": "satisfacao_media"
        })
        .sort_values("satisfacao_media", ascending=False)
        .reset_index(drop=True)
    )
    logging.info("Análise de qualidade de vida concluída.")
    return resultado

def analisar_especializacoes(df):
    """
    CALCULA SALÁRIO MÉDIO, SCORE DE CRESCIMENTO E AVALIAÇÃO DA EMPRESA POR ESPECIALIZAÇÃO DE IA.
    """
    df["salary_usd"] = pd.to_numeric(df["salary_usd"], errors="coerce")
    df["career_growth_score"] = pd.to_numeric(df["career_growth_score"], errors="coerce")
    df['company_rating'] = pd.to_numeric(df['company_rating'], errors='coerce')

    resultado = (
        df.groupby("ai_specialization")[
            ["salary_usd", "career_growth_score", "company_rating"]
        ]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={
            "ai_specialization": "especializacao",
            "salary_usd": "salario_medio_usd",
            "career_growth_score": "crescimento_carreira",
            "company_rating": "avaliacao_empresa"
        })
        .sort_values("salario_medio_usd", ascending=False)
        .reset_index(drop=True)
    )
    logging.info("Análise de especializações concluída.")
    return resultado