"""Example: make an image of a shell model with Gammalib"""
import gammalib

# Create a SNR shell model
center = gammalib.GSkyDir()
center.radec_deg(0.3, 0.1)
model = gammalib.GModelSpatialRadialShell(center, 0.5, 0.1)

# Make an empty sky map
# (cartesian projection, celestial coordinates)
ra, dec, binsz, npix = 0, 0, 0.01, 300
image = gammalib.GSkymap("CAR", "CEL", ra, dec,
                         -binsz, binsz, npix, npix, 1)

# Fill the sky map with the model image
energy = gammalib.GEnergy()
time   = gammalib.GTime()
for pix in range(image.npix()):
    dir = image.pix2dir(pix)
    theta = center.dist(dir)
    image[pix] = model.eval(theta, energy, time)

# Save the image to a FITS file
image.save('shell.fits')
