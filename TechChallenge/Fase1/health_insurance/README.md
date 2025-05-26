# Análise e Modelagem de Custos de Seguro Saúde

Este projeto realiza uma análise exploratória e modelagem preditiva sobre um conjunto de dados de seguros de saúde, conforme documentado no notebook `health_insurance.ipynb`. O objetivo é investigar os fatores que influenciam o valor cobrado pelo seguro, utilizando técnicas de visualização, análise estatística e modelos de regressão (linear, polinomial e árvore de decisão). O notebook inclui desde a exploração dos dados, tratamento de variáveis categóricas, análise de correlação, até a avaliação de desempenho dos modelos preditivos.

## Como rodar o projeto

1. **Instale o Conda**  
   Siga as instruções da [documentação oficial](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

2. **Clone o repositório ou faça o download do ZIP**  
   Para clonar via git, execute:
   ```sh
   git clone https://github.com/thiagofernandes101/ProjetosFiap.git
   ```
   Ou faça o download do ZIP diretamente pelo GitHub.

3. **Obtenha o dataset do Kaggle**  
   Baixe o arquivo do dataset em [Kaggle Health Insurance](https://www.kaggle.com/datasets/mirichoi0218/insurance)  
   
   Extraia o arquivo `insurance.csv` e coloque-o na pasta `archive`, que deve estar na mesma hierarquia do arquivo `health_insurance.ipynb`.

4. **Crie o ambiente Conda com as dependências**  
   Execute no terminal:
   ```sh
   conda env create -f environment.yml
   ```

5. **Ative o ambiente**
   ```sh
   conda activate env-health-insurance
   ```

6. **Abra o notebook**
   Abra o arquivo `health_insurance.ipynb` no VS Code ou Jupyter Notebook para executar as células e acompanhar toda a análise.

## Principais dependências

- Python >= 3.10
- pandas
- seaborn
- matplotlib
- scikit-learn
- openpyxl

Todas as dependências estão listadas em [environment.yml](environment.yml).