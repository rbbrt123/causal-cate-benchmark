import numpy as np

def generate_dataset(n_samples, p_treatment, seed):

    rng = np.random.default_rng(seed)

    X = rng.normal(0, 1, (n_samples, 2))

    T = rng.binomial(1, p_treatment, n_samples)

    mu0 = 2 + X[:,0] + 0.5*X[:,1]
    tau = 1 + 0.8*X[:,0]

    epsilon = rng.normal(0, 1, n_samples)

    Y = mu0 + (tau*T) + epsilon

    return X, T, Y, tau