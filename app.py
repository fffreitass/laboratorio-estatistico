import math
import io, zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import requests
from scipy.stats import poisson
from src import minhastats as ms

st.set_page_config(page_title="Laboratório Estatístico",layout="wide")
st.title("📊 Laboratório Estatístico Interativo")
st.caption("Maria Luiza de Freitas Viana — 72650012 | Projeto individual")

@st.cache_data
def carregar_dados():
    try:
        return pd.read_csv("bank-full.csv", sep=";")
    except Exception:
        return None

df=carregar_dados()
if df is None:
    up=st.file_uploader("Envie bank-full.csv se o download automático falhar.",type=["csv"])
    if up is not None: df=pd.read_csv(up,sep=";")
    else:
        st.info("Baixe bank-full.csv na página oficial da UCI e envie acima.")
        st.stop()

st.success(f"Dataset carregado: {len(df):,} registros e {len(df.columns)} variáveis.")
num_cols=df.select_dtypes(include=np.number).columns.tolist()
cat_cols=df.select_dtypes(exclude=np.number).columns.tolist()
tabs=st.tabs(["Módulo 0","Módulo 1","Módulo 2","Módulo 3","Módulo 4","Módulo 5","Módulo 6"])

with tabs[0]:
    st.subheader("Dados reais")
    st.write("Fonte: UCI Machine Learning Repository — Bank Marketing.")
    st.dataframe(df.head(20),use_container_width=True)
    st.write(f"Variáveis numéricas: {len(num_cols)} | categóricas: {len(cat_cols)}")

with tabs[1]:
    st.subheader("Núcleo estatístico próprio")
    c=st.selectbox("Variável numérica",num_cols,key="m1"); x=df[c].dropna().tolist()
    q1,med,q3=ms.quartis(x)
    cols=st.columns(5)
    for box,label,val in zip(cols,["Média","Mediana","DP amostral","Amplitude","CV"],[ms.media(x),med,ms.desvio_padrao(x),ms.amplitude(x),ms.coeficiente_variacao(x)]):
        box.metric(label,f"{val:.4f}")
    st.write("Quartis:",{"Q1":q1,"Q2":med,"Q3":q3})
    st.info("Os testes automatizados em tests/test_minhastats.py usam tolerância 1e-10.")

with tabs[2]:
    st.subheader("Estatística descritiva interativa")
    tipo=st.radio("Tipo de variável",["Numérica","Categórica"],horizontal=True)
    if tipo=="Numérica":
        c=st.selectbox("Variável",num_cols,key="m2n"); x=df[c].dropna().astype(float).tolist()
        q1,med,q3=ms.quartis(x); iqr=q3-q1; lo=q1-1.5*iqr; hi=q3+1.5*iqr
        out=sum(v<lo or v>hi for v in x)
        hist=pd.cut(pd.Series(x),bins="auto").value_counts().sort_index().rename_axis("Classe").reset_index(name="Frequência")
        hist["Frequência relativa (%)"]=hist["Frequência"]/len(x)*100
        st.dataframe(hist,use_container_width=True)
        st.write(f"Média: {ms.media(x):.4f} | Mediana: {med:.4f} | DP: {ms.desvio_padrao(x):.4f} | Outliers pelo IQR: {out}")
        fig,ax=plt.subplots(); ax.hist(x,bins="auto"); ax.set_title(f"Histograma — {c}"); ax.set_xlabel(c); ax.set_ylabel("Frequência"); st.pyplot(fig); plt.close(fig)
        fig,ax=plt.subplots(); ax.boxplot(x,vert=False); ax.set_title(f"Boxplot — {c}"); st.pyplot(fig); plt.close(fig)
        if abs(ms.media(x)-med)<.05*max(ms.desvio_padrao(x),1): assim="aproximadamente simétrica"
        elif ms.media(x)>med: assim="assimétrica à direita"
        else: assim="assimétrica à esquerda"
        st.info(f"Interpretação automática: {c} é {assim}. Foram identificados {out} possíveis outliers pela regra do IQR.")
    else:
        c=st.selectbox("Variável",cat_cols,key="m2c"); freq=df[c].value_counts(dropna=False)
        tab=pd.DataFrame({"Frequência":freq,"Percentual (%)":freq/len(df)*100})
        st.dataframe(tab,use_container_width=True)
        fig,ax=plt.subplots(); freq.head(15).plot(kind="bar",ax=ax); ax.set_title(f"Barras — {c}"); ax.set_ylabel("Frequência"); st.pyplot(fig); plt.close(fig)
        if len(freq)<=8:
            fig,ax=plt.subplots(); ax.pie(freq.values,labels=freq.index.astype(str),autopct="%1.1f%%"); ax.set_title(f"Pizza — {c}"); st.pyplot(fig); plt.close(fig)

