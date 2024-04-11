#! /usr/bin/env python3
"""
Method to find offsets between images
1. Read images from list directory
2. Read fluxscale info from tan_nwgint directory
3. Read WCS info from tan_nwgint directory
4. Use FITSIO (https://github.com/esheldon/fitsio) to read images
5. Use WCS (https://github.com/DarkEnergySurvey/despyastro/blob/master/python/despyastro/wcsutil.py) to transform pixel coordinates between images
6. Subtract images
7. 
"""

import os
import argparse
import re
import time
import fitsio
import wcsutil
import numpy as np


###########################################
def get_data(filename,verbose=0):
    """Function to obtain header, image, mask data
    """

    ifits=fitsio.FITS(filename,'r') # Could be changed to 'rw' as needed
    ih=ifits['SCI'].read_header()
    isci=ifits['SCI'].read()
    imsk=ifits['MSK'].read()
    iwgt=ifits['WGT'].read()
    ifits.close()
    if (verbose > 0):
        print("Successfully read {:s}".format(filename))

    return ih,isci,imsk,iwgt
  

###########################################
def medclip(data,clipsig=5.0,maxiter=10,converge_num=0.0001,verbose=0):
    ct = data.size
    iter = 0; c1 = 1.0 ; c2 = 0.0

    avgval = np.mean(data)
    medval = np.median(data)
    sig = np.std(data)
    wsm = np.where( abs(data-medval) < clipsig*sig )
    if ((verbose > 0)and(verbose < 4)):
        print("iter,avgval,medval,sig")
    if ((verbose > 2)and(verbose < 4)):
        print(0,avgval,medval,sig)
    if (verbose > 3):
        print("iter,avgval,medval,sig,ct,c1,c2")
        print(0,avgval,medval,sig,ct,c1,c2)

    while (c1 >= c2) and (iter < maxiter):
        iter += 1
        lastct = ct
        avgval = np.mean(data[wsm])
        medval = np.median(data[wsm])
        sig = np.std(data[wsm])
        wsm = np.where( abs(data-medval) < clipsig*sig )
        ct = len(wsm[0])
        if ct > 0:
            c1 = abs(ct - lastct)
            c2 = converge_num * lastct
        if ((verbose > 2)and(verbose < 4)):
            print(iter,avgval,medval,sig)
#        print ct,c1,c2
        if (verbose > 3):
            print(iter,avgval,medval,sig,ct,c1,c2)
#   End of while loop
    if (iter >= maxiter):
        print("Warning: medclip had not yet converged after {:d} iterations".format(iter))

    medval = np.median(data[wsm])
    avgval = np.mean(data[wsm])
    stdval = np.std(data[wsm])
    if (verbose > 0):
        print(iter+1,avgval,medval,sig)

    return avgval,medval,stdval,ct


###########################################
def med_diff(ImgDict,iImg,jImg,minpix=500,verbose=0):

    t0=time.time()
    ih,isci,imsk,iwgt=get_data(iImg)
    jh,jsci,jmsk,jwgt=get_data(jImg)
    t1=time.time()
    if (verbose > 2):
        print("Read images: {:.2f} ".format(t1-t0))
#
#
    isci=isci*ImgDict[iImg]['fluxscale']
    jsci=jsci*ImgDict[jImg]['fluxscale']
    t1a=time.time()
    if (verbose > 2):
        print("Scale mages: {:.2f} ".format(t1a-t1))

#    isci2=np.reshape(isci,isci.size)
    iwgt2=np.reshape(iwgt,iwgt.size)
    iwsm=np.where(iwgt2>0.0)

#    jsci2=np.reshape(jsci,jsci.size)
#    jwgt2=np.reshape(jwgt,jwgt.size)
    t2=time.time()
    if (verbose > 2):
        print("Reshape images: {:.2f} ".format(t2-t1a))

