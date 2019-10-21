from permutacoes import permutacao,Permutacoes






def main():
    mensagem = 0xa23456789fdc1abb
    chave = 0xa123456789abcdef
    x = "{0:b}".format(mensagem).zfill(64)
    x0 = permutacao(Permutacoes.IP,x)
