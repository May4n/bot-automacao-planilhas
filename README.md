Bot de Automação de Planilhas — Análise de Mercado de IA
Bot desenvolvido em Python que lê automaticamente uma planilha de vagas de emprego em IA, processa os dados, gera um relatório Excel com 3 abas de análise e um dashboard visual com 4 gráficos de mercado — tudo organizado por data de execução e configurável via terminal.

O que o bot faz

Lê arquivos .xlsx ou .csv automaticamente

Com base em dados reais de +25.000 vagas globais (2025/2026):

Custo de contratação por nível de experiência — salário médio, bônus e taxa de aceitação de oferta
Qualidade de vida por modelo de trabalho — horas semanais, férias e satisfação
Especializações de IA — quais perfis pagam mais e têm maior crescimento de carreira
Dashboard visual com 4 gráficos de mercado — países, indústrias, porte de empresa e risco de automação


Exporta um relatório .xlsx formatado com 3 abas, cabeçalho colorido e linhas alternadas
Gera um dashboard .png com 4 gráficos de pizza
Organiza os arquivos de saída em pastas por data de execução
Suporta modo --dry-run para visualizar os dados no terminal sem salvar arquivos
Registra logs de todas as execuções

🚀 Como usar
1. Clone o repositório
bashgit clone https://github.com/May4n/bot-automacao-planilhas.git
cd bot-automacao-planilhas

2. Crie e ative o ambiente virtual
bashpython -m venv .venv
source .venv/Scripts/activate   # Windows (Git Bash)
source .venv/bin/activate        # Linux / macOS

3. Instale as dependências
bashpip install -r requirements.txt

4. Adicione o arquivo de dados
Coloque seu arquivo .xlsx ou .csv dentro da pasta arquivos/.
O projeto foi desenvolvido com o dataset Global AI Jobs,
disponível gratuitamente no Kaggle.

5. Execute o bot

# Modo diagnóstico — visualiza os dados no terminal sem salvar arquivos
python main.py --arquivo nome_do_arquivo.xlsx --dry-run

6. Verifique os resultados
Os arquivos gerados são salvos automaticamente em:
saida/ YYYY-MM-DD/
                ├── analise_contratacao.xlsx           → relatório Excel com 3 abas
                └── dashboard_mercado_de_trabalho.png  → dashboard com 4 gráficos
Ajuda

Para ver todos os comandos disponíveis:Configurações
Para alterar o horário de execução automática:
bash# Todo dia às 09:30
python main.py --arquivo dados.xlsx --horario 09:30
python main.py --help

Análises geradas

Aba 1 — Custo de Contratação
Salário médio, bônus médio e taxa de aceitação de oferta agrupados por nível de experiência (Entry, Mid, Senior, Lead).

Aba 2 — Qualidade de Vida
Horas semanais médias, dias de férias médios e satisfação média agrupados por modelo de trabalho (Remote, Hybrid, Onsite).

Aba 3 — Especializações de IA
Salário médio, score de crescimento de carreira e avaliação média de empresa agrupados por especialização (LLM, NLP, Computer Vision, MLOps, Generative AI, Analytics, Reinforcement Learning, Forecasting).

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
argparse — interface de linha de comando (CLI)

Insights gerados com dados reais (2025/2026)
Com base em +25.770 vagas de IA globais:

Profissionais Lead têm salário médio de $142k — 37% acima de Entry ($61k).

Remote, Hybrid e Onsite apresentam satisfação praticamente igual — o modelo de trabalho não impacta significativamente a felicidade do funcionário.

Generative AI lidera o ranking de salários ($97k), seguida de perto por LLM ($97k) e Analytics ($97k).

A taxa de aceitação de oferta é similar em todos os níveis (75%) — mercado competitivo independente da senioridade.

    Sobre o projeto
Este projeto foi desenvolvido como portfólio para demonstrar habilidades em automação de dados com Python. O bot foi construído com arquitetura modular — cada arquivo tem uma responsabilidade única, seguindo boas práticas de desenvolvimento (PEP 8, DRY, early filter, docstrings).
