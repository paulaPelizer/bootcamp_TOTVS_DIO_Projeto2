## 📊 Projeto 2: Dashboards de Vendas Interativos (Excel 365)

Este projeto engloba duas versões de painéis gerenciais focados em conversão de dados brutos para suporte à tomada de decisão. Ambos utilizam a arquitetura de planilhas dividida em 3 camadas: `Bases`, `Cálculos` e `Dashboard`.

---

### 🟢 Versão A: Análise de Vendas de Assinaturas (Xbox Game Pass) - *Escopo Original do Exercício*

#### 📝 Descrição
Análise exploratória e visual focada na receita e comportamento de assinantes do serviço **Xbox Game Pass**. O objetivo é identificar a performance de diferentes planos (Core, Standard, Ultimate), tipos de faturamento (Mensal, Trimestral, Anual) e o impacto de cupons de desconto.

#### 🔄 Estrutura da Planilha
* **`Bases`:** Contém dados detalhados como `Subscriber ID`, `Name`, `Plan`, `Start Date`, `Subscription Type` e agregadores (`EA Play Season Pass`, `Minecraft Season Pass` e cupons).
* **`Cálculos`:** Consolidação técnica respondendo a dores de negócio, como faturamento de planos anuais segmentado por auto-renovação e totalização de receitas agregadas de passes de temporada.
* **`Dashboard`:** Interface em Dark Mode utilizando a identidade visual da marca (paleta com tons `#9BC848` e `#22C55E`), equipada com gráficos dinâmicos para monitorar as receitas agregadas.

---

### 🔵 Versão B: Gestão e BPO de Documentos - *Extensão de Portfólio (Cenário de Produção)*

#### 📝 Descrição
Uma adaptação autoral voltada para o mercado corporativo de serviços. Simula o controle comercial de uma empresa de tecnologia focada em **BPO de Documentos e Soluções Digitais** (*Digitalização Inteligente*, *Gestão Documental em Nuvem ECM/GED*, *Assinaturas Eletrônicas* e *Outsourcing de Impressão*).

#### 🔄 Estrutura da Planilha
* **`Bases`:** Histórico de contratos mapeados por volumetrias e organizados por competência mensal por extenso (Janeiro, Fevereiro e Março).
* **`Cálculos`:** Tabelas dinâmicas configuradas para segmentar a receita total por linha de serviço e monitorar a evolução do **Ticket Médio** corporativo.
* **`Dashboard`:** Painel executivo integrado a **Segmentações de Dados (Slicers)** conectadas diretamente às tabelas dinâmicas, permitindo filtros cruzados por *Canal de Venda* e *Segmento de Mercado*.

#### ⚙️ Automação de Carga Inicial (Python)
Para a inicialização da base desta versão, foi utilizado o seguinte script de apoio em Python para gerar o arquivo estruturado:
