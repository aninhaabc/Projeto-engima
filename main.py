from enigma import gerar_matrizes_de_permutacao, encriptar_enigma, decriptar_enigma, ALFABETO

if __name__ == "__main__":
    mensagem = "aaafdsds"

    # Usar o tamanho do alfabeto para as matrizes de permutação
    N = len(ALFABETO)
    P, Q = gerar_matrizes_de_permutacao(N)
    
    mensagem_cifrada = encriptar_enigma(mensagem, P, Q)
    print("Mensagem Cifrada:", mensagem_cifrada)
    
    mensagem_recuperada = decriptar_enigma(mensagem_cifrada, P, Q)
    print("Mensagem Recuperada:", mensagem_recuperada)
