texto=[]
def menu():
	print("digite '/salvar' para salvar um novo arqui de texto")
	print("digite '/adicionar' para adicionar linhas ao arquivo existente")
	print("digite '/texto' para mostrar o texto escrito")
	print("digite '/menu' para mostrar as informacooes novamente")
	
	texto=[]
	EscreverTexto()

def LeArquivo():
	arq=open('texto.text','r')
	print(arq.readlines())
	arq.close()
	
def SalvarTexto():
	linha=""
	arq=open('texto.txt','w')	
	for i in range(0,len(texto)):
		linha=texto[i]
		arq.writelines(f"{linha}\n")
	print("texto salvo!")
	arq.close()
	EscreverTexto()		

		
def LeArquivo():
	arq=open('texto.txt','r')
	print(arq.readlines())
	arq.close()
	EscreverTexto()
	
def AdLinhas():
	linha=""
	arq=open('texto.txt','a')	
	for i in range(0,len(texto)):
		linha=texto[i]
		arq.writelines(f"{linha}\n")
	print("Linhas adicionadas!")
	arq.close()
	texto.clear()
	EscreverTexto()
	

def EscreverTexto():
	sentenca=input("")
	while sentenca!= " ":
		if sentenca == "/salvar":
			SalvarTexto()
		elif sentenca == "/adicionar":
			AdLinhas()
		elif sentenca == "/menu":
			menu()
		elif sentenca == "/texto":
			LeArquivo()
		else:
			texto.append(sentenca)
			sentenca=input("")
	print("fim do texto")
	LeArquivo()
	
menu()
