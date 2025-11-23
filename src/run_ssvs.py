import numpy as np
from collections import Counter
from src.ssvs_core import ssvs_gibbs, ols_with_se

def summarize(gammas, top_k=4):
    cnt = Counter(tuple(g) for g in gammas)
    total = len(gammas)
    out = []
    for gamma, freq in cnt.most_common(top_k):
        model = " ".join(str(i+1) for i, g in enumerate(gamma) if g==1) or "NONE"
        out.append((model, freq, freq/total))
    return out

def run_table1(X, y, seed=0, n_iter=30000, burn_in=5000):
    _, se, _ = ols_with_se(X, y)
    gammas = ssvs_gibbs(y, X, tau=se, c=10, n_iter=n_iter, burn_in=burn_in, random_state=seed)
    return summarize(gammas)
