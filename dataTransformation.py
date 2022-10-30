import pandas as pd
import tabula
from zipfile36 import ZipFile

# 2.1 Extrair do pdf do anexo I do teste 1 acima os dados da tabela Rol de Procedimentos e Eventos em Saúde (todas as páginas);

# Existem duas formas nesse caso, você pode baixar e extrair do arquivo

# import requests
# file = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.pdf'
# response = requests.get(file)
# open("AnexoI.pdf", "wb").write(response.content)
# pdf = "AnexoI.pdf"
# table = tabula.read_pdf(
#     pdf, pages='3', encoding="utf-8", multiple_tables=False)

# Ou extrair diretamente do link, que é mais prático, mais rápido e deixa o codigo mais limpo

pdf = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.pdf'

# Salvar dados em uma tabela estruturada, em csv;
print('Extraindo dados e salvando em uma tabela csv. Aguarde...')
csv_table = tabula.convert_into(
    pdf, 'tabelaAnexoI.csv', output_format="csv", pages='all')
print('Arquivo csv criado com sucesso.')

# Com a legenda no rodapé substituir os dados abreviados das colunas OD e AMB para as respectivas descrições.
# Legenda:
# OD: Seg. Odontológica
# AMB: Seg. Ambulatorial

df = pd.read_csv("tabelaAnexoI.csv", encoding='cp1252')
print('Substituindo dados abreviados. Aguarde.')
df['OD'] = df['OD'].replace({'OD': 'Seg. Odontológica'})
df['AMB'] = df['AMB'].replace({'AMB': 'Seg. Ambulatorial'})
df.to_csv("tabelaAnexoI.csv", index=False, encoding='utf-8')
print('Substituição concluida com sucesso')

# Zipar o csv num arquivo "Teste_{seu_nome}.zip"
with ZipFile('Teste_Rafaelly.zip', 'w') as zipped_f:
    print('Compactando arquivo csv...')
    zipped_f.write("tabelaAnexoI.csv")

print('Finalizado com sucesso!')
