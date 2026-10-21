"""Print the GC percentage for each non-empty FASTA record."""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fasta_path", help="path to the FASTA file")
    parser.add_argument(
        "--min-gc",
        type=float,
        help="print only records with GC percentage above this threshold",
    )
    args = parser.parse_args()

    header = None
    sequence = []

    def report_record():
        bases = "".join(sequence).upper()
        if not bases:
            print(f"Warning: empty sequence for {header!r}; skipping", file=sys.stderr)
            return
        gc_percentage = (bases.count("G") + bases.count("C")) / len(bases) * 100
        if args.min_gc is None or gc_percentage > args.min_gc:
            print(f">{header}\t{gc_percentage:.4f}%")

    with open(args.fasta_path) as fasta_file:
        for line in fasta_file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    report_record()
                header = line[1:]
                sequence = []
            elif header is None:
                parser.error("sequence data must follow a FASTA header")
            else:
                sequence.append("".join(line.split()))

    if header is not None:
        report_record()


if __name__ == "__main__":
    main()
