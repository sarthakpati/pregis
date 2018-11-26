import numpy as np
import time
import gc

def pca_GPU(test_img, mean_brain, Beta, BetaT, _gamma, correction, verbose):
    import algo as algo
    t_begin = time.clock()
    l,m,n = test_img.shape
    D = test_img - mean_brain
    
    L_tmp, T, alpha = algo.decompose(D, Beta, BetaT, _gamma, verbose)
    for i in range(correction):
        sum_alpha_beta = np.dot(Beta, alpha)
        D_prime = D + L_tmp - sum_alpha_beta.reshape(l,m,n)
        L_tmp, T, alpha = algo.decompose(D_prime, Beta, BetaT , _gamma, verbose)

    gc.collect()
    t_end = time.clock()
    t_elapsed = t_end - t_begin
    print 'Decomposition takes: %f seconds' %t_elapsed

    L = D  - T + mean_brain
    return (L, T, alpha)

def pca_CPU(test_img, mean_brain, atlas_map, Beta, _lambda, _gamma, correction, verbose):
    import algo_cpu as algo
    t_begin = time.clock()
    l,m,n = test_img.shape
    D = test_img - mean_brain
    inb = np.where(atlas_map == 2)
    outb = np.where(atlas_map == 0)
    b = np.where(atlas_map == 1)
    _Lambda = _lambda * np.ones(atlas_map.shape, dtype=atlas_map.dtype)
    _Lambda[inb] = 10
    _Lambda[outb] = 0.001

    _Gamma = _gamma*np.ones(atlas_map.shape, dtype=atlas_map.dtype)
    _Gamma[outb] = 10
    _Gamma[b] = 10
    L_tmp, S, T, alpha = algo.decompose(D, Beta, _Lambda, _Gamma, _lambda, _gamma, verbose)
    for i in range(correction):
        AlphaBeta = np.dot(Beta, alpha).reshape(l,m,n)
        D_prime = np.array(D, copy=True)
        D_prime[inb] = D_prime[inb] + L_tmp[inb] - AlphaBeta[inb]
        L_tmp, S, T, alpha = algo.decompose(D_prime, Beta ,_Lambda, _Gamma, _lambda, _gamma, verbose)

    gc.collect()
    t_end = time.clock()
    t_elapsed = t_end - t_begin
    print 'Decomposition takes: %f seconds' %t_elapsed

    L = D - S - T + mean_brain
    return (L, S, T, alpha)

  
