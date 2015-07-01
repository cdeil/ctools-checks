This is an investigation of the crashes from Python pipelines
that pass the GObservations object around:
https://cta-redmine.irap.omp.eu/issues/1491

Building the C++ code here doesn't work, because ctools can't be (easily)
used as a library, the header files aren't installed.

For now the simplest solution would be to put the C++ program in the
ctools source tree and use the build system there.
