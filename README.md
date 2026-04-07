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

## 📊 Demonstração

### 📌 Documentação da API
<img width="1277" height="980" alt="Captura de tela 2026-04-06 140618" src="https://github.com/user-attachments/assets/3b42fca2-8ce4-4fe9-9e2e-a1e46e95533c" />


### 📌 Faturamento por mês
<img width="1279" height="981" alt="Captura de tela 2026-04-06 140617" src="https://github.com/user-attachments/assets/037dd2a1-0526-46da-9c4a-83edee1672c1" />


### 📌 Top produtos
<img width="1274" height="980" alt="Captura de tela 2026-04-06 140619" src="https://github.com/user-attachments/assets/4429492b-1a51-48c4-9856-58de00c34c0d" />
