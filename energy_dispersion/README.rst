Energy dispersion
=================

Description
-----------

This is a first test of energy dispersion in GammaLib / ctools.

1. Simulate a Gaussian spectal line at 10 TeV with intrinsic width of 1 TeV with ``edisp=yes``.
2. Fit the spectral line with ``edisp=no`` (should result in incorrect width > 1 TeV)
3. Fit the spectal line with ``edisp=yes`` (should result in correct width ~ 1 TeV)

To execute this test simply run::

	./make.sh


Results
-------

For GammaLib f5102f9 and ctools 20f257e I obtain the following results
(copied from the log file):

Fit with ``edisp=no``
+++++++++++++++++++++

Normalization ............: 1.00163e-09 +/- 3.1659e-12 [1e-16,1e-06] ph/cm2/s (free,scale=1e-09)
Mean .....................: 1.00047e+07 +/- 3584.42 [100000,1e+09] MeV (free,scale=1e+07)
Sigma ....................: 1.11942e+06 +/- 2479.5 [10000,1e+08] MeV (free,scale=1e+06)


Fit with ``edisp=yes``
++++++++++++++++++++++

Normalization ............: 1.00163e-09 +/- 3.1659e-12 [1e-16,1e-06] ph/cm2/s (free,scale=1e-09)
Mean .....................: 1.00047e+07 +/- 3584.42 [100000,1e+09] MeV (free,scale=1e+07)
Sigma ....................: 1.11942e+06 +/- 2479.5 [10000,1e+08] MeV (free,scale=1e+06)

Conclusion
----------

Currently the ``edisp`` parameter in ``ctlike`` has no effect.
Fit results are not taking energy dispersion into account for ``edisp=yes``.
