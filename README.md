Bot de Automação de Planilhas — Análise de Mercado de IA
Bot desenvolvido em Python que lê automaticamente uma planilha de vagas de emprego em IA, processa os dados, gera um relatório Excel formatado e um dashboard visual com gráficos de mercado — tudo organizado por data de execução.

    O que o bot faz

Lê arquivos .xlsx ou .csv automaticamente
Filtra dados por ano (2025 e 2026)
Limpa e trata dados inconsistentes
Analisa padrões de contratação por nível de experiência e modelo de trabalho
Gera análises de mercado: vagas por país, indústria, porte de empresa e risco de automação
Exporta um relatório .xlsx formatado com cabeçalho colorido e linhas alternadas
Gera um dashboard .png com 4 gráficos de pizza
Organiza os arquivos de saída em pastas por data de execução
Agenda execução automática diária no horário configurado
Registra logs de todas as execuções

🚀 Como usar
1. Clone o repositório
bashgit clone https://github.com/May4n/bot-python-planilhas.git
cd bot-python-planilhas
2. Crie e ative o ambiente virtual
bashpython -m venv .venv
source .venv/Scripts/activate   # Windows (Git Bash)
source .venv/bin/activate        # Linux / macOS
3. Instale as dependências
bashpip install -r requirements.txt
4. Adicione o arquivo de dados
Coloque seu arquivo .xlsx ou .csv dentro da pasta arquivos/. O projeto usa o dataset Global AI Jobs disponível gratuitamente no Kaggle.
5. Configure o nome do arquivo
Abra o main.py e ajuste o nome do arquivo na linha:
pythondf = ler_arquivo("seu_arquivo.xlsx")
6. Execute o bot
bashpython main.py
O bot vai rodar imediatamente e depois aguardar o próximo horário agendado. Para encerrar, pressione CTRL+C no terminal.

    Configurações
Para alterar o horário de execução automática, edite essa linha no main.py:
pythonschedule.every().day.at("08:00").do(executar_bot)
Exemplos de agendamento:
pythonschedule.every(10).minutes.do(executar_bot)   # a cada 10 minutos
schedule.every().hour.do(executar_bot)         # a cada hora
schedule.every().monday.at("09:00").do(executar_bot)  # toda segunda às 9h

    Dependências
pandas
openpyxl
matplotlib
schedule

    Exemplo de saída
O bot gera automaticamente dois arquivos na pasta saida/YYYY-MM-DD/:
Relatório Excel — tabela formatada com análise de contratação por nível de experiência e modelo de trabalho, com cabeçalho azul escuro e linhas alternadas.
Dashboard — imagem .png com 4 gráficos de pizza mostrando:

Top 10 países com mais vagas de IA
Distribuição por setor da indústria
Vagas por porte de empresa
Distribuição por risco de automação


    Tecnologias utilizadas

Python 3.x
pandas — leitura, limpeza e análise de dados
openpyxl — geração de relatórios Excel formatados
matplotlib — geração de gráficos e dashboard
schedule — agendamento de execução automática
logging — registro de logs de execução


    Sobre o projeto
Este projeto foi desenvolvido como portfólio para demonstrar habilidades em automação de dados com Python. O bot foi construído com arquitetura modular — cada arquivo tem uma responsabilidade única, seguindo boas práticas de desenvolvimento.
