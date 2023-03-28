import subprocess
import time

EXE_PATH = "/home/lquivron/Documents/Year_3/Swarm_Intelligence/Swarm_Intelligence_TP_Python/TP3/PSO_C__"
TOPOLOGIES = ["gbest", "ring", "wheel"]
NB_RUN = 20
NB_ITERATIONS = 50
NB_PARTICULES = [5,10,20,50]


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

def exercice_4():
    nb_particule = 20
    topology = "wheel"
    inertia_range = [0.1, 0.4, 0.8, 1]
    phi1_range = [0.2, 0.7, 1, 2]
    phi2_range = [0.2, 0.7, 1, 2]
    for inertia in inertia_range:
        for phi1 in phi1_range:
            for phi2 in phi2_range:
                for run in range(NB_RUN):
                    st = f"{EXE_PATH} --rosenbrock" \
                       f" --save_file results/exo_4/intertia_{inertia}_phi1_{phi1}_phi2_{phi2}_run_{run}.csv" \
                       f" --seed {1234 + run}"\
                       f" --iterations {NB_ITERATIONS}"\
                       f" --{topology} "\
                       f" --particles {nb_particule}"\
                        f" --inertia {inertia}" \
                       f" --phi1 {phi1}"\
                       f" --phi2 {phi2}"\
                       f" --n 10"
                    print(st)
                    subprocess.run(st, check=True, shell=True)


if __name__ == '__main__':

    #exercice_2()
    #exercice_3()
    exercice_4()
