import subprocess as executarComando
import dados

comando = dados.meu_comando
senha = dados.minha_senha

if __name__ == "__main__":
    try:
        terminal = f'echo "{senha}" | sudo -S {comando}'
        executarComando.check_output(terminal, shell=True, text=True)
    except:
        print("Comando ou senha de usuario incorreto")