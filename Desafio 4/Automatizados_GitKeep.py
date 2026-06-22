import os
import json
from datetime import datetime

class AutomatizadorGitkeep:
    def __init__(self, diretorio_raiz="."):
        self.diretorio_raiz = diretorio_raiz
        self.diretorio_logs = os.path.join(diretorio_raiz, "logs")
        self.arquivo_log = os.path.join(self.diretorio_logs, "log.json")
        self.criados = []
        self.removidos = []

    def executar(self):
        for raiz, diretorios, arquivos in os.walk(self.diretorio_raiz, topdown=True):
            # Ignora a pasta de logs para não processá-la
            if "logs" in raiz.split(os.sep):
                continue

            # Remove a pasta 'logs' da lista de subdiretórios para evitar que o os.walk entre nela
            if "logs" in diretorios:
                diretorios.remove("logs")

            caminho_gitkeep = os.path.join(raiz, ".gitkeep")
            
            # Lista apenas o que não for o próprio .gitkeep
            itens_no_diretorio = [f for f in arquivos if f != ".gitkeep"] + diretorios

            if len(itens_no_diretorio) == 0:
                # Diretório está vazio (ou só tinha o .gitkeep)
                if ".gitkeep" not in arquivos:
                    with open(caminho_gitkeep, "w") as f:
                        pass
                    self.criados.append(caminho_gitkeep)
            else:
                # Diretório não está vazio
                if ".gitkeep" in arquivos:
                    os.remove(caminho_gitkeep)
                    self.removidos.append(caminho_gitkeep)

        self._salvar_logs()

    def _salvar_logs(self):
        if not os.path.exists(self.diretorio_logs):
            os.makedirs(self.diretorio_logs)

        dados_execucao = {
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "arquivos_criados": self.criados,
            "arquivos_removidos": self.removidos
        }

        historico = []
        if os.path.exists(self.arquivo_log):
            try:
                with open(self.arquivo_log, "r", encoding="utf-8") as f:
                    historico = json.load(f)
                    if not isinstance(historico, list):
                        historico = []
            except json.JSONDecodeError:
                historico = []

        historico.append(dados_execucao)

        with open(self.arquivo_log, "w", encoding="utf-8") as f:
            json.dump(historico, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    automatizador = AutomatizadorGitkeep()
    automatizador.executar()