with tabs[3]:
    st.subheader("Probabilidade e simulação")
    exp=st.radio("Experimento",["Lei dos Grandes Números","Teorema Central do Limite"],horizontal=True)
    reps=st.slider("Número de repetições",100,10000,2000,100)
    if exp=="Lei dos Grandes Números":
        lanc=st.slider("Número de lançamentos",100,100000,10000,100)
        rng=np.random.default_rng(42); resultados=rng.integers(0,2,size=lanc); fr=np.cumsum(resultados)/np.arange(1,lanc+1)
        fig,ax=plt.subplots(); ax.plot(fr); ax.axhline(.5,linestyle="--"); ax.set_xlabel("Lançamentos"); ax.set_ylabel("Frequência relativa de cara"); ax.set_title("Convergência para 0,5"); st.pyplot(fig); plt.close(fig)
    else:
        c=st.selectbox("Variável do dataset",num_cols,key="m3"); n=st.slider("Tamanho de cada amostra",2,500,30)
        rng=np.random.default_rng(42); arr=df[c].dropna().to_numpy(float)
        means=[rng.choice(arr,size=n,replace=True).mean() for _ in range(reps)]
        fig,ax=plt.subplots(); ax.hist(means,bins="auto"); ax.set_title(f"Médias amostrais — {c}, n={n}"); ax.set_xlabel("Média amostral"); st.pyplot(fig); plt.close(fig)
        st.write(f"Média das médias: {ms.media(means):.4f} | DP das médias: {ms.desvio_padrao(means):.4f}")

with tabs[4]:
    st.subheader("Distribuições teóricas")

    tipo = st.radio(
        "Distribuição candidata",
        ["Normal", "Poisson"],
        horizontal=True
    )

    if tipo == "Normal":
        c = st.selectbox("Variável numérica", num_cols, key="m4_normal")
        x = df[c].dropna().astype(float).to_numpy()

        fig, ax = plt.subplots()
        ax.hist(x, bins="auto", density=True, alpha=.55, label="Dados")

        mu = ms.media(x)
        sd = ms.desvio_padrao(x, False)
        grid = np.linspace(x.min(), x.max(), 400)

        y = np.exp(-.5 * ((grid - mu) / sd) ** 2) / (
            sd * math.sqrt(2 * math.pi)
        )

        ax.plot(
            grid,
            y,
            label=f"Normal (μ={mu:.2f}, σ={sd:.2f})"
        )

        ax.legend()
        ax.set_title(f"Normal sobre histograma — {c}")
        st.pyplot(fig)
        plt.close(fig)

        st.info(
            "A curva Normal foi ajustada usando a média e o desvio-padrão "
            "estimados a partir dos dados. A comparação visual permite observar "
            "o quanto a distribuição empírica se aproxima ou se afasta do modelo Normal."
        )

    else:
        poisson_cols = [
            col for col in ["campaign", "previous"]
            if col in df.columns
        ]

        c = st.selectbox(
            "Variável de contagem",
            poisson_cols,
            key="m4_poisson"
        )

        x = df[c].dropna().astype(int).to_numpy()

        fig, ax = plt.subplots()

        valores, contagens = np.unique(x, return_counts=True)
        frequencias = contagens / len(x)

        ax.bar(
            valores,
            frequencias,
            alpha=.55,
            label="Dados"
        )

        lam = ms.media(x)

        k = np.arange(0, int(x.max()) + 1)

        ax.plot(
            k,
            poisson.pmf(k, lam),
            "o-",
            label=f"Poisson (λ={lam:.2f})"
        )

        ax.set_xlim(-0.5, min(int(x.max()) + 0.5, 25))
        ax.set_xlabel(c)
        ax.set_ylabel("Probabilidade / frequência relativa")
        ax.set_title(f"Poisson sobre distribuição observada — {c}")
        ax.legend()

        st.pyplot(fig)
        plt.close(fig)

        st.info(
            "A distribuição de Poisson é apropriada para variáveis discretas "
            "de contagem. Por isso, nesta análise são utilizadas variáveis como "
            "'campaign' e 'previous', em vez de idade."
        )

with tabs[5]:
    st.subheader("Correlação e regressão linear")
    c1,c2=st.columns(2); X=c1.selectbox("Variável X",num_cols,key="xreg"); Y=c2.selectbox("Variável Y",num_cols,index=min(1,len(num_cols)-1),key="yreg")
    pares=df[[X,Y]].dropna(); xs=pares[X].astype(float).tolist(); ys=pares[Y].astype(float).tolist()
    r=ms.correlacao_pearson(xs,ys); a,b,r2=ms.regressao_linear(xs,ys)
    fig,ax=plt.subplots(); ax.scatter(xs,ys,s=8,alpha=.35); line=np.linspace(min(xs),max(xs),100); ax.plot(line,a*line+b); ax.set_xlabel(X); ax.set_ylabel(Y); ax.set_title("Dispersão e reta de regressão"); st.pyplot(fig); plt.close(fig)
    st.write(f"r = {r:.4f} | R² = {r2:.4f} | ŷ = {a:.4f}x + {b:.4f}")
    st.write(f"Interpretação: para cada aumento de 1 unidade em X, a previsão média de Y varia {a:.4f} unidade(s), dentro do modelo linear. Correlação não implica causalidade.")
    xv=st.number_input("Digite um valor de X para previsão",value=float(ms.media(xs))); st.metric("Ŷ previsto",f"{a*xv+b:.4f}")

with tabs[6]:
    st.subheader("Relatório de descobertas")
    st.write("As descobertas abaixo são pontos iniciais e devem ser confirmadas pelos resultados exibidos nos módulos anteriores.")
    st.markdown("**Descoberta 1 — distribuição/outliers:** balance apresenta forte assimetria à direita, com média acima da mediana e valores extremos.")
    st.markdown("**Descoberta 2 — associação:** pdays e previous apresentam associação linear positiva moderada no conjunto analisado.")
    st.markdown("**Descoberta 3 — simulação:** aumentando o tamanho das amostras no TCL, as médias amostrais tendem a se concentrar ao redor da média e adquirir formato aproximadamente normal.")
