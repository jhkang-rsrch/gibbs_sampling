import numpy as np
import pandas as pd
from collections import Counter

from src.ssvs_core import ssvs_gibbs, ols_with_se
from src.generate_data import generate_example_4_2

# false choice 정의
def false_choice(gamma):
    bad = []
    bad.extend(list(np.where(gamma[:15] == 1)[0] + 1))      # 1~15 false inclusion
    bad.extend(list(np.where(gamma[15:] == 0)[0] + 16))     # 16~60 false exclusion
    return bad

def run_table2(seed=0, n_iter=30000, burn_in=5000, save=True):
    print("\n=== Running Table 2 (Example 4.2) ===")

    # 데이터 불러오기
    X, y = generate_example_4_2(seed)
    _, se, _ = ols_with_se(X, y)

    settings = [(1,5), (1,10), (10,100), (10,500)]
    rows = []

    for a, c in settings:
        print(f"  Setting (σβ/τ={a}, c={c}) ...")
        tau = se / a
        gammas = ssvs_gibbs(y, X, tau=tau, c=c,
                            n_iter=n_iter, burn_in=burn_in,
                            random_state=seed)

        cnt = Counter(tuple(g) for g in gammas)
        total = len(gammas)

        for gamma, freq in cnt.most_common(5):
            vars_in = " ".join(str(i+1) for i,g in enumerate(gamma) if g==1) or "NONE"
            bad = false_choice(np.array(gamma))

            rows.append({
                "sigma_beta/tau": a,
                "c": c,
                "model": vars_in,
                "freq": freq,
                "proportion": freq/total,
                "false_choice": bad
            })

    df = pd.DataFrame(rows)
    if save:
        df.to_csv("results/table2.csv", index=False)
        print("Saved → results/table2.csv")

    return df

if __name__ == "__main__":
    df = run_table2()
    print(df)
