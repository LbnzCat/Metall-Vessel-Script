
# geometric tolerance


tol = 1e-7


# number formatting
def vector_format(vector):
    # output for edge definitions
    return "({:.8f} {:.8f} {:.8f})".format(
        vector[0],
        vector[1],
        vector[2]
    )

# cylinder/frustum creation:
# ratio of radius of internal block vertex of a cylinder/frustum
# to outer radius of that cylinder/frustum

frustum_core_to_outer = 0.64
# frustum_core_to_outer = (e.R/e.r_1)*2**0.5
# the same as above but is used for edge points
frustum_edge_to_outer = 1.1*frustum_core_to_outer/2**0.5
# frustum_edge_to_outer = frustum_core_to_outer/2**0.5


