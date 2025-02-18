import numpy as np

from allel import Allel
from individuum import Individiuum


class Simulation:
    def __init__(self, pop_size: int, mutation_rate: float, allel_length: int, can_reproduce):
        """

        :param pop_size: Die konstante Größe der Population.
        :param mutation_rate: Die Wahrscheinlichkeit, dass eine Base bei der Replikation mit einer
         anderen (oder derselben) getauscht wird.
        :param allel_length: Die Anzahl an Basen jedes Allels
        :param can_reproduce: eine Funktion, die als Parameter ein Individuum nimmt und ein bool zurückliefert,
         ob dieses Individuum sich reproduzieren darf.
        """
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.allel_length = allel_length
        self.can_reproduce = can_reproduce

    def start(self, num_rounds: int):
        self.individuen = []
        for i in range(self.pop_size):
            self.individuen.append(Individiuum(Allel(self.allel_length), Allel(self.allel_length)))

        data_points = [self.heterozygotie()]

        for i in range(num_rounds):
            self.next_generation()

            data_points.append(self.heterozygotie())
        return data_points

    def heterozygotie(self):
        self.allele = set()
        for i in self.individuen:
            self.allele.add(i.allel1)
            self.allele.add(i.allel2)
        return len(self.allele) / (2 * self.pop_size)

    def next_generation(self):
        reproduction = [i for i in self.individuen if self.can_reproduce(i)]

        np.random.shuffle(reproduction)

        if len(reproduction) % 2 == 1:
            reproduction.pop(-1)

        for i in range(len(reproduction) // 2):
            a = reproduction[i * 2]
            b = reproduction[i * 2 + 1]
            nachkommen = a.reproduction_with(b, self.mutation_rate)
            self.individuen.append(nachkommen)

        np.random.shuffle(self.individuen)

        self.individuen = self.individuen[:self.pop_size]
