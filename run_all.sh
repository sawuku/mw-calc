#!/usr/bin/env bash
# Run mw.py on every data/*.txt file and write results/summary.tsv
set -euo pipefail

mkdir -p results
out="results/summary.tsv"

> "$out"

for f in data/*.txt; do
    while read -r name formula; do
        # TODO 2: skip blank lines and lines starting with #
        # TODO 3: run mw.py on $formula and save the result
    mw=$(python3 mw.py "$formula")
    echo "$formula -> $mw"
        # TODO 4: append name, formula, and mw to the output file
        :
    done < "$f"
done

echo "Done: wrote $out"
