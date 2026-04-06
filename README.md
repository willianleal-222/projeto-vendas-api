# Projeto Vendas API

API desenvolvida com FastAPI para análise de vendas, permitindo consulta de faturamento, produtos mais vendidos e vendas por período.

## Como rodar o projeto

pip install fastapi uvicorn pandas  
cd api  
uvicorn main:app --reload  

## Rotas

/faturamento → retorna o faturamento total  
/top-produtos → retorna os produtos mais vendidos  
/vendas-mes → retorna o faturamento por mês  

## Exemplo de resposta

/faturamento

{
  "faturamento_total": 8510
}

## Tecnologias

Python  
Pandas  
FastAPI  
