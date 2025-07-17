import os
import pandas as pd

def carregar_dados(data_dir, nome_arquivo):
    caminho = os.path.join(data_dir, nome_arquivo)
    if os.path.exists(caminho):
        return pd.read_excel(caminho).to_dict(orient='records')
    return []

def salvar_dados(data_dir, nome_arquivo, dados, colunas):
    caminho = os.path.join(data_dir, nome_arquivo)
    df = pd.DataFrame(dados, columns=colunas)
    df.to_excel(caminho, index=False)

def verificar_login(data_dir, email, senha):
    usuarios = carregar_dados(data_dir, 'usuarios.xlsx')
    for u in usuarios:
        if u['email'] == email and str(u['senha']) == str(senha):
            return u['tipo_usuario']
    return None

def criar_planilhas_se_necessarias(data_dir):
    arquivos = {
        "usuarios.xlsx": ["id", "nome", "email", "senha", "tipo_usuario"],
        "empresas.xlsx": ["id", "nome_empresa", "email", "cnpj", "telefone", "endereco", "descricao"],
        "candidatos.xlsx": ["id", "nome", "email", "telefone", "endereco", "formacao", "experiencia", "arquivo_curriculo_base64"],
        "vagas.xlsx": ["id_vaga", "id_empresa", "titulo", "descricao", "local", "tipo_contrato", "salario", "data_criacao"],
        "candidaturas.xlsx": ["id_candidatura", "id_candidato", "id_vaga", "data_envio", "status"]
    }
    for nome, colunas in arquivos.items():
        caminho = os.path.join(data_dir, nome)
        if not os.path.exists(caminho):
            df = pd.DataFrame(columns=colunas)
            df.to_excel(caminho, index=False)
