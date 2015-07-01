#include "ctools.h"

int main(void) {
    ctobssim sim;
    sim["inmodel"].filename("${CTOOLS}/share/models/crab.xml")
    sim["outevents"].filename("events.fits")
    sim["caldb"].string("prod2")
    sim["irf"].string("South_50h")
    sim["ra"].real(83.63)
    sim["dec"].real(22.01)
    sim["rad"].real(5.0)
    sim["tmin"].real(0.0)
    sim["tmax"].real(1800.0)
    sim["emin"].real(0.1)
    sim["emax"].real(100.0)
    sim.execute()
    
    GObservations& obs = sim.obs()
    obs.print()
}
