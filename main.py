from src.table1 import run_table1
from src.table2 import run_table2
from src.generate_data import generate_example_4_1, generate_example_4_2
from src.export_pdf import export_pdf

def run_all():
    print("=== Running Table 1 ===")
    for problem in [1, 2]:
        X, y = generate_example_4_1(problem=problem, seed=0, save=True)
        run_table1(X, y, seed=0, problem=problem, save=True) 

    merge_table1_csv()

    export_pdf("results/table1.csv", "report/table1.pdf", "Table 1: Example 4.1")

    print("\n=== Running Table 2 ===")
    X, y = generate_example_4_2(seed=0, save=True)
    run_table2(seed=0, save=True)
    export_pdf("results/table2.csv", "report/table2.pdf", "Table 2: Example 4.2")


def merge_table1_csv():
    import pandas as pd, glob, os

    files = glob.glob("results/table1_problem*.csv")
    dfs = [pd.read_csv(f) for f in files]
    df_total = pd.concat(dfs, ignore_index=True)

    df_total.to_csv("results/table1.csv", index=False)
    print("[Merged] results/table1.csv created.")


if __name__ == "__main__":
    run_all()
