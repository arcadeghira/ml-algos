import numpy as np
from kernelMatrix import *


def regularizedKernLSTrain(Xtr, Ytr, kernel, sigma, lam):
    '''Arguments:
    Xtr: training input
    Ytr: training output
    kernel: type of kernel ('linear', 'polynomial', 'gaussian')
    lam: regularization parameter

    Returns:
    c: model weights

    Example of usage:
    c =  regularizedKernLSTrain.regularizedKernLSTrain(Xtr, Ytr, 'gaussian', 1, 1E-1);'''
    n = Xtr.shape[0]
    K = kernelMatrix(Xtr, Xtr, sigma, kernel)
    c = np.dot(np.linalg.pinv(K + lam * n * np.identity(n)), Ytr)

    return c
