#parte de aprendizado
import memoria


while True:
    escolha = int(input("digite 1 para aprender e 2 para pesquisar na memoria"))
    if escolha == 1:
        a = memoria.contatos_lista
        print(a)
        aprender_nome = str(input("digite o nome"))

        aprender_numero = str(input("digite o numero"))

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
    else:
        nome = str(input("digite um nome a ser pesquiado"))
        memoriaP = memoria.contatos_lista
        print(memoriaP)
        if nome in memoriaP:
            pegar_memoria = memoriaP[nome]
            print("O numero de {} é: {}".format(nome, pegar_memoria))
