Energy dispersion
=================

Infos
-----

This is a first test of energy dispersion in GammaLib / ctools.

1. Simulate a Gaussian spectal line at 1 TeV with intrinsic width of 0.1 TeV.
2. Fit the spectral line with edisp=no (should result in incorrect width > 0.1 TeV)
3. Fit the spectal line with edisp=yes (should result in correct width ~ 0.1 TeV)


Commands
--------

ctobssim infile=model.xml outfile=events.fits \
         caldb=$GAMMALIB/share/caldb/cta irf=kb_I_50h_v3 \
         ra=0 dec=0 rad=1 tmin=0 tmax=3600 \
         emin=0.1 emax=100 edisp=no

ctlike infile=events.fits srcmdl=model.xml \
       outmdl=results_edisp_no.xml logfile=results_edisp_no_ctlike.log \
       caldb=$GAMMALIB/share/caldb/cta irf=kb_I_50h_v3
       edisp=no

ctlike infile=events.fits srcmdl=model.xml \
       outmdl=results_edisp_yes.xml logfile=results_edisp_yes_ctlike.log \
       caldb=$GAMMALIB/share/caldb/cta irf=kb_I_50h_v3
       edisp=yes
