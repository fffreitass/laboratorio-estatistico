"""Núcleo estatístico próprio do Laboratório Estatístico."""
from collections import Counter
import math

def _clean(values):
    vals=[float(v) for v in values if v is not None and not (isinstance(v,float) and math.isnan(v))]
    if not vals: raise ValueError("A lista precisa conter pelo menos um valor numérico.")
    return vals

def media(values):
    vals=_clean(values); return sum(vals)/len(vals)

def mediana(values):
    vals=sorted(_clean(values)); n=len(vals); meio=n//2
    return vals[meio] if n%2 else (vals[meio-1]+vals[meio])/2

def moda(values):
    vals=_clean(values); c=Counter(vals); maior=max(c.values())
    if maior==1: return []
    return sorted([v for v,n in c.items() if n==maior])

def amplitude(values):
    vals=_clean(values); return max(vals)-min(vals)

def variancia(values,amostral=True):
    vals=_clean(values); n=len(vals)
    if amostral and n<2: raise ValueError("Variância amostral exige pelo menos dois valores.")
    m=media(vals)
    return sum((x-m)**2 for x in vals)/(n-1 if amostral else n)

def desvio_padrao(values,amostral=True):
    return math.sqrt(variancia(values,amostral))

def percentil(values,p):
    vals=sorted(_clean(values))
    if not 0<=p<=100: raise ValueError("p deve estar entre 0 e 100.")
    if len(vals)==1: return vals[0]
    pos=(len(vals)-1)*p/100; baixo=math.floor(pos); alto=math.ceil(pos)
    if baixo==alto: return vals[baixo]
    peso=pos-baixo
    return vals[baixo]+peso*(vals[alto]-vals[baixo])

def quartis(values):
    return percentil(values,25),percentil(values,50),percentil(values,75)

def coeficiente_variacao(values):
    m=media(values)
    if m==0: raise ValueError("Coeficiente de variação indefinido quando a média é zero.")
    return desvio_padrao(values,True)/abs(m)*100

def covariancia(x,y,amostral=True):
    xs,ys=_clean(x),_clean(y)
    if len(xs)!=len(ys): raise ValueError("As listas precisam ter o mesmo tamanho.")
    if amostral and len(xs)<2: raise ValueError("Covariância amostral exige pelo menos dois pares.")
    mx,my=media(xs),media(ys)
    return sum((a-mx)*(b-my) for a,b in zip(xs,ys))/(len(xs)-1 if amostral else len(xs))

def correlacao_pearson(x,y):
    xs,ys=_clean(x),_clean(y)
    if len(xs)!=len(ys) or len(xs)<2: raise ValueError("As listas precisam ter o mesmo tamanho e pelo menos dois pares.")
    mx,my=media(xs),media(ys)
    num=sum((a-mx)*(b-my) for a,b in zip(xs,ys))
    dx=sum((a-mx)**2 for a in xs); dy=sum((b-my)**2 for b in ys)
    den=math.sqrt(dx*dy)
    if den==0: raise ValueError("Correlação indefinida para variável constante.")
    return num/den

def regressao_linear(x,y):
    xs,ys=_clean(x),_clean(y)
    if len(xs)!=len(ys) or len(xs)<2: raise ValueError("As listas precisam ter o mesmo tamanho e pelo menos dois pares.")
    mx,my=media(xs),media(ys); sxx=sum((a-mx)**2 for a in xs)
    if sxx==0: raise ValueError("Não é possível regressão quando X é constante.")
    a=sum((xi-mx)*(yi-my) for xi,yi in zip(xs,ys))/sxx
    b=my-a*mx; r=correlacao_pearson(xs,ys)
    return a,b,r**2
