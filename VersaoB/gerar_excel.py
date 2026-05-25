import pandas as pd

# 1. Criando os dados para a aba 'Bases' (Agora com os meses por extenso)
dados_bases = {
    'ID_Venda': ['V001', 'V002', 'V003', 'V004', 'V005', 'V006', 'V007', 'V008', 'V009'],
    'Data': ['Janeiro', 'Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Março', 'Março', 'Março'],
    'Cliente': ['Banco Alfa', 'Hospital Vida', 'Tech Inova', 'Advocacia Pinheiro', 'Indústria Metal', 'Escola Saber', 'Clínica São José', 'Banco Alfa', 'Logística Express'],
    'Segmento': ['Financeiro', 'Saúde', 'Tecnologia', 'Jurídico', 'Indústria', 'Educação', 'Saúde', 'Financeiro', 'Logística'],
    'Solucao_Servico': ['Gestão Documental Nuvem', 'Digitalização Inteligente', 'Assinatura Digital Eletrônica', 'Outsourcing de Impressão', 'Digitalização Inteligente', 'Gestão Documental Nuvem', 'Assinatura Digital Eletrônica', 'Outsourcing de Impressão', 'Gestão Documental Nuvem'],
    'Qtd': [1, 12000, 250, 5, 45000, 1, 500, 12, 2],
    'Valor_Unitario': [4500.00, 0.35, 12.00, 850.00, 0.28, 3200.00, 10.00, 900.00, 5100.00],
    'Canal_Venda': ['Direto', 'Parceiros', 'Online', 'Direto', 'Direto', 'Online', 'Parceiros', 'Direto', 'Parceiros'],
    'Status': ['Concluído', 'Concluído', 'Concluído', 'Concluído', 'Concluído', 'Em Processo', 'Concluído', 'Concluído', 'Concluído']
}

df_bases = pd.DataFrame(dados_bases)

# Criando a coluna de faturamento multiplicando quantidade por valor unitário
df_bases['Faturamento_Total'] = df_bases['Qtd'] * df_bases['Valor_Unitario']


# 2. Criando os dados consolidados para a aba 'Cálculos' (Resumos para os gráficos)
dados_calculos = {
    'Linha_de_Servico': ['Gestão Documental Nuvem', 'Digitalização Inteligente', 'Assinatura Digital Eletrônica', 'Outsourcing de Impressão'],
    'Total_Faturamento': [17900.00, 16800.00, 8000.00, 15050.00],
    'Contratos_Fechados': [3, 2, 2, 2]
}

df_calculos = pd.DataFrame(dados_calculos)


# 3. Salvando as duas tabelas em um único arquivo Excel, divididos por abas (sheets)
with pd.ExcelWriter('dashboard_vendas.xlsx', engine='openpyxl') as writer:
    df_bases.to_excel(writer, sheet_name='Bases', index=False)
    df_calculos.to_excel(writer, sheet_name='Cálculos', index=False)

print("✨ Sucesso! Arquivo 'dashboard_vendas.xlsx' atualizado com os meses por extenso!")