# Laboratório Estatístico Interativo

**Autora:** Maria Luiza de Freitas Viana — matrícula 72650012  
**Grupo:** Individual (Maria Luiza de Freitas Viana)

## Dataset
Bank Marketing — UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/222/bank%2Bmarketing

O projeto utiliza o arquivo bank-full.csv do conjunto Bank Marketing.

## Objetivo
Laboratório interativo em Python e Streamlit com núcleo estatístico próprio, testes automatizados, estatística descritiva, simulações de Monte Carlo, distribuições teóricas, correlação e regressão linear.

## Estrutura
- app.py — interface e módulos 0–6.
- src/minhastats.py — núcleo estatístico próprio.
- tests/test_minhastats.py — testes automatizados.
- RELATORIO.md — relatório técnico.
- requirements.txt — dependências.

## Instalação
python -m venv .venv
pip install -r requirements.txt

## Execução
streamlit run app.py

A aplicação tenta baixar os dados da UCI. Se não conseguir, é possível enviar bank-full.csv pelo componente de upload.

## Testes
pytest -q

A tolerância numérica documentada nos testes é 1e-10.

## Evidências
Antes da entrega final, adicione capturas de tela ou um GIF da aplicação funcionando.
