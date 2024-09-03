import numpy as np
from typing import Tuple

ALFABETO = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 áéíóúàèìòùâêîôûãõçÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ.,;:!?()[]{}<>\"'\\/@#&*+-=%_"

def gerar_matrizes_de_permutacao(N: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gera duas matrizes de permutação de tamanho N x N.
    """
    P = np.eye(N)
    np.random.shuffle(P)

    Q = np.eye(N)
    np.random.shuffle(Q)
    
    return P, Q

def encriptar_enigma(mensagem: str, P: np.ndarray, Q: np.ndarray) -> str:
    """
    Encripta a mensagem usando duas matrizes de permutação, com aleatoriedade
    para evitar padrões perceptíveis.
    """
    N = len(ALFABETO)
    mensagem = mensagem.lower()
    mensagem_filtrada = ''.join([letra for letra in mensagem if letra in ALFABETO])

    M = np.zeros((N, len(mensagem_filtrada)))
    for i, letra in enumerate(mensagem_filtrada):
        idx = ALFABETO.index(letra)
        M[idx, i] = 1

    M_cifrada = np.dot(Q, np.dot(P, M))

    # Introduzir aleatoriedade, mas garantir reversibilidade
    mensagem_cifrada = ""
    for i in range(M_cifrada.shape[1]):
        col = M_cifrada[:, i]
        max_idx = np.argmax(col)
        shift = (i + max_idx) % N  # Deslocamento dependente da posição
        mensagem_cifrada += ALFABETO[shift]
    
    return mensagem_cifrada

def decriptar_enigma(mensagem_encriptada: str, P: np.ndarray, Q: np.ndarray) -> str:
    """
    Decripta a mensagem usando as inversas das matrizes de permutação.
    """
    N = len(ALFABETO)
    M_cifrada = np.zeros((N, len(mensagem_encriptada)))
    for i, letra in enumerate(mensagem_encriptada):
        shift = ALFABETO.index(letra)
        original_idx = (shift - i) % N  # Reverter o deslocamento
        M_cifrada[original_idx, i] = 1
    
    P_inv = np.linalg.inv(P)
    Q_inv = np.linalg.inv(Q)
    M_recuperada = np.dot(P_inv, np.dot(Q_inv, M_cifrada))

    mensagem_recuperada = ""
    for i in range(M_recuperada.shape[1]):
        idx = np.argmax(M_recuperada[:, i])
        mensagem_recuperada += ALFABETO[idx]

    return mensagem_recuperada