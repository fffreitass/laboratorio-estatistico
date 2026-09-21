# RELATÓRIO — Laboratório Estatístico Interativo

## 1. Identificação
**Estudante:** Maria Luiza de Freitas Viana  
**Matrícula:** 72650012  
**Grupo:** Individual

## 2. Dataset e justificativa
Foi escolhido o dataset **Bank Marketing**, disponibilizado pelo UCI Machine Learning Repository. O conjunto possui 45.211 registros e 17 variáveis na versão bank-full.csv, incluindo variáveis numéricas e categóricas suficientes para os requisitos do projeto.

Fonte original: https://archive.ics.uci.edu/dataset/222/bank%2Bmarketing

A temática permite analisar características dos clientes e resultados de campanhas de marketing bancário, além de oferecer variáveis adequadas para estatística descritiva, simulação, distribuição, correlação e regressão.

## 3. Núcleo estatístico próprio
As medidas exibidas pela aplicação são calculadas em src/minhastats.py.

### Média
x̄ = (1/n) Σ xi

### Mediana
Os valores são ordenados. Para quantidade ímpar, usa-se o elemento central; para quantidade par, calcula-se a média dos dois elementos centrais.

### Moda
É identificada por contagem das ocorrências de cada valor.

### Amplitude
A = xmax − xmin

### Variância
Populacional:
σ² = Σ(xi − μ)² / n

Amostral:
s² = Σ(xi − x̄)² / (n − 1)

### Desvio padrão
É a raiz quadrada da variância.

### Percentis e quartis
Foi implementada interpolação linear sobre os valores ordenados. Q1, Q2 e Q3 correspondem aos percentis 25, 50 e 75.

### Coeficiente de variação
CV = (s / |x̄|) × 100

### Covariância
Cov(X,Y) = Σ[(xi − x̄)(yi − ȳ)] / (n − 1)

### Correlação de Pearson
r = Σ[(xi − x̄)(yi − ȳ)] / √[Σ(xi − x̄)² Σ(yi − ȳ)²]

### Regressão linear
A inclinação foi obtida por:
a = Σ[(xi − x̄)(yi − ȳ)] / Σ(xi − x̄)²

e o intercepto por:
b = ȳ − ax̄

A previsão é ŷ = ax + b.

## 4. Validação
Os testes automatizados estão em tests/test_minhastats.py. As funções próprias são comparadas com NumPy e SciPy, utilizando tolerância numérica de 1e-10.

São testados média, mediana, moda, variâncias populacional e amostral, desvio padrão, percentis, covariância, correlação e regressão.

## 5. Módulo 2 — Estatística descritiva
Para variáveis numéricas, a aplicação apresenta tabela de frequências por classes, medidas de tendência central e dispersão, histograma e boxplot. Os possíveis outliers são identificados pela regra IQR.

## 6. Módulo 3 — Probabilidade e simulação
A Lei dos Grandes Números é demonstrada por lançamentos simulados de uma moeda. O Teorema Central do Limite é demonstrado por amostras aleatórias repetidas de uma variável numérica do dataset.

## 7. Módulo 4 — Distribuições teóricas
A aplicação permite comparar o histograma de uma variável numérica com distribuições teóricas, com parâmetros estimados a partir dos dados.

## 8. Módulo 5 — Correlação e regressão
O usuário escolhe duas variáveis numéricas. A aplicação apresenta o diagrama de dispersão, correlação de Pearson, reta de mínimos quadrados, equação, R² e previsão. É destacado que correlação não implica causalidade.

## 9. Módulo 6 — Descobertas

### Descoberta 1 — Distribuição da variável `balance`
A variável `balance` apresentou média de **1362,27** e mediana de **448,00**. O desvio-padrão amostral foi de **3044,77** e o coeficiente de variação foi de aproximadamente **223,51%**. Os resultados indicam forte assimetria à direita.

### Descoberta 2 — Associação entre `pdays` e `previous`
Foi obtido coeficiente de correlação de Pearson de aproximadamente **r = 0,4548** e coeficiente de determinação de **R² = 0,2069**. Há associação linear positiva, sem implicar causalidade.

### Descoberta 3 — Teorema Central do Limite
Na simulação foi utilizada a variável `age`, com amostras de tamanho **n = 30**. As médias amostrais apresentaram distribuição aproximadamente normal.

## 10. Conclusão
O laboratório reúne os principais conceitos estatísticos solicitados na atividade em uma aplicação interativa.

## 11. Evidências
As capturas registram a execução da aplicação e os principais resultados.

![Dataset carregado](evidencias/01-dataset.png.png)

![Estatísticas da variável balance](evidencias/02-estatistica-balance.png.png)

![Histograma e boxplot de balance](evidencias/03-histograma-boxplot-balance.png.png)

![Simulação do Teorema Central do Limite](evidencias/04-teorema-central-limite.png.png)

![Regressão entre pdays e previous](evidencias/05-regressao-pdays-previous.png.png)

## 12. Vídeo demonstrativo
O vídeo de apresentação e explicação do projeto está disponível no Google Drive:

https://drive.google.com/file/d/1PwxZUIEQZivLGEJ_X2EIPyswAjGyVKK7/view?usp=drivesdk
