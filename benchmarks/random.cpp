#include <boost/progress.hpp>
#include <random>
#include <GammaLib.hpp>

using namespace boost;

void cpp_random(int size) {
	std::cout << "cpp" << std::endl;
	// http://en.cppreference.com/w/cpp/numeric/random
   std::minstd_rand rng;
  std::poisson_distribution<> distribution(2.0);
  progress_timer timer;
  double s = 0;
  for(int ii = 0; ii < size; ++ii) {
   		s += distribution(rng);
	}

  std::cout << s << std::endl;
}


void gammalib_random(int size) {
	std::cout << "gammalib" << std::endl;
	GRan rng;
  progress_timer timer;
	double s = 0;
	for (int ii=0; ii < size; ++ii) {
	  s += rng.poisson(2.0);		
	}
	std::cout << s << std::endl;
}


int main (int argc, const char * argv[])
{
	cpp_random(1e7);
	gammalib_random(1e7);
  return 0;
}
