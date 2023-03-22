import subprocess
import time

EXE_PATH = "/home/lquivron/Documents/Year_3/Swarm_Intelligence/TP2/MyImplementation/analysis/aco"
INSTANCES = ["ulysses22", "att532"]
NB_RUN = 20
def run_one_test(exe_path, instance, save_path, nb_run, ants=None):
    for i in range(nb_run):
        subprocess.run(f"{exe_path}"
                       f" --instance {instance}"
                       f" --save_file {save_path}_ants_{ants}_run_{i}.csv"
                       f" --seed {1234+i}"
                       f" --tours 500"
                       f" --ants {ants}"
                       f" --rho 0.5", check=True, shell=True)


def exercice_4_c():
    alphas = [1,0]
    betas = [0,1]
    for i in range(2):
        for instance in INSTANCES:
            for run in range(NB_RUN):
                subprocess.run(f"{EXE_PATH}"
                               f" --instance instances/{instance}.tsp"
                               f" --save_file results/exo_4_c/{instance}_alpha_{alphas[i]}_beta_{betas[i]}_run_{run}.csv"
                               f" --seed {1234 + run}"
                               f" --tours 500"
                               f" --alpha {alphas[i]}"
                               f" --beta {betas[i]}"
                               f" --rho 0.001"
                               f" --ants 10", check=True, shell=True)
def exercice_4_e():
    alpha = 1
    beta = 1
    rhos = [0.01, 0.5, 0.7, 1]
    for rho in rhos:
        for instance in INSTANCES:
            for run in range(NB_RUN):
                subprocess.run(f"{EXE_PATH}"
                               f" --instance instances/{instance}.tsp"
                               f" --save_file results/exo_4_e/{instance}_rho_{rho}_run_{run}.csv"
                               f" --seed {1234 + run}"
                               f" --tours 500"
                               f" --alpha {alpha}"
                               f" --beta {beta}"
                               f" --rho {rho}"
                               f" --ants 10", check=True, shell=True)


def exercice_4_a():
    instance = "instances/att532.tsp"
    save_path = "results/att532"
    nb_run = 20
    ants_ranges = [2, 5, 10, 20, 50, 100]
    for ants in ants_ranges:
        run_one_test(EXE_PATH, instance, save_path, nb_run, ants)


if __name__ == '__main__':

    #exercice_4_c()
    exercice_4_e()
