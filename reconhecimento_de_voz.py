import speech_recognition as sr
import pyttsx3
from config import *
from random import choice
import memoria

reproducao = pyttsx3.init()

resposta = ""
def sai_som(reposta):
	reproducao.say(reposta)
	reproducao.runAndWait()


def assistente():
	print("Oi, qual  é o seu nome completo")
	sai_som("Oi, qual é o seu nome completo")
	while True:
		resposta_erro_aleatoria = choice(lista_erros)
		rec = sr.Recognizer()

		with sr.Microphone() as s:
			rec.adjust_for_ambient_noise(s)

			while True:
				try:
					audio = rec.listen(s)
					user_name = rec.recognize_google(audio, language="pt")
					user_name = verifica_nome(user_name)
					name_list()
					apresentacao = "{}".format(verifica_nome_exist(user_name))
					print(apresentacao)
					sai_som(apresentacao)

					brute_user_name = user_name
					user_name = user_name.split(" ")
					user_name = user_name[0]
					break
				except sr.UnknownValueError:
					sai_som(resposta_erro_aleatoria)
			break

	print("=" * len(apresentacao))
	print("Ouvindo...")

	while True:
		resposta_erro_aleatoria = choice(lista_erros)
		rec = sr.Recognizer()

		with sr.Microphone() as s:
			rec.adjust_for_ambient_noise(s)

			while True:
				try:
					audio = rec.listen(s)
					entrada = rec.recognize_google(audio, language="pt")
					print("{}: {}".format(user_name, entrada))
					# operações matematicas
					if "Quanto é" in entrada or "quanto é" in entrada:

						entrada = entrada.replace("Quanto é", "")
						entrada = entrada.replace("quanto é", "")
						print(entrada)
						resposta = calcula(entrada)
						print(resposta)
					#else:
						#reposta = conversas[entrada]

					if "adicionar" in entrada or "adicione" in entrada:
						
						a = memoria.contatos_lista
						print(a)

						print("fale o nome do contato")
						audio = rec.listen(s)
						aprender_nome = rec.recognize_google(audio, language="pt")

						print("fale o numero do contato")
						audio = rec.listen(s)
						aprender_numero = rec.recognize_google(audio, language="pt")

						#tratamento do texto a aprender
						aspas = "\'"
						aprender = aspas + aprender_nome + aspas + ": " + aspas + aprender_numero + aspas + ","

						#verificar quantas linhas o arquivo tem

						with open('memoria.py') as myfile:
							count = sum(1 for line in myfile)
							print(count)

						#apagar uma linha especifica de um arquivo

						filename = 'memoria.py'
						line_to_delete = count
						initial_line = 1
						file_lines = {}

						with open(filename) as f:
							content = f.readlines() 

						for line in content:
							file_lines[initial_line] = line.strip()
							initial_line += 1

						f = open(filename, "w")
						for line_number, line_content in file_lines.items():
							if line_number != line_to_delete:
								f.write('{}\n'.format(line_content))

						f.close()
						print('Deleted line: {}'.format(line_to_delete))

						#APRENDER O NUMERO
						arquivo = open('memoria.py', 'r') # Abra o arquivo (leitura)
						conteudo = arquivo.readlines()
						conteudo.append(aprender)   # insira seu conteúdo
						conteudo.append('\n'+'}')

						arquivo = open('memoria.py', 'w') # Abre novamente o arquivo (escrita)
						arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

						arquivo.close()

					if "exibir" in entrada:
						print("fale o nome da pessoa para procurar o numero")
						audio = rec.listen(s)
						nome = rec.recognize_google(audio, language="pt")
						resposta = str(memoria.contatos_lista[nome])
						print("o numero é: {}".format(resposta))

					print("Assistente: {}".format(resposta))
					sai_som("{}".format(resposta))

				except sr.UnknownValueError:
					sai_som(resposta_erro_aleatoria)


if __name__ == '__main__':
	intro()
	sai_som("Iniciando")
	assistente()
