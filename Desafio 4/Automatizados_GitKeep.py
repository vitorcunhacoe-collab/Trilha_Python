#Importanto bibliotecas

import os #pra manipular com arquivos do computador
import json #pra escrever o relatório
from datetime import datetime #pra saber o momento em que tais mudanças foram feitas e colocar no relatório

class AutomatizadorGitkeep: #a classe que vai executar
    def __init__(self, diretorio_raiz="."): #começo a classe dentro do diretório raiz atual caso não especifique outro
        self.diretorio_raiz = diretorio_raiz
        self.diretorio_logs = os.path.join(diretorio_raiz, "logs") #caminho pra pasta onde o objeto vai fazer o registro
        self.arquivo_log = os.path.join(self.diretorio_logs, "log.json") #nome do relatório "log"
        self.criados = [] #lista pra guardar arquivos criados, nesse caso o .gitkeep criado
        self.removidos = [] #lista pra guardar arquivos apagados, nesse caso o .gitkeep apagado

    def executar(self): #ja tenho minha classe, oq ela vai fazer é essa função
        for raiz, diretorios, arquivos in os.walk(self.diretorio_raiz, topdown=True): #ele checa pasta por pasta do diretório e checa quais arquivos estão dentro
            # Ignora a pasta de logs para não processá-la e entrar num loop
            if "logs" in raiz.split(os.sep):
                continue

            # Remove a pasta 'logs' da lista de subdiretórios para evitar que o os.walk entre nela, só pra ter certeza que ele não vai nem mais tentar
            if "logs" in diretorios:
                diretorios.remove("logs")

            caminho_gitkeep = os.path.join(raiz, ".gitkeep") #define qual é o arquivo que ele tem que checar se existe e como achar ele
            
            # Lista apenas o que não for o próprio .gitkeep
            itens_no_diretorio = [f for f in arquivos if f != ".gitkeep"] + diretorios

            if len(itens_no_diretorio) == 0:
                # Diretório está vazio (ou só tinha o .gitkeep)
                if ".gitkeep" not in arquivos:
                    with open(caminho_gitkeep, "w") as f: #cria o arquivo gitkeep como se fosse escrever
                        pass #não escreve nada, deixa em branco mais criado
                    self.criados.append(caminho_gitkeep) #registra que criou
            else:
                # Diretório não está vazio
                if ".gitkeep" in arquivos:
                    os.remove(caminho_gitkeep) #não precisa dele se não tiver vazio
                    self.removidos.append(caminho_gitkeep) #registra que removeu

        self._salvar_logs() #depois de tudo ele escreve o log

    def _salvar_logs(self): #como vai ser esse log?
        if not os.path.exists(self.diretorio_logs):
            os.makedirs(self.diretorio_logs) #se a pasta logs ainda não existir ele cria

        dados_execucao = {
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "arquivos_criados": self.criados,
            "arquivos_removidos": self.removidos
        } #criação do bloco de texto do relatório, data e hora exata, oq foi criado e oq foi apagado

        historico = [] #lista vazia pra armazenar logs anteriores
        if os.path.exists(self.arquivo_log):
            try:
                with open(self.arquivo_log, "r", encoding="utf-8") as f: #tenta abrir o relatório pra ler, se arquivo existir e tiver coisas dentro
                    historico = json.load(f) #ele passa conteúdo do arquivo pra variável
                    if not isinstance(historico, list): # se o conteúdo do log antigo não for uma lista válida, recomeça do zero
                        historico = []
            except json.JSONDecodeError:
                historico = []

        historico.append(dados_execucao) #adiciona novo relatório ao histórico

        with open(self.arquivo_log, "w", encoding="utf-8") as f:
            json.dump(historico, f, indent=4, ensure_ascii=False) #salva tudo escrito no log


if __name__ == "__main__":
    automatizador = AutomatizadorGitkeep()
    automatizador.executar()