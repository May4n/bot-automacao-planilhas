import logging
import schedule
import time
from datetime import datetime
from leitor import ler_arquivo, limpar_dados
from processador import analisar_contratacao
from processador import (
            analisar_contratacao,
            analisar_vagas_por_pais,
            analisar_vagas_por_industria,
            analisar_porte_empresa,
            analisar_risco_automacao
        )
from dashboard import gerar_dashboard
from relatorio import gerar_relatorio # NO TOPO DO ARQUIVO
from datetime import datetime
import os
import argparse

def executar_bot(name_file):
    logging.info("Bot INICIADO.")
    hora_atual = datetime.now().strftime('%H:%M:%S')
    print(f"[{hora_atual}] Executando bot")
    
    try:
        #Passo 1 e 2: leitura e limpeza
        df = ler_arquivo(name_file)
        df = limpar_dados(df)
        print(f"Arquivo lido com SUCESSO! {len(df)} linhas encontradas.")
        logging.info("Bot finalizado com sucesso.")

        resultado = analisar_contratacao(df)
        print("\n--- ANALISE DE CONTRATACAO ---")
        print(resultado)

        #Passo 3: Processamento
        contratacao = analisar_contratacao(df)
        pais = analisar_vagas_por_pais(df)
        industria = analisar_vagas_por_industria(df)
        porte = analisar_porte_empresa(df)
        print("PORTE COMPLETO:")
        print(porte)
        automacao = analisar_risco_automacao(df)
        
        #CRIA PASTA COM DATA DE HOJE
        data_hoje = datetime.now().strftime("%Y-%m-%d")
        pasta_saida = f"saida/{data_hoje}"

        #GARANTE QUE A PASTA SAÍDA/ EXISTE
        os.makedirs(pasta_saida, exist_ok=True)

        #SALVA OS ARQUIVOS NA PASTA DA DATA
        gerar_relatorio(resultado, f"{pasta_saida}/analise_contratacao.xlsx")
        gerar_dashboard(pais, industria, porte, automacao, f"{pasta_saida}/dashboard_mercado_de_trabalho.png")

        print(f"Arquivos salvos em: {pasta_saida}/")

        hora_fim = datetime.now().strftime(':%H:%M:%S')
        print(f"\n[{hora_fim}] EXECUCAO CONCLUIDA. Aguardando próximo ciclo...")
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
    help="NOme do arquivo de entrada (ex: global_ai_jobs.xlsx)"
)

parser.add_argument(
    "--horario",
    type=str,
    default="08:00",
    help="HOra´rio de execução diária no formato HH:HM (padrão: 08:00)"
)

args = parser.parse_args()

#--------AGENDAODR
schedule.every().day.at(args.horario).do(
    lambda: executar_bot(args.arquivo)
    )
print(f"Bot agendado para rodar todos os dias às {args.horario}")
print("Pressione CRTL+C para parar.\n")

executar_bot(args.arquivo) #RODA UMA VEZ IMEDIATAMENTE

while True:
    schedule.run_pending()
    time.sleep(1.5)