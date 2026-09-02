class DNA:
    def __init__(self, strand):
        self.strand = strand

    def hamming_distance(self, other):
        strand_length = min(len(self.strand), len(other))
        counter = 0
        for idx in range(strand_length):
            if self.strand[idx] != other[idx]:
                counter += 1
        return counter