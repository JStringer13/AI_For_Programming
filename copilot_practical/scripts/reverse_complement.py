COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C"}


def read_fasta_sequence(path):
    """Read the sequence from a single-record FASTA file."""
    sequence = []
    found_record = False

    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if found_record:
                    raise ValueError("Expected a single-record FASTA file")
                found_record = True
                continue
            if not found_record:
                raise ValueError("FASTA sequence data must follow a header")
            sequence.append("".join(line.split()))

    return "".join(sequence)


def reverse_complement(seq):
    """Return the DNA reverse complement."""
    try:
        return "".join(COMPLEMENT[base] for base in reversed(seq.upper()))
    except KeyError as error:
        raise ValueError(f"Unsupported DNA base: {error.args[0]}") from error


if __name__ == "__main__":
    import sys

    seq = read_fasta_sequence(sys.argv[1])
    print(reverse_complement(seq))