#    nSubSample=32
#
##    inx=(ih['NAXIS1']-nSubSample)/nSubSample
##    iny=(ih['NAXIS2']-nSubSample)/nSubSample
##    iImg_ix=np.zeros([iny,inx],dtype=np.float64)
##    iImg_iy=np.zeros([iny,inx],dtype=np.float64)
##    for iy in range(iny):
##        for ix in range(inx):
##            iImg_ix[iy,ix]=(nSubSample/2) + ( ix * nSubSample )
##            iImg_iy[iy,ix]=(nSubSample/2) + ( iy * nSubSample )
#    inx=ih['NAXIS1']
#    iny=ih['NAXIS2']
#    iImg_ix=np.zeros([iny,inx],dtype=np.float64)
#    iImg_iy=np.zeros([iny,inx],dtype=np.float64)
#    for iy in range(iny):
#        for ix in range(inx):
#            iImg_ix[iy,ix]=ix
#            iImg_iy[iy,ix]=iy
##    iImg_ix=np.reshape(iImg_ix,iImg_ix.size)[iwsm]
##    iImg_iy=np.reshape(iImg_iy,iImg_iy.size)[iwsm]
#    iImg_ix=np.reshape(iImg_ix,iImg_ix.size)
#    iImg_iy=np.reshape(iImg_iy,iImg_iy.size)

    iImg_iy, iImg_ix = np.indices(isci.shape)
#   remove points that are masked (have wgt=0)
    iImg_ix=np.reshape(iImg_ix,iImg_ix.size)[iwsm]
    iImg_iy=np.reshape(iImg_iy,iImg_iy.size)[iwsm]
    iImg_rx=iImg_ix.astype('f8')
    iImg_ry=iImg_iy.astype('f8')

    t3=time.time()
    if (verbose > 2):
        print("Form pixel arrays: {:.2f} ".format(t3-t2))

    iRA,iDec=ImgDict[iImg]['wcs'].image2sky(iImg_rx,iImg_ry)
    t4a=time.time()
    if (verbose > 2):
        print("Transform(1) pixel arrays: {:.2f} ".format(t4a-t3))
    jImg_ix,jImg_iy=ImgDict[jImg]['wcs'].sky2image(iRA,iDec)
    t4=time.time()
    if (verbose > 2):
        print("Transform(2) pixel arrays: {:.2f} ".format(t4-t4a))

    jImg_ix=np.rint(jImg_ix).astype(int)
    jImg_iy=np.rint(jImg_iy).astype(int)
#    print(iImg_ix.dtype)
#    print(jImg_ix.dtype)

    jwsm=np.where(np.logical_and(np.logical_and(jImg_ix>0,jImg_ix<jh['NAXIS1']),np.logical_and(jImg_iy>0,jImg_iy<jh['NAXIS2'])))
    t5=time.time()
    if (verbose > 2):
        print("Mask non-overlap: {:.2f} ".format(t5-t4))

    nover=jImg_ix[jwsm].size
    if (verbose > 2):
        print("Preliminary number of overlaping pixels: {:d}".format(nover))

    j_ix=jImg_ix[jwsm]
    j_iy=jImg_iy[jwsm]
    i_ix=iImg_ix[jwsm]
    i_iy=iImg_iy[jwsm]

#    for i in range(0,j_ix.size,57):
#        print(" {:8d}   {:4d} {:4d}   {:4d} {:4d}  {:10.3f} {:10.3f} {:15.7f} ".format(i,i_ix[i],i_iy[i],j_ix[i],j_iy[i],isci[i_iy[i],i_ix[i]],jsci[j_iy[i],j_ix[i]],jwgt[j_iy[i],j_ix[i]]))

    diff=isci[i_iy,i_ix]-jsci[j_iy,j_ix]
    dwgt=jwgt[j_iy,j_ix]
    dwsm=np.where(dwgt>0)

#    print(diff)
#    print(diff[dwsm])

    MedPix=diff[dwsm].size
