import numpy as np
from scipy.stats import pearsonr
from src import minhastats as ms

TOL=1e-10
x=[1,2,2,4,7]
y=[2,1,3,5,9]

def test_media(): assert abs(ms.media(x)-np.mean(x))<TOL
def test_mediana(): assert abs(ms.mediana(x)-np.median(x))<TOL
def test_moda(): assert ms.moda(x)==[2.0]
def test_variancias():
    assert abs(ms.variancia(x,True)-np.var(x,ddof=1))<TOL
    assert abs(ms.variancia(x,False)-np.var(x,ddof=0))<TOL
def test_desvio_padrao(): assert abs(ms.desvio_padrao(x)-np.std(x,ddof=1))<TOL
def test_percentis():
    assert abs(ms.percentil(x,25)-np.percentile(x,25))<TOL
    assert abs(ms.percentil(x,75)-np.percentile(x,75))<TOL
def test_covariancia(): assert abs(ms.covariancia(x,y)-np.cov(x,y,ddof=1)[0,1])<TOL
def test_correlacao_e_regressao():
    assert abs(ms.correlacao_pearson(x,y)-pearsonr(x,y).statistic)<TOL
    a,b,r2=ms.regressao_linear(x,y); ar,br=np.polyfit(x,y,1)
    assert abs(a-ar)<TOL and abs(b-br)<TOL
    assert abs(r2-pearsonr(x,y).statistic**2)<TOL
