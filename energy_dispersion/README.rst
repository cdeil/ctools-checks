Energy dispersion
=================

Infos
-----

This is a first test of energy dispersion in GammaLib / ctools.

1. Simulate a Gaussian spectal line at 10 TeV with intrinsic width of 1 TeV with edisp=yes.
2. Fit the spectral line with edisp=no (should result in incorrect width > 1 TeV)
3. Fit the spectal line with edisp=yes (should result in correct width ~ 1 TeV)

To execute this test simply run::

	./make.sh