#    if (MedPix >= minpix):
#        MedDiff=np.median(diff[dwsm])
#        MedStd=np.std(diff[dwsm])
#    else:
#        MedDiff=0.0
#        MedPix=-1
#        MedStd=-1.0
#    t6=time.time()
#    if (verbose > 0):
#        if (MedPix >= minpix):
#            print("Final values (npix,med_diff,med_std,timing): {:8d} {:12.5f} {:12.5f} {:6.2f}".format(MedPix,MedDiff,MedStd,(t6-t0)))

    if (MedPix >= minpix):
        mdiffval=diff[dwsm]
        AvgDiff,MedDiff,MedStd,MedPix=medclip(mdiffval,verbose=0)
    if (MedPix >= minpix):
        if (verbose > 0):
            t6=time.time()
            #print("Final values (npix,med_diff,med_std,timing): {:8d} {:12.5f} {:12.5f} {:6.2f}".format(MedPix,MedDiff,MedStd,(t6-t0)))
    else:    
        MedDiff=0.0
        MedPix=-1
        MedStd=-1.0
    

#    for i in range(iImg_ix[jwsm].size):
#        print(i,iImg_ix[jwsm][i],iImg_iy[jwsm][i],jImg_ix[jwsm][i],jImg_iy[jwsm][i])
#        ra=numpy.reshape(BleedImg[Img]['ra'],BleedImg[Img]['ra'].size)
#        dec=numpy.reshape(BleedImg[Img]['dec'],BleedImg[Img]['ra'].size)
#        x,y=WCSDict[Tile][Img]['wcs'].sky2image(ra,dec)
#        BleedImg[Img]['x']=numpy.reshape(x,numpy.shape(BleedImg[Img]['ra']))
#        BleedImg[Img]['y']=numpy.reshape(y,numpy.shape(BleedImg[Img]['ra']))

    return MedDiff,MedStd,MedPix

 
################################################
def getoff(x,*p):

    print("#################")
    y=np.zeros((x.size),dtype=np.float64)
    nfile=len(p)
    tol=0.001
    for i in range(x.size-1):
        cnt=x[i]
        ifv=1
        ncnt=nfile-1
        ii=0
        jj=0
        while (ii == 0):
            mark=float(ncnt)+tol
            if (cnt <= mark):
                ii=ifv
                jj=int(ifv+round(cnt))
            else:
                ifv=ifv+1
                cnt=cnt-float(ncnt)
                ncnt=ncnt-1
#        print i,x[i],ii,jj,xifl[i],xjfl[i]
        y[i]=p[jj-1]-p[ii-1]

    return y


################################################
def getoff2(x,*p):
#    print("#################")
#    y=np.zeros((x.size),dtype=np.float64)
#    for i in range(x.size):
##        ii=xifl[i]
##        jj=xjfl[i]
#        y[i]=p[xjfl[i]]-p[xifl[i]]
    y=np.array([p[xjfl[i]]-p[xifl[i]] for i in range(x.size)])
    return y

################################################
def getoff3(x,*p):
    print("#################")
    y=p[xjfl]-p[xifl]

    return y


################################################
if __name__ == "__main__":
    # usage `python3 findoff.py -i "list/sci.g.list" -o "findoff_out/test.g.offset_b8" -v 1 --useTAN --fluxscale "list/flx.g.list"`
    t00=time.time()
    parser = argparse.ArgumentParser(description='Code to take offset measurement and find optimal set of per image offsets for the ensemble') 

    parser.add_argument('-i','--input',   action='store', type=str, default=None, required=True,  help='Input image list')
    parser.add_argument('-o','--output',  action='store', type=str, default=None, required=True,  help='Output file of offset measurements')
    parser.add_argument('--fluxscale',    action='store', type=str, default=None, help='Optional set of fluxscales that need to be applied to data')
    parser.add_argument('--magzero',      action='store', type=str, default=None, help='Optional set of ZeroPoints to convert to fluxscales and applied to data')
    parser.add_argument('--magbase',      action='store', type=float, default=30.0, help='MagBase for converting magzero to fluxscale (default=30.0)')
    parser.add_argument('--useTAN',        action='store_true', default=False, required=False, help='Flag to use tan_nwgint variant of input images')

    parser.add_argument('-v','--verbose', action='store', type=int, default=0,    required=False, help='Verbosity (default=0, max=2)')
    parser.add_argument('-b','--boot',    action='store_true', default=False,     required=False, help='Use bootstrap to make an intial guess)')

    args = parser.parse_args()
    if (args.verbose > 0):
        print("Args: {:}".format(args))

    # get information from input image list
    f=open(args.input,'r')

    i=0
    flist=[]  # list of image names
    fdict={}  # dictionary of image names, id, fluxscales, and WCS
    # read image list
    for line in f:
        cols=line.split()
        fname0=cols[0]
        fname=re.sub("coadd_nwgint","tan_nwgint",fname0)  # just to match the filenames in tan_nwgint directory correctly
        fname=re.sub("_nwgint.fits","_nwgint_tan.fits",fname)
        flist.append(fname)
        fdict[fname]={}
        fdict[fname]['inum']=i
        fdict[fname]['fname0']=fname0
        i=i+1
    print("Found {:d} image files".format(len(flist)))
    f.close()

    # read fluxscale info
    if ((args.fluxscale is None)and(args.magzero is None)):
        if (args.verbose > 0): 
            print("No --fluxscale or --magzero.  Assuming all fluxscales are 1.0")
        for fname in fdict:
            fdict[fname]['fluxscale']=1.0
    else:
        if (args.fluxscale is not None):
