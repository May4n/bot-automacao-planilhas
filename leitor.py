import pandas as pd
import logging
import os

def ler_arquivo(name_file):
    """LÊ UM ARQUIVO ARQUIVO .xlsx ou .csv da pasta arquivos/ e retorna um DataFrame"""

    caminho = f"arquivos/{name_file}"

    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo deu RED, PATRÃO: {caminho}")
    
    # DESCOBRE A EXTENSÃO E LÊ O FORMATO CERTO

    if name_file.endswith(".xlsx"):
        df = pd.read_excel(caminho, header=1)
        logging.info(f"Arquivo Excel lido:{name_file}")
    elif name_file.endswith(".csv"):
        df = pd.read_csv(caminho, sep=";", encoding="utf-8")
        logging.info(f"Arquivo CSV lido: {name_file}")
    else:
        raise ValueError(f"Formato não suportado: {name_file}")
    

    return df

def limpar_dados(df):
    """LIMPA E TRATA OS DADOS DO DataFrame"""
    total_antes = len(df)

    df = df.dropna(how="all")
    df = df.drop_duplicates()
    df = df[df.iloc[:, 0] != df.columns[0]]
    df = df.reset_index(drop=True)
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df = df[df['year'].isin([2025,2026])]
    df = df.reset_index(drop=True) #isin() FILTRA APENAS AS LINHAS DO ANO SELECIONADO DENTRO DESSA LISTA

    df.columns = (
        df.columns
        .str.strip() # REMOVE OS ESPAÇOS NAS BORDAS
        .str.lower() #TUDO MINUSCULO
        .str.replace(" ", "_") #ESPAÇOS VIRAM UNDERLINE
    )

    total_depois = len(df)

    removidas = total_antes - total_depois
    logging.info(f"Limpeza concluída. Linhas removidas: {removidas}")
    
    return df