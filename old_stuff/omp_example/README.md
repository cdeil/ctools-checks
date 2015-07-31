This is a check if the compiler and Gammalib / ctools support OpenMP

http://blog.llvm.org/2015/05/openmp-support_22.html

OpenMP support is now available via clang-3.7 and libomp in Macports:
http://stackoverflow.com/a/31600942/498873

-I/opt/local/include -L/opt/local/lib -fopenmp=libomp

$ clang-mp-3.7 hello_openmp.c -o hello_openmp -I/opt/local/include -L/opt/local/lib -fopenmp=libomp
$ ./hello_openmp 
Hello from thread 3, nthreads 8
Hello from thread 2, nthreads 8
Hello from thread 6, nthreads 8
Hello from thread 4, nthreads 8
Hello from thread 5, nthreads 8
Hello from thread 7, nthreads 8
Hello from thread 1, nthreads 8
Hello from thread 0, nthreads 8


I tried building Gammalib with clang and OMP:

CXX=/opt/local/bin/clang++-mp-3.7 ./configure --enable-openmp
make -j9 check

But there's crashes and errors:
https://gist.github.com/cdeil/8b4c976f696e268affd1#file-gistfile1-txt-L24

I also don't see `-fopenmp=libomp` in the build log.

For now I won't investigate further ... but I should try again at some point.