#            print("RAG: Going the fluxscale route")
            if (os.path.isfile(args.fluxscale)):
                f_flux=open(args.fluxscale,'r')
                useFluxScale=True
        elif (args.magzero is not None):
#            print("RAG: Going the magzero route")
            if (os.path.isfile(args.magzero)):
                f_flux=open(args.magzero,'r')
                useFluxScale=False
        else:
            print("No fluxscale or magzero?  This line should never be able to execute")

        i2=0
        for line in f_flux:
            cols=line.split()
            fname=re.sub("\[0\]","",cols[0])
            if (useFluxScale):
                fscale=float(cols[1])
            else:
                fscale=10.**(0.4*(args.magbase-float(cols[1])))
            if (args.useTAN):
                fname=re.sub("coadd_nwgint","tan_nwgint",fname)  # just to match the filenames correctly
                fname=re.sub("_nwgint.fits","_nwgint_tan.fits",fname)
            if (fname in fdict):
                fdict[fname]['fluxscale']=fscale
                i2=i2+1
            else:
                print("{:s} not found in fdict".format(fname))
        f_flux.close()
        if (useFluxScale):
            print("Found {:d} fluxscale entries made in fdict".format(i2))
        else:
            print("Found {:d} fluxscale entries made in fdict (from --magzero)".format(i2))
        
    i3=0
    for fname in fdict:
        if ('fluxscale' in fdict[fname]):
            i3=i3+1
    print("Found {:d} fluxscale entries in fdict".format(i3))

