#include <iostream>
#include "GammaLib.hpp"

int main(void) {
  // HESS 2006 publication Crab spectrum (2006A&A...457..899A)
  GEnergy e0(1, "TeV");
  double diff_flux = 3.45e-17; // cm^-2 sec^-1 MeV^-1
  double spectral_index = -2.63;
  GModelSpectralPlaw power_law(diff_flux, spectral_index, e0);

  // Compute integral flux in 1 to 10 TeV energy band
  GEnergy emin(1, "TeV");
  GEnergy emax(10, "TeV");
  double int_flux = power_law.flux(emin, emax);
  std::cout << int_flux << std::endl; // cm^-2 sec^-1
}
