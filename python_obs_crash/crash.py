import ctools

def simulate_data():
    sim = ctools.ctobssim()
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

    obs = sim.obs()
    return obs

obs = simulate_data()
# sim has gone out of scope and deletes the data on desctruction
# leaving a Python obs object with a dangling pointer to a
# C++ GObservations object

# Accessing a method like obs.__str__ which will call 
# _wrap_GBase___str__(_object*, _object*)
# can crash because the GObservations object is gone or at least
# in an invalid state (sometimes something is printed, corresponding
# to an empty object)
print(obs)
# import IPython; IPython.embed()
