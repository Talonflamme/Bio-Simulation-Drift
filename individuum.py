import numpy as np

from allel import Allel


class Individiuum:
    def __init__(self, allel1: Allel, allel2: Allel):
        self.allel1 = allel1
        self.allel2 = allel2

    def is_heterozygot(self):
        return self.allel1 != self.allel2

    def is_homozygot(self):
        return self.allel1 == self.allel2

    def __eq__(self, other):
        if not isinstance(other, Individiuum):
            return False

        if self.allel1 == other.allel1 and self.allel2 == other.allel2:
            return True

        # order of allel does not matter
        if self.allel1 == other.allel2 and self.allel2 == other.allel1:
            return True

        return False

    def reproduction_with(self, other: 'Individiuum', mutation_rate: float) -> 'Individiuum':
        male = np.random.choice([self.allel1, self.allel2])
        female = np.random.choice([other.allel1, other.allel2])

        male.create_mutation(mutation_rate)
        female.create_mutation(mutation_rate)

        return Individiuum(male, female)
