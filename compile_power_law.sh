$ pkg-config --cflags gammalib
-I/usr/local/gamma/include/gammalib -I/opt/local/include 
$ pkg-config --libs gammalib
-L/usr/local/gamma/lib -lgamma

$ clang++ power_law.cpp -o power_law `pkg-config --cflags --libs gammalib`
$ ./power_law 
2.06695e-11

$ python power_law.py
2.06694730422e-11