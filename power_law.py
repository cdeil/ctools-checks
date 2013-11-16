# Filename: power_law.py
from gammalib import GEnergy, GModelSpectralPlaw



# HESS 2006 publication Crab spectrum (2006A&A...457..899A)
e0 = GEnergy(1, 'TeV')
diff_flux = 3.45e-17 # cm^-2 sec^-1 MeV^-1
spectral_index = -2.63
power_law = GModelSpectralPlaw(diff_flux, spectral_index, e0)

# Compute integral flux in 1 to 10 TeV energy band
emin = GEnergy(1, 'TeV')
emax = GEnergy(10, 'TeV')
int_flux = power_law.flux(emin, emax)
print(int_flux) # cm^-2 sec^-1
