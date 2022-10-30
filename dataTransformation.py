import pandas
import tabula
# import requests

# 2.1 Extrair do pdf do anexo I do teste 1 acima os dados da tabela Rol de Procedimentos e Eventos em Saúde (todas as páginas);

# Existem duas formas nesse caso, você pode baixar e extrair do arquivo

# file = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.pdf'
# response = requests.get(file)
# open("AnexoI.pdf", "wb").write(response.content)
# pdf = "AnexoI.pdf"
# table = tabula.read_pdf(pdf, pages='all')

# Ou extrair diretamente do link, que é mais prático, mais rápido e deixa o codigo mais limpo
pdf = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.pdf'

# Salvar dados em uma tabela estruturada, em csv;

csv_table = tabula.convert_into(
    pdf, 'tabelaAnexoI.csv', output_format="csv", pages='all')

# TODO e Zipar o csv num arquivo "Teste_{seu_nome}.zip"
# TODO Com a legenda no rodapé substituir os dados abreviados das colunas OD e AMB para as respectivas descrições.
# Legenda:
# OD: Seg. Odontológica
# AMB: Seg. Ambulatorial
