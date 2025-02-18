import numpy as np


class Allel:
    def __init__(self, arg: str | int):
        if isinstance(arg, str):
            self.dna = arg
        else:
            self.dna = "".join(np.random.choice(["a", "t", "g", "c"], size=arg).tolist())

    def __eq__(self, other):
        if isinstance(other, str):
            return self.dna == other

        if not isinstance(other, Allel):
            return False

        return self.dna == other.dna

    def __str__(self):
        return self.dna

    def __repr__(self):
        return f"Allel({self.dna})"

    def __hash__(self):
        return hash(self.dna)

    def create_mutation(self, mutation_rate: float):
        for i in range(len(self.dna)):
            if np.random.random() < mutation_rate:
                new_base = np.random.choice(["a", "t", "g", "c"])
                self.dna = self.dna[:i] + new_base + self.dna[i + 1:]
