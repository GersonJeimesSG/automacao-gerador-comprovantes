import pandas   # importar o pandas para trabalhar com tabelas
from fpdf import FPDF #importar criador PDF

tabela_funcionario = pandas.read_csv("base_dados_funcionarios_menor_20.csv") #atrela a variavel, o pandas para lever o arquivo csv.

empresa = "Marcelo e Sara Tranportes Ltda."
cnpj = "01.336.733/0001-64"

for indice, info_funcionario in tabela_funcionario.iterrows(): #criado for para percorrer a tabela. iterrows() é o metodo.
  funcionario = info_funcionario.nome
  cpf = info_funcionario.cpf
  salario = info_funcionario.salario
  texto_recibo = (f"Pelo presente, eu {funcionario}\
  , inscrito no CPF sob nº {cpf}, declaro que RECEBI\
  na data de hoje, o valor de R$ {salario}, por meio de depósito\
  bancário, de {empresa}, inscrito no \
  CNPJ sob nº {cnpj}, referente ao mês anterior\
  ao da data da assinatura, já incluindo todas as horas\
  devidas e benefícios.")

  pdf = FPDF() #para abrir o programa
  pdf.add_page() #para abrir uma pagina em branco.
  pdf.set_font("helvetica","",14) # para definir qual fonte a ser usada. primeira é a fonte, o B é para negrito e o 16 o tamanho.
  pdf.multi_cell(txt=texto_recibo, w=0, align="c") #para criar multiplas celulas. O W é para definir a largura. align para alinhar o texto.
  pdf.ln(30) #para adicionar linhas em branco.

  pdf.multi_cell(txt="Sendo expressão de verdade e sem qualquer coação, firmo o presente.", w=0, align="c") #para criar multiplas celulas. O W é para definir a largura. align para alinhar o texto.
  pdf.ln(30)

  pdf.cell(txt="______, ___ de ______ de _____", w=0, align="c")
  pdf.ln(30)

  pdf.cell(txt="_______________________________", w=0, align="c")
  pdf.ln()

  pdf.cell(txt=funcionario, w=0, align="c")

  pdf.output(f"Recibos/Recibo_{funcionario}.pdf") #para criar um arquivo pdf. Saida
