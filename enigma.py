import numpy as np
from typing import Tuple

def gerar_matrizes_de_permutacao(N : int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gera duas matrizes de permutação de tamanho N x N.
    """
    P = np.eye(N)
    np.random.shuffle(P)

    Q = np.eye(N)
    np.random.shuffle(Q)
    
    return P, Q

def encriptar_enigma(mensagem : str, P : np.ndarray, Q : np.ndarray) -> str:
    """
    Encripta a mensagem usando duas matrizer de permutação
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    N = len(alfabeto)

    mensagem = mensagem.lower()
    mensagem_filtrada = ''.join([letra for letra in mensagem if letra in alfabeto])

    M = np.zeros((N, len(mensagem_filtrada)))
    for i, letra in enumerate(mensagem_filtrada):
        idx = alfabeto.index(letra)
        M[idx,i] = 1

    M_cifrada = np.dot(Q, np.dot(P, M))

    mensagem_cifrada = ""
    for i in range(M_cifrada.shape[1]):
        idx = np.argmax(M_cifrada[: , i])
        mensagem_cifrada += alfabeto[idx]
    
    return mensagem_cifrada


def decriptar_enigma(mensagem_encriptada : str, P : np.ndarray, Q : np.ndarray) -> str:
    """
    Decripta a mensagem usando as inversas das matrizes de permutação
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    N = len(alfabeto)

    M_cifrada = np.zeros((N, len(mensagem_encriptada)))
    for i, letra in enumerate(mensagem_encriptada):
        idx = alfabeto.index(letra)
        M_cifrada[idx, i] = 1
    
    P_inv = np.linalg.inv(P)
    Q_inv = np.linalg.inv(Q)
    M_recuperada = np.dot(P_inv, np.dot(Q_inv, M_cifrada))

    mensagem_recuperada = ""
    for i in range(M_recuperada.shape[1]):
        idx = np.argmax(M_recuperada[:,i])
        mensagem_recuperada += alfabeto[idx]

    return mensagem_recuperada

if __name__ == "__main__":
    mensagem = "batatinha quando nasce espalha rama pelo chão "
    
    P, Q = gerar_matrizes_de_permutacao(27)
    
    mensagem_cifrada = encriptar_enigma(mensagem, P, Q)
    print("Mensagem Cifrada:", mensagem_cifrada)
    
    mensagem_recuperada = decriptar_enigma(mensagem_cifrada, P, Q)
    print("Mensagem Recuperada:", mensagem_recuperada)
