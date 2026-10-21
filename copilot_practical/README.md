# GC Content Calculator

`scripts/gc_content.py` reads a FASTA file containing multiple records,
including sequences split across several lines. It prints each
non-empty record’s header and GC percentage to two decimal places.
Empty sequences produce a warning and are skipped.

Run from the `copilot_practical` directory:

```bash
python3 scripts/gc_content.py input/multi_seq.fasta
```

The optional `--min-gc` argument filters records by GC percentage:

```bash
python3 scripts/gc_content.py input/multi_seq.fasta --min-gc 50
```

Only records strictly above the threshold are reported. For example,
an 80% GC record is excluded when the threshold is 80. Without this
option, all non-empty records are reported.