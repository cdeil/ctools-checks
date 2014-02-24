MODEL=model.xml
EVENTS=events.fits
CALDB=$GAMMALIB/share/caldb/cta
IRF=kb_I_50h_v3
SEED=42

ctobssim infile=$MODEL outfile=$EVENTS \
         caldb=$CALDB irf=$IRF seed=$SEED \
         ra=0 dec=0 rad=1 tmin=0 tmax=3600 \
         emin=0.1 emax=100 edisp=yes

ctlike infile=$EVENTS srcmdl=$MODEL \
       outmdl=results_edisp_no.xml logfile=results_edisp_no_ctlike.log \
       caldb=$CALDB irf=$IRF
       edisp=no

ctlike infile=$EVENTS srcmdl=$MODEL \
       outmdl=results_edisp_yes.xml logfile=results_edisp_yes_ctlike.log \
       caldb=$CALDB irf=$IRF
       edisp=yes
