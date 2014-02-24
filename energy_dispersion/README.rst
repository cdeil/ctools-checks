Energy dispersion
=================

Infos
-----

This is a first test of energy dispersion in GammaLib / ctools.

1. Simulate a Gaussian spectal line at 1 TeV with intrinsic width of 0.1 TeV.
2. Fit the spectral line with edisp=no (should result in incorrect width > 0.1 TeV)
3. Fit the spectal line with edisp=yes (should result in correct width ~ 0.1 TeV)

To execute this test simply run::

	./make.sh
