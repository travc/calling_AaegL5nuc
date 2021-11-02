#!/usr/bin/env python
import sys
import os

VCFS_DIR = sys.argv[1]

FN = 'regions_list.tsv'
OUTFN = 'regions_list_vcfs.txt'
ZEROPAD = 6

with open(OUTFN,'w') as outfh:
    with open(FN,'r') as fh:
        for i,l in enumerate(fh):
            f = l.strip().split()
            print(f"{VCFS_DIR}/pfilt-{i:06}.{f[0]}:{f[1]}-{f[2]}.vcf.gz", file=outfh)
