import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração inicial para exibição gráfica
sns.set(style="whitegrid")

# Passo 1: Carregar os dados experimentais
# Exemplo de dados: concentração de reagentes e tempo de reação
data = {
    'experimento': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'concentracao_molar': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    'tempo_reacao_segundos': [150, 120, 95, 80, 60, 45, 40, 35, 30, 25],
    'temperatura_celsius': [25, 25, 26, 26, 27, 27, 28, 28, 29, 29]
}

df = pd.DataFrame(data)

# Exibir os dados carregados
print("Dados experimentais carregados:")
print(df)

# Passo 2: Processar os dados
# Remover possíveis outliers ou valores extremos
df = df[(np.abs(df['tempo_reacao_segundos'] - df['tempo_reacao_segundos'].mean()) <= (2 * df['tempo_reacao_segundos'].std()))]

# Normalizar os dados (escala entre 0 e 1)
df_normalized = df.copy()
df_normalized['concentracao_molar'] = (df['concentracao_molar'] - df['concentracao_molar'].min()) / (df['concentracao_molar'].max() - df['concentracao_molar'].min())
df_normalized['tempo_reacao_segundos'] = (df['tempo_reacao_segundos'] - df['tempo_reacao_segundos'].min()) / (df['tempo_reacao_segundos'].max() - df['tempo_reacao_segundos'].min())
df_normalized['temperatura_celsius'] = (df['temperatura_celsius'] - df['temperatura_celsius'].min()) / (df['temperatura_celsius'].max() - df['temperatura_celsius'].min())

print("\nDados normalizados:")
print(df_normalized)

# Passo 3: Analisar a correlação entre as variáveis
correlation_matrix = df.corr()
print("\nMatriz de correlação:")
print(correlation_matrix)

# Visualizar a matriz de correlação usando um heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlação entre Variáveis')
plt.show()

# Passo 4: Criar visualizações para os dados
# Gráfico de dispersão da concentração versus tempo de reação
plt.figure(figsize=(10, 6))
sns.scatterplot(x='concentracao_molar', y='tempo_reacao_segundos', data=df, s=100, color='blue', marker='o')
plt.title('Concentração de Reagente vs Tempo de Reação')
plt.xlabel('Concentração (M)')
plt.ylabel('Tempo de Reação (s)')
plt.grid(True)
plt.show()

# Gráfico de linha para observar a tendência da temperatura ao longo dos experimentos
plt.figure(figsize=(10, 6))
plt.plot(df['experimento'], df['temperatura_celsius'], marker='o', linestyle='-', color='red')
plt.title('Variação da Temperatura ao Longo dos Experimentos')
plt.xlabel('Número do Experimento')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.show()

# Passo 5: Salvar os resultados processados em um novo arquivo CSV
df.to_csv('dados_processados.csv', index=False)
print("\nDados processados foram salvos no arquivo 'dados_processados.csv'.")

# Passo 6: Exemplo de uma função para calcular a taxa de reação com base nos dados
def calcular_taxa_reacao(concentracao, tempo_reacao):
    return concentracao / tempo_reacao

# Calcular a taxa de reação para cada experimento e adicionar ao DataFrame
df['taxa_reacao'] = calcular_taxa_reacao(df['concentracao_molar'], df['tempo_reacao_segundos'])
print("\nDados com a taxa de reação calculada:")
print(df)

# Visualizar a taxa de reação em função da concentração
plt.figure(figsize=(10, 6))
sns.lineplot(x='concentracao_molar', y='taxa_reacao', data=df, marker='o', color='green')
plt.title('Taxa de Reação em Função da Concentração')
plt.xlabel('Concentração (M)')
plt.ylabel('Taxa de Reação (M/s)')
plt.grid(True)
plt.show()

# Passo 7: Relatório final
with open('relatorio_final.txt', 'w') as f:
    f.write("Relatório Final do Projeto de Big Data na Química\n")
    f.write("------------------------------------------------\n\n")
    f.write("Matriz de Correlação:\n")
    f.write(correlation_matrix.to_string())
    f.write("\n\nDados Processados:\n")
    f.write(df.to_string())

print("\nRelatório final salvo no arquivo 'relatorio_final.txt'.")
