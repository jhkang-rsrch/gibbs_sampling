import os
import pandas as pd
from src.run_ssvs import run_table1 as _run

def run_table1(X, y, seed=0, problem=None, save=True):
    res = _run(X, y, seed=seed)

    if save and problem is not None:
        df = pd.DataFrame(res, columns=["model", "freq", "proportion"])
        os.makedirs("results", exist_ok=True)  # ← os 사용 가능함
        df.to_csv(f"results/table1_problem{problem}.csv", index=False)
        print(f"[Saved] results/table1_problem{problem}.csv")

    return res
