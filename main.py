import logging
import schedule
import time
from datetime import datetime
from leitor import ler_arquivo, limpar_dados
from processador import (
            analisar_vagas_por_pais,
            analisar_vagas_por_industria,
            analisar_porte_empresa,
            analisar_risco_automacao,
            analisar_qualidade_vida,
            analisar_especializacoes,
            analisar_custo_contratacao
        )
from dashboard import gerar_dashboard
from relatorio import gerar_relatorio # NO TOPO DO ARQUIVO
from datetime import datetime
import os
import argparse
import pandas as pd

pd.set_option('display.width', None)        # largura infinita
pd.set_option('display.max_columns', None)  # mostra todas as colunas
pd.set_option('display.float_format', '{:.2f}'.format)  # 2 casas decimais


def executar_bot(name_file, abas=["todas"]):
    logging.info("Bot INICIADO.")
    hora_atual = datetime.now().strftime('%H:%M:%S')
    print(f"[{hora_atual}] Executando bot")
    
    try:
        #Passo 1 e 2: leitura e limpeza
        df = ler_arquivo(name_file)
        df = limpar_dados(df)
        
        #LINHAS DE DIAGNÓSTICO
        #print(df['offer_acceptance_rate'].describe())
        #print(df['offer_acceptance_rate'].head(10))
        #print(df["ai_specialization"].nunique()) # CONTA VALORES ÚNICOS
        #print(df["ai_specialization"].value_counts()) # LISTA CADA VALOR E QUANTAS VEZES APARECE
        
        print(df.columns.tolist()) #TODAS AS 35 COLUNAS SÃO LISTADAS NO TERMINAL
        print(f"Arquivo lido com SUCESSO! {len(df)} linhas encontradas.")
        logging.info("Bot finalizado com sucesso.")
        
        resultado = analisar_qualidade_vida(df), analisar_especializacoes(df), analisar_custo_contratacao(df)
        print("\n--- ANALISE PLANIHA ---")
        print(resultado)

        #Passo 3: Processamento
        industria = analisar_vagas_por_industria(df)
        custo = analisar_custo_contratacao(df)
        qualidade = analisar_qualidade_vida(df)
        especializacoes = analisar_especializacoes(df)
        porte = analisar_porte_empresa(df)
        pais = analisar_vagas_por_pais(df)
        automacao = analisar_risco_automacao(df)
        
        #CRIA PASTA COM DATA DE HOJE
        data_hoje = datetime.now().strftime("%Y-%m-%d")
        pasta_saida = f"saida/{data_hoje}"

        if not args.dry_run:
            #GARANTE QUE A PASTA SAÍDA/ EXISTE
            os.makedirs(pasta_saida, exist_ok=True)

            #SALVA OS ARQUIVOS NA PASTA DA DATA
            gerar_relatorio(custo, qualidade, especializacoes, f"{pasta_saida}/analise_contratacao.xlsx")
            gerar_dashboard(pais, industria, porte, automacao, f"{pasta_saida}/dashboard_mercado_de_trabalho.png")
            print(f"Arquivos salvos em: {pasta_saida}/")
        else:
            pd.set_option('display.max_rows', None)  # ← mostra todas as linhas
            print("\n--- MODO DRY RUN — nenhum arquivo será salvo ---")
            pd.set_option('display.max_rows', None)
            print("\nCUSTO DE CONTRATAÇÃO:")
            pd.set_option('display.max_rows', None)
            print(custo)
            pd.set_option('display.max_rows', None)
            print("\nQUALIDADE DE VIDA:")
            pd.set_option('display.max_rows', None)
            print(qualidade)
            pd.set_option('display.max_rows', None)
            print("\nESPECIALIZAÇÕES:")
            pd.set_option('display.max_rows', None)
            print(especializacoes)
        
            hora_fim = datetime.now().strftime('%H:%M:%S')
            print(f"\n[{hora_fim}] EXECUÇÃO CONCLUIDA. Aguardando próximo ciclo...")
            logging.info("Bot finalizado com sucesso;")
        
    except Exception as e:
        logging.error(f"Erro na execucao: {e}")
        print(f"ERROR: {e}")

#---------CONFIGURAÇAO DO ARGPARSE
parser = argparse.ArgumentParser(
    description="Bot de Automação de Planilhas" 
)

parser.add_argument(
    "--arquivo",
    type=str,
    required=True,
    help="Nome do arquivo de entrada (ex: global_ai_jobs.xlsx)"
)

parser.add_argument(
    "--dry-run",
    action="store_true",  # não precisa de valor, só a flag basta
    default=False,
    help="Roda o bot sem salvar arquivos — só exibe resultados no terminal"
)

parser.add_argument(
    "--abas",
    nargs="+",  # aceita um ou mais valores
    choices=["custo", "qualidade", "especializacoes", "todas"],
    default=["todas"],
    help="Quais abas gerar: custo, qualidade, especializacoes, ou todas"
)

args = parser.parse_args()
try:
    executar_bot(args.arquivo,args.abas) #RODA UMA VEZ IMEDIATAMENTE
except KeyboardInterrupt:
    print("\nBot encerrado pelo usuário.")