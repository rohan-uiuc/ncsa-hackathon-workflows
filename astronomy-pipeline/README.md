# Astronomy pipeline

## Overview
The goal of the process is to remove residual background light from the images (it changes from one image to the next because the images were taken at different times and the scattered light from the atmosphere will depend on things like the amount of clouds, the phase of the moon and how close the telescope might be pointing to it, or how close in time to sunrise/sunset the image was taken).

1. `findoff.py` is comparing the area of overlap between each image and calculating the median difference.
2. `fitoff.py` is taking the differences among all the overlapping images (from findoff) and calculating the best offset value to add/subtract to the pixel values in each image
3. `zoff_apply.py` is taking the values found in fitoff and then applying them to the original images.
4. Output of `zoff_apply` is a FITS file that can be viewed using DS9.
5. Read the documentation within the scripts to see what processes are being done in each.
6. The pipeline : for each band (i,r), run `findoff.py`. using the output from `findoff`, run `fitoff` and using the output from `fitoff`, run `zoff_apply` 

This method is based on paper https://ui.adsabs.harvard.edu/abs/1995ASPC...77..335R/abstract

## Task for the hackathon
- Develop a workflow agent that takes in the input directory, checks if required files are present, creates the code for the pipeline, executes it and prompts user when a result is generated.

## Data
- Download data from shared GDrive https://drive.google.com/drive/folders/1mT5QSrH1sv20HYG2P7HDP9L1-KveDJmX
- List of images in `list` directory. Basically some text files.
- Fluxscale values are in files named `flx`
- Weight values are in files named `wgt`
- Files after SWarp (another process not part of the pipeline) are named `sci`
- FITS images in `tan_nwgint` and `coadd` directory. Use DS9 to view the images
- Data contains images for bands i and r.
- The current scripts can process 5 light bands / colors : g,i,r,Y, and z. 

## Requirements
- Python 3.12+
- pip


## Usage
1. Activate virtual env
2. Install requirements
3. `python3 findoff.py -i "data/list/sci.i.list" -o "out/test.i.offset_b8" -v 1 --useTAN --fluxscale "data/list/flx.i.list"` .  
4. `python3 fitoff.py -i "out/test.i.offset_b8" -o "out/test.i.zoff_b8" -b -v 2`
5. `python3 zoff_apply.py -i "out/test.i.zoff_b8" --fluxscale "data/list/flx.i.list" -o "out/"`

Do not hard code the band (i,r) - all the scripts should run for all bands present in the dataset. The above python command is showing an example of running one input file.

## Useful info
- Astropy.org (https://www.astropy.org/)
- FITS files (https://docs.astropy.org/en/latest/io/fits/index.html)
- Use DS9 to view the FITS files (https://sites.google.com/cfa.harvard.edu/saoimageds9/download)
- SWarp program (https://www.astromatic.net/software/swarp/, https://github.com/astromatic/swarp)
- Coadd (https://wiki.eigenvector.com/index.php?title=Coadd)
- World Coordinate System (https://docs.astropy.org/en/latest/wcs/index.html)

## Acknowledgements
- Robert Gruendl
- Dark Energy Survey https://des.ncsa.illinois.edu/, https://github.com/DarkEnergySurvey/despyastro

