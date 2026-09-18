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
Para variáveis numéricas, a aplicação apresenta tabela de frequências por classes, medidas de tendência central e dispersão, histograma e boxplot. Os possíveis outliers são identificados pela regra:

IQR = Q3 − Q1

Limite inferior = Q1 − 1,5 IQR

Limite superior = Q3 + 1,5 IQR

Para variáveis categóricas, são apresentadas frequências, percentuais e gráficos de barras; quando há poucas categorias, também é exibido gráfico de pizza.

## 6. Módulo 3 — Probabilidade e simulação
A Lei dos Grandes Números é demonstrada por lançamentos simulados de uma moeda, acompanhando a frequência relativa de caras e sua aproximação de 0,5.

O Teorema Central do Limite é demonstrado por amostras aleatórias repetidas de uma variável numérica do dataset. O usuário controla o número de repetições e o tamanho da amostra, e a aplicação apresenta o histograma das médias amostrais.

## 7. Módulo 4 — Distribuições teóricas
A aplicação permite comparar o histograma de uma variável numérica com uma Normal, usando média e desvio padrão estimados dos dados, ou com uma Poisson, usando λ igual à média.

A comparação é interpretada visualmente e não é apresentada como teste formal de aderência.

## 8. Módulo 5 — Correlação e regressão
O usuário escolhe duas variáveis numéricas. A aplicação apresenta o diagrama de dispersão, correlação de Pearson, reta de mínimos quadrados, equação, R² e uma caixa para previsão.

A interpretação é feita no contexto do modelo linear. É destacado que correlação não implica causalidade.

## 9. Módulo 6 — Descobertas
As três descobertas a seguir devem ser conferidas na execução final da aplicação e acompanhadas dos respectivos prints.

1. **Distribuição de balance:** a variável apresenta assimetria à direita, com média superior à mediana e valores extremos.
2. **Associação entre pdays e previous:** as duas variáveis apresentam associação linear positiva moderada no conjunto.
3. **Teorema Central do Limite:** conforme o tamanho da amostra aumenta, as médias amostrais ficam mais concentradas em torno da média e apresentam formato aproximadamente normal.

## 10. Conclusão
O laboratório reúne os principais conceitos estatísticos solicitados na atividade em uma aplicação interativa. A separação entre o núcleo estatístico próprio e a interface permite verificar que as medidas apresentadas ao usuário não dependem diretamente das funções estatísticas prontas das bibliotecas de referência.

## 11. Evidências
Inserir aqui capturas da aplicação para os módulos 0 a 6 e, especialmente, os resultados utilizados para sustentar as três descobertas.
