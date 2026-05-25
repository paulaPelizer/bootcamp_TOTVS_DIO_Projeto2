# 🎓 Bootcamp TOTVS - Portfólio de Projetos de Dados

Este repositório foi criado para centralizar todos os projetos práticos e desafios desenvolvidos por mim durante o Bootcamp da DIO em parceria com a TOTVS. O objetivo é aplicar conceitos do mundo real de Engenharia de Dados, Ciência de Dados e Inteligência Artificial utilizando Python e ferramentas de análise.

---

## 🛠️ Projeto 1: Pipeline ETL com Python e Pandas

### 📝 Descrição do Projeto
Este projeto simula um cenário real de inteligência de negócios, onde foi desenvolvido um pipeline de **ETL (Extract, Transform, Load)** para automatizar a criação de mensagens personalizadas de investimentos e retenção para clientes, baseando-se no saldo atual de cada um.

Para contornar a indisponibilidade de APIs externas e focar na arquitetura de dados e na manipulação local, o projeto foi desenhado utilizando arquivos como fonte e destino.

### 🔄 Como o Pipeline Funciona:
1. **Extract (Extração):** Leitura de uma base bruta de clientes (`clientes.csv`) contendo informações de ID, Nome, Saldo e Tipo de Cartão, utilizando a biblioteca **Pandas**.
2. **Transform (Transformação):** Aplicação de regras de negócio em Python para analisar o saldo de cada cliente e gerar uma mensagem personalizada de marketing direcionada (ex: recomendação de Renda Fixa, Renda Variável ou Reserva de Emergência).
3. **Load (Carregamento):** Exportação e salvamento dos dados transformados em um novo arquivo estruturado (`clientes_com_mensagem.csv`), otimizado com codificação (`utf-8-sig`) e separadores (`;`) para abertura imediata no Microsoft Excel, sistemas de ERP ou ferramentas de BI.

### 📂 Estrutura dos Arquivos do Projeto 1
* `etl_projeto.py`: Código-fonte em Python com as três etapas do pipeline.
* `clientes.csv`: Arquivo com os dados brutos de entrada.
* `clientes_com_mensagem.csv`: Arquivo final gerado após o processamento do pipeline.

### 🚀 Tecnologias Utilizadas
* **Python 3**
* **Pandas** (Manipulação e análise de dados)

---

## 📊 Projeto 2: Dashboard de Vendas - Produção e Gestão de Documentos

### 📝 Descrição do Projeto
O objetivo deste projeto foi desenvolver um dashboard gerencial no Microsoft Excel focado no setor de **BPO (Business Process Outsourcing) de Documentos e Soluções Digitais**. O painel transforma registros brutos de contratos e serviços em uma ferramenta visual interativa para apoiar a tomada de decisão da diretoria comercial.

O cenário simula uma empresa que comercializa licenças e serviços como *Digitalização Inteligente*, *Gestão Documental em Nuvem (ECM/GED)*, *Assinaturas Digitais* e *Outsourcing de Impressão*.

### 🔄 Estrutura do Arquivo Excel
O projeto foi estruturado seguindo as melhores práticas de design e arquitetura de planilhas, dividido em 3 camadas:
1. **`Bases`:** Armazenamento dos dados brutos e históricos de vendas mapeados por mês de vigência por extenso (Janeiro, Fevereiro e Março).
2. **`Cálculos`:** Área de inteligência técnica onde foram aplicadas **Tabelas Dinâmicas** e matrizes de apoio para consolidar faturamentos, volumes e a métrica de **Ticket Médio**.
3. **`Dashboard`:** Interface gráfica voltada para o usuário final com KPIs de faturamento e ticket médio, integrada a **Segmentações de Dados (Filtros Visuais)** conectados diretamente às Tabelas Dinâmicas, permitindo análises cruzadas em tempo real.

### ⚙️ Script de Automação da Base (Python)
Para simular a extração e carga inicial de dados (ETL) no Excel de forma automatizada, foi desenvolvido o script abaixo que popula e gera o arquivo `.xlsx` estruturado com as abas separadas.
