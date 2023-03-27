import subprocess
import time

EXE_PATH = "/home/lquivron/Documents/Year_3/Swarm_Intelligence/Swarm_Intelligence_TP_Python/TP3/PSO_C__"
TOPOLOGIES = ["gbest", "ring", "wheel"]
NB_RUN = 20
NB_ITERATIONS = 50
NB_PARTICULES = [5,10,20,50]
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
def exercice_2():

    for nb_particule in NB_PARTICULES:
        for run in range(NB_RUN):
            subprocess.run(f"{EXE_PATH}"
                           f" --rastrigin"
                           f" --save_file results/exo_2/rastrigin_nb_particules_{nb_particule}_run_{run}.csv"
                           f" --seed {1234 + run}"
                           f" --iterations {NB_ITERATIONS}"
                           f" --gbest"
                           f" --particles {nb_particule}"
                           f" --phi1 {1.0}"
                           f" --phi2 {1.0}"
                           f" --n 10", check=True, shell=True)
def exercice_3():
    for topology in TOPOLOGIES:
        for nb_particule in NB_PARTICULES:
            for run in range(NB_RUN):
                st = f"{EXE_PATH} --rastrigin" \
                   f" --save_file results/exo_3/topology_{topology}_rastrigin_nb_particules_{nb_particule}_run_{run}.csv" \
                   f" --seed {1234 + run}"\
                   f" --iterations {NB_ITERATIONS}"\
                   f" --{topology} "\
                   f" --particles {nb_particule}"\
                   f" --phi1 {1.0}"\
                   f" --phi2 {1.0}"\
                   f" --n 10"
                print(st)
                subprocess.run(st, check=True, shell=True)


def exercice_4_a():
    instance = "instances/att532.tsp"
    save_path = "results/att532"
    nb_run = 20
    ants_ranges = [2, 5, 10, 20, 50, 100]
    for ants in ants_ranges:
        run_one_test(EXE_PATH, instance, save_path, nb_run, ants)


if __name__ == '__main__':

    #exercice_2()
    exercice_3()
