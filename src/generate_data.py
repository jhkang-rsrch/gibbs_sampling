import numpy as np
import os

def generate_example_4_1(problem=1, seed=0, save=False):
    rng = np.random.default_rng(seed)
    n, p = 60, 5
    X = rng.normal(size=(n, p))

    if problem == 2:
        Z = rng.normal(size=n)
        X[:, 2] = X[:, 2] + 0.15 * Z

    beta_true = np.array([0, 0, 0, 1, 1.2])
    y = X @ beta_true + rng.normal(scale=2.5, size=n)

    if save:
        os.makedirs("data", exist_ok=True)
        np.savez(f"data/example4_1_problem{problem}_seed{seed}.npz", X=X, y=y)
        print(f"[Saved] data/example4_1_problem{problem}_seed{seed}.npz")

    return X, y


def generate_example_4_2(seed=0, save=False):
    rng = np.random.default_rng(seed)
    n, p = 120, 60
    Z = rng.normal(size=n)
    X = rng.normal(size=(n,p)) + Z[:,None]

    beta_true = np.zeros(p)
    beta_true[15:30] = 1
    beta_true[30:45] = 2
    beta_true[45:60] = 3

    y = X @ beta_true + rng.normal(scale=2.0, size=n)

    if save:
        os.makedirs("data", exist_ok=True)
        np.savez(f"data/example4_2_seed{seed}.npz", X=X, y=y)
        print(f"[Saved] data/example4_2_seed{seed}.npz")

    return X, y