###############################

    # FITSIO and WCS on images
    file_missing=False
    ts0=time.time()
    for Img in flist:
        if (os.path.isfile(Img)):
            ih,isci,imsk,iwgt=get_data(Img)
            fdict[Img]['header']=ih
            fdict[Img]['crossra0']=ih['CROSSRA0']
            fdict[Img]['ra_cent']=ih['RA_CENT']
            fdict[Img]['dec_cent']=ih['DEC_CENT']
            if (ih['CROSSRA0'] == "Y"):
                fdict[Img]['ra_size']=(360.0-ih['RACMAX'])+ih['RACMIN']
                fdict[Img]['dec_size']=ih['DECCMAX']-ih['DECCMIN']
            else:
                fdict[Img]['ra_size']=ih['RACMAX']-ih['RACMIN']
                fdict[Img]['dec_size']=ih['DECCMAX']-ih['DECCMIN']
            fdict[Img]['wcs']=wcsutil.WCS(ih)
            print("Read WCS for {:s} will be using a fluxscale of {:.5f} ".format(Img,fdict[Img]['fluxscale']))
        else:
            print("File: {:s} not found.".format(Img))
            file_missing=True
    if (file_missing):
        print("Missing file(s).  Aborting!")
        exit(1)
    ts1=time.time()
    print("Timing (acquire WCS): {:.2f}".format(ts1-ts0))

    nimg=len(flist)
    imatch=np.zeros((nimg,nimg),dtype='int16')
    zoff=np.zeros((nimg,nimg),dtype='double')
    for iImg in flist:
        for jImg in flist:
            if (iImg == jImg):
                imatch[fdict[iImg]['inum'],fdict[jImg]['inum']]=0
            else:
                if ((fdict[iImg]['crossra0'] == "Y")or(fdict[jImg]['crossra0'] == "Y")):
                    print("Either {:s} or {:s} or both have CROSSRA0 == Y".format(iImg,jImg))
                    ra1=fdict[iImg]['ra_cent']
                    ra2=fdict[jImg]['ra_cent']
                    if (ra1 > 180.):
                        ra1=ra1-360.0
                    if (ra2 > 180.):
                        ra2=ra2-360.0
                    dra=ra1-ra2
                    printf("Checking that CROSSRA0 case is working")
                    printf("  {:12.7f} --> {:12.7f} for {:s} ".format(fdict[iImg]['ra_cent'],ra1,iImg))
                    printf("  {:12.7f} --> {:12.7f} for {:s} ".format(fdict[jImg]['ra_cent'],ra2,jImg))
                    printf("  {:12.7f}  ".format(dra))
                else:
                    dra=fdict[iImg]['ra_cent']-fdict[jImg]['ra_cent']
                ddec=fdict[iImg]['dec_cent']-fdict[jImg]['dec_cent']
                ra_size=0.5*(fdict[iImg]['ra_size']+fdict[jImg]['ra_size'])
                dec_size=0.5*(fdict[iImg]['dec_size']+fdict[jImg]['dec_size'])
                if (args.verbose > 3):
                    print("dr={:12.7f} dd={:12.7f} rs={:12.7f} ds={:12.7f} ".format(dra,ddec,ra_size,dec_size))                    
                OverLap=False
                OverLapStr="NoOverlap"
                if ((abs(dra) < ra_size)and(abs(ddec) < dec_size)):
                    OverLap=True
                    OverLapStr="  Overlap"
                    imatch[fdict[iImg]['inum'],fdict[jImg]['inum']]=1
                if (args.verbose > 3):
                    print("{ovstr:9s}: {r1:12.7f} {r2:12.7f} {d1:12.7f} {d2:12.7f} ".format(
                        ovstr=OverLapStr,
                        r1=fdict[iImg]['header']['RACMIN'],
                        r2=fdict[iImg]['header']['RACMAX'],
                        d1=fdict[iImg]['header']['DECCMIN'],
                        d2=fdict[iImg]['header']['DECCMAX']))
                    print("     with: {r1:12.7f} {r2:12.7f} {d1:12.7f} {d2:12.7f} ".format(
                        r1=fdict[jImg]['header']['RACMIN'],
                        r2=fdict[jImg]['header']['RACMAX'],
                        d1=fdict[jImg]['header']['DECCMIN'],
                        d2=fdict[jImg]['header']['DECCMAX']))

    print(imatch)
    
    fout=open(args.output,'w')
    for iImg in flist:
        fout.write(" {inum:6d} {fname:s} \n".format(
            inum=fdict[iImg]['inum']+1,
            fname=fdict[iImg]['fname0']))
    fout.write("END OF FILELIST\n")

    count=1
    for iImg in flist:
        for jImg in flist:
            if (fdict[jImg]['inum'] > fdict[iImg]['inum']):
                if (imatch[fdict[iImg]['inum'],fdict[jImg]['inum']] == 1):
                    if (args.verbose > 1):
                        print(iImg,jImg)
                    medoff,medsig,npix=med_diff(fdict,iImg,jImg,minpix=500,verbose=args.verbose)
                    if (npix >= 500):
                        fout.write(" {offval:11.3f} {cval:11.3f} {inum:6d} {jnum:6d} {pixval:10d} {offsig:12.4f} \n".format(
                            offval=medoff,
                            cval=count,
                            inum=fdict[iImg]['inum']+1,
                            jnum=fdict[jImg]['inum']+1,
                            pixval=npix,
                            offsig=medsig))
                count=count+1
    fout.close()    

    print("Total execution time: {:.2f} seconds".format(time.time()-t00))
#
#   Finally finished
#
    exit(0)                    
    