import matplotlib.pyplot as plt
import matplotlib
import logging
import os

matplotlib.use("Agg") #MODO SEM INTERFACE GRÁFICA - SALVA COMO ARQUIVO

def gerar_dashboard(pais, industria, porte, automacao, nome_saida):
    """
    GERA UM DASHBOARD COM 4 GRÁFICOS DE PIZZA E SALVA COMO IMAGEM .png

    Parâmetros:
    pais — DataFrame de vagas por país
        industria — DataFrame de vagas por indústria
        porte — DataFrame de vagas por porte de empresa
        automacao — DataFrame de vagas por risco de automação
        nome_saida — nome do arquivo .png a ser salvo em saida/
    """
    print("INICIANDO geração do Dashboard...")
    caminho = nome_saida
    #CRIA UMA FIGURA COM 4 GRÁFICOS - 2 LINHAS X 2 COLUNAS
    fig, eixos = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle(
        "Análise de Mercado - Vagas de IA (2025/2026)",
        fontsize=18,
        fontweight="bold",
        y=1.02
    )

    # --- GRÁFICO 1: Vagas por país -----
    
    eixos[0, 0].pie(
        pais["total_vagas"],
        labels=pais["country"],
        autopct=lambda pct: f"{pct:.1f}%",
        startangle=90
    )
    eixos[0, 0].set_title("Top 10 países com mais vagas", fontsize=13)
    
        # ---- GRÁFICO 2: VAGAS POR INDÚSTRIA -----
    
    eixos[0, 1].pie(
        industria["total_vagas"],
        labels=industria["industry"],
        autopct=lambda pct: f"{pct:.1f}%",
        startangle=90
    )
    eixos[0, 1].set_title("Vagas por setor da indústria", fontsize=13)
    

        # --- GRÁFICO 3: VAGAS POR PORTE DE EMPRESA -----
    
    eixos[1, 0].pie(
        porte["total_vagas"],
        labels=porte["company_size"],
        autopct=lambda pct: f"{pct:.1f}%",
        startangle=90
    )
    eixos[1, 0].set_title(" Vagas por porte de empresa", fontsize=13)
    

        # ---- GRÁFICO 4: RISCO DE AUTOMAÇÃO -------
    
    eixos[1, 1].pie(
        automacao["total_vagas"],
        labels=automacao["risco_faixa"].astype(str),
        autopct=lambda pct: f"{pct:.1f}%",
        startangle=90
    )
    eixos[1, 1].set_title("Distribuição por risco de automação", fontsize=13)
    

        #SALVA E FECHA A FIGURA
    plt.tight_layout()
    plt.savefig(caminho, dpi=150, bbox_inches="tight")
    print(f"Caminho absoluto: {os.path.abspath(caminho)}") #MOSTRA O CAMINHO COMPLETO
    plt.close()

    logging.info(f"Dashboard salvo em: {caminho}")
    print(f"Dashboard salvo em: {caminho}")