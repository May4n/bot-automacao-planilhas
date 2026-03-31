import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import logging
import os

def gerar_relatorio(resultado, nome_saida):
    """
    GERA UM ARQUIVO EXCEL FORMATADO COM OS RESULTADOS DA ANALISE

    PARAMETROS:
    RESULTADO - DataFrame VINDO DO processador.py
    nome_saida - nome do arquivo a ser criado em saida/
    """
    caminho = nome_saida

    #CRIA UM ARQUIVO EXCEL NOVO NA MEMÓRIA
    wb = openpyxl.Workbook()
    ws = wb.active # PEGA A ABA ATIVA(Sheet1)
    ws.title = "Análise de Contratação" #RENOMEIA A ABA

    # --- ESTILO DO CABEÇALHO ------
    #PatternFill DEFINE A COR DE FUNDO DA CÉLULA
    #fgColor É O CÓDIGO HEXADECIMAL DA COR(SEM O #)
    fill_cabecalho = PatternFill(
        start_color="191970",
        end_color="1F4E79",
        fill_type="solid"
    )
    fonte_cabecalho = Font(
        bold=True,
        color="FFFFFF",
        size=12
    )

    #---- ESTILO DAS LINHAS ALTERNADAS------
    fill_impar = PatternFill(
        start_color="FFFFFF",
        end_color="FFFFFF",
        fill_type="solid"
    )

    fill_par = PatternFill(
        start_color="D6E4F0",
        end_color="D6E4F0",
        fill_type="solid"  
    )

    #--- ESTILO DE BORDA FINA -----
    borda = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin"),
    )

    #----- ESCREVE O CABEÇALHO-----
    #df.columns RETORNA OS NOMES DAS COLUNAS DO RESULTADO
    colunas = list(resultado.columns)
    for col_idx, nome_coluna in enumerate(colunas, start=1):
        celula = ws.cell(row=1, column=col_idx, value=nome_coluna)
        celula.fill = fill_cabecalho
        celula.font = fonte_cabecalho
        celula.alignment = Alignment(horizontal="center")
        celula.border = borda

        #---- ESCREVE OS DADOS LINHA POR LINHA ----------
        # iterrows() PERCORRE O DataFrame LINHA POR LINHA
        #row_idx COMECA EM 2 PARA NAO SOBRESCREVER O CABEÇALHO
        for row_idx, (_, linha) in enumerate(resultado.iterrows(), start=2):
            for col_idx, valor in enumerate(linha, start=1):
                celula = ws.cell(row=row_idx, column=col_idx, value=valor)
                celula.border = borda
                celula.alignment = Alignment(horizontal="center")

                #LINHAS PARES FICAM AZUL CLARO, IMPARES FICAM BRANCAS
                if row_idx % 2 == 0:
                    celula.fill = fill_par
                else:
                    celula.fill = fill_impar

        #-----AJUSTA LARGURA DAS COLUNAS AUTOMATICAMENTE------
        #get_column_letter CONVERTE NUMERO PARA LETRA: 1->A, 2->B, 3->C
        for col_idx, nome_coluna in enumerate(colunas, start=1):
            letra = get_column_letter(col_idx)
            largura = max(len(str(nome_coluna)), 15) + 4
            ws.column_dimensions[letra].width = largura

        #----- SALVA O ARQUIVO ------------------------
    wb.save(caminho)
    logging.info(f"Relatório salvo em: {caminho}")
    print(f"Relatório salvo em: {caminho}")

    return
