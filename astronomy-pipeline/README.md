# Astronomy pipeline

## Overview
The goal of the process is to remove residual background light from the images (it changes from one image to the next because the images were taken at different times and the scattered light from the atmosphere will depend on things like the amount of clouds, the phase of the moon and how close the telescope might be pointing to it, or how close in time to sunrise/sunset the image was taken).

`findoff.py` is comparing the area of overlap between each image and calculating the median difference.
`fitoff.py` is taking the differences among all the overlapping images (from findoff) and calculating the best offset value to add/subtract to the pixel values in each image
`zoff_apply.py` is taking the values found in fitoff and then applying them to the original images.

This method is based on paper https://ui.adsabs.harvard.edu/abs/1995ASPC...77..335R/abstract

## Data
- List of images in `list` directory. Basically some text files.
- Fluxscale values are in files named `flx`
- Weight values are in files named `wgt`
- Files after swarp are named `sci`
- FITS images in `tan_nwgint` directory. Use DS9 to view the images
- The current scripts process 5 light bands / colors : g,i,r,Y, and z. 

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
3. `python3 zoff_apply.py -i "out/test.g.zoff_b8" --fluxscale "list/flx.g.list" -o "out"`  ( not working as WGT_ME tags are not present in FITS images.)

## Useful info
- Astropy.org (https://www.astropy.org/)
- FITS files (https://docs.astropy.org/en/latest/io/fits/index.html)
- Use DS9 to view the FITS files (https://sites.google.com/cfa.harvard.edu/saoimageds9/download)
- World Coordinate System (https://docs.astropy.org/en/latest/wcs/index.html)

## Acknowledgements
- Robert Gruendal
- Dark Energy Survey https://des.ncsa.illinois.edu/, https://github.com/DarkEnergySurvey/despyastro

