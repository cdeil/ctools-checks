PROGRAM=crash
OBJ=crash.cpp
CFLAGS=`pkg-config --cflags gammalib`
LDFLAGS=`pkg-config --libs gammalib`

$(PROGRAM): $(OBJ)
	$(CXX) -o $@ $^ $(CFLAGS) $(LDFLAGS)
