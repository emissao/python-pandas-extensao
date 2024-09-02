
# Projeto de Extensão: Análise de Dados Experimentais em Química com Python

## Descrição do Projeto

Este projeto foi desenvolvido como parte de uma atividade de extensão no ano de 2017, em parceria com o pré-vestibular social "+nós" localizado em Nilópolis, RJ. O objetivo do projeto foi aplicar técnicas de Big Data e análise de dados utilizando a linguagem Python para tratar, analisar e visualizar dados experimentais de química. O foco foi melhorar o entendimento dos alunos sobre a relação entre variáveis experimentais, como concentração de reagentes e tempo de reação, e como essas variáveis podem ser usadas para calcular taxas de reação.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- **`main.py`**: Contém o código principal para processamento de dados, visualização, e análise.
- **`dados_experimentais.csv`**: Arquivo de exemplo contendo os dados brutos usados para análise.
- **`dados_processados.csv`**: Arquivo gerado pelo código que contém os dados processados, sem outliers e normalizados.
- **`relatorio_final.txt`**: Relatório gerado automaticamente com a matriz de correlação e os resultados da análise.
- **`README.md`**: Este arquivo, contendo as instruções e informações sobre o projeto.

## Funcionalidades

- **Carregamento e Visualização de Dados**: O projeto carrega os dados experimentais de um arquivo CSV e exibe uma visão geral dos dados.
- **Processamento de Dados**: Inclui a remoção de outliers e normalização dos dados para garantir análises precisas.
- **Análise de Correlação**: Calcula e exibe a matriz de correlação entre as variáveis experimentais.
- **Visualização Gráfica**: Gera gráficos de dispersão e de linha para facilitar a interpretação dos dados experimentais.
- **Cálculo da Taxa de Reação**: Implementa uma função para calcular a taxa de reação com base na concentração e no tempo de reação.
- **Geração de Relatório**: Cria automaticamente um relatório em formato de texto com os principais resultados da análise.

## Requisitos

- **Python 3.x**: Este projeto foi desenvolvido em Python 3 e requer a versão 3.6 ou superior.
- **Bibliotecas Python**:
  - `pandas`: Para manipulação e análise de dados.
  - `numpy`: Para operações numéricas.
  - `matplotlib`: Para geração de gráficos.
  - `seaborn`: Para visualizações estatísticas mais elaboradas.

## Como Executar o Projeto

1. Clone este repositório em sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-projeto.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd nome-do-projeto
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o script principal:
   ```bash
   python main.py
   ```

5. Os resultados serão exibidos no terminal e os arquivos processados serão salvos na pasta do projeto.

## Resultados Esperados

Após a execução do script, os seguintes resultados serão gerados:

- **Gráficos**: Gráficos de dispersão e linha para análise visual dos dados.
- **Arquivos CSV**: Dados experimentais processados, prontos para análise posterior.
- **Relatório**: Um arquivo de texto com a matriz de correlação e uma visão geral dos dados analisados.

## Contribuições

Este projeto foi desenvolvido em um contexto educacional, e todos os participantes do "+nós" foram envolvidos no processo, desde a coleta de dados até a análise final. Se você deseja contribuir para o projeto ou sugerir melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é de uso livre para fins educacionais e não possui restrições de licença. 

## Contato

Para mais informações, entre em contato com [Seu Nome] - [seu.email@exemplo.com] ou visite o site do pré-vestibular "+nós" em [https://www.maisnos.com.br](https://www.maisnos.com.br).


