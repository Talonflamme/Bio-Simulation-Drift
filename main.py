import numpy as np
import matplotlib.pyplot as plt

from individuum import Individiuum
from simulation import Simulation

np.random.seed(42)


def can_reproduce(individuum: Individiuum):
    return np.random.random() < 0.5


def sim(N):
    total_data = []

    for i in range(20):
        sim = Simulation(pop_size=N, mutation_rate=0.0, allel_length=10, can_reproduce=can_reproduce)

        data = sim.start(100)

        total_data.append(data)

        plt.plot(data, alpha=0.1)

    data = np.array(total_data)
    data = np.average(data, axis=0)

    plot, = plt.plot(data)

    plot.set_label(f"Trend N = {N}")


def main():
    sim(20)

    plt.legend()
    # plt.show()


if __name__ == '__main__':
    # main()
    import cProfile
    cProfile.run("main()")
