# Astronomy pipeline

## Overview
Task is to find the offsets between two files.

## Requirements
- Python 3.12+
- pip

## Installation
1. Clone the repository
2. Install the requirements
3. Run the pipeline


## Usage
1. `python3 findoff.py -i "list/sci.g.list" -o "out/test.g.offset_b8" -v 1 --useTAN --fluxscale "list/flx.g.list"`
2. `python3 fitoff.py -i "out/test.g.offset_b8" -o "out/test.g.zoff_b8" -b -v 2`
3. `python3 zoff_apply.py -i "findoff_out/test.g.zoff_b8" --fluxscale "list/flx.g.list" -o "out"`  ( not working as WGT_ME tags are not present in FITS images.)

## Useful info
1. Astropy.org (https://www.astropy.org/)
2. FITS files (https://docs.astropy.org/en/latest/io/fits/index.html)
3. Use DS9 to view the FITS files (https://sites.google.com/cfa.harvard.edu/saoimageds9/download)
4. World Coordinate System (https://docs.astropy.org/en/latest/wcs/index.html)

## Acknowledgements
1. Robert Gruendal
2. Dark Energy Survey https://des.ncsa.illinois.edu/, https://github.com/DarkEnergySurvey/despyastro

