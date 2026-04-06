from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()


caminho = os.path.join(os.path.dirname(__file__), "..", "vendas.csv")
df = pd.read_csv(caminho)

df['faturamento'] = df['valor'] * df['quantidade']

@app.get("/")
def home():
    return {"mensagem": "API funcionando!"}

@app.get("/faturamento")
def faturamento():
    total = df['faturamento'].sum()
    return {"faturamento_total": float(total)}

@app.get("/top-produtos")
def top_produtos():
    resultado = df.groupby('produto')['quantidade'].sum()
    return resultado.to_dict()

@app.get("/vendas-mes")
def vendas_mes():
    df['mes'] = pd.to_datetime(df['data']).dt.month
    resultado = df.groupby('mes')['faturamento'].sum()
    return resultado.to_dict()