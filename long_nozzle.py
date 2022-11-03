from classy_blocks.classes.mesh import Mesh
from classy_blocks.classes.operations import Face
from classy_blocks.classes.shapes import Cylinder, Frustum, RevolvedRing


def get_mesh():
    r0_nozzle = 40e-3
    l0_nozzle = 60e-3

    r0_inlet = 30e-3
    l0_inlet = 300e-3

    r1_nozzle = 105e-3/1.5
    l1_nozzle = 150e-3

    r1_inlet = 60e-3
    l1_inlet = 200e-3/2

    r2_nozzle = 110e-3
    l2_nozzle = 100e-3*2

    l2_inlet = 580e-3*1.5

    n_cells_radial = 7
    n_cells_tangential = 12
    cell_ratio = 4
    outer_cell_size = (2 * r0_nozzle) / (3 * n_cells_radial)
    axial_cell_size = outer_cell_size * cell_ratio

    mesh = Mesh()

    z_start = 0
    z_end = l0_nozzle
    nozzle0 = Frustum([0, 0, z_start], [0, 0, z_end], [r0_nozzle, 0, z_start], r0_inlet)
    nozzle0.chop_axial(start_size=axial_cell_size)
    nozzle0.chop_radial(count=n_cells_radial)
    nozzle0.chop_tangential(count=n_cells_tangential)
    nozzle0.set_bottom_patch('inlet')
    nozzle0.set_outer_patch('wall')
    mesh.add(nozzle0)

    z_start = z_end
    z_end += l0_inlet
    inlet0 = Cylinder([0, 0, z_start], [0, 0, z_end], [r0_inlet, 0, z_start])
    inlet0.chop_axial(start_size=axial_cell_size, end_size=outer_cell_size)
    inlet0.set_outer_patch('wall')

    mesh.add(inlet0)

    z_start = z_end
    z_end += l1_nozzle
    nozzle1_inner = Frustum([0, 0, z_start], [0, 0, z_end], [r0_inlet, 0, z_start], r1_inlet * 0.7)
    nozzle1_inner.chop_axial(length_ratio=0.5, start_size=outer_cell_size, end_size=axial_cell_size)
    nozzle1_inner.chop_axial(length_ratio=0.5, start_size=axial_cell_size, end_size=outer_cell_size)

    mesh.add(nozzle1_inner)

    ring_face = Face([
        [0, r0_inlet, z_start],
        [0, r1_inlet * 0.7, z_end],
        [0, r1_inlet, z_end],
        [0, r1_nozzle, z_start]
    ])

    nozzle1_outer = RevolvedRing([0, 0, z_start], [0, 0, z_end], ring_face)
    nozzle1_outer.chop_radial(count=6)
    nozzle1_outer.set_bottom_patch('wall')
    nozzle1_outer.set_outer_patch('wall')

    mesh.add(nozzle1_outer)

    z_start = z_end
    z_end += l1_inlet
    inlet1 = Cylinder([0, 0, z_start], [0, 0, z_end], [r1_inlet * 0.7, 0, z_start])
    inlet1.chop_axial(start_size=outer_cell_size, end_size=axial_cell_size)
    mesh.add(inlet1)

    ring_face = Face([
        [0, r1_inlet * 0.7, z_start],
        [0, r1_inlet * 0.7, z_end],
        [0, r1_inlet, z_end],
        [0, r1_inlet, z_start]
    ])

    nozzle2_outer = RevolvedRing([0, 0, z_start], [0, 0, z_end], ring_face)
    nozzle2_outer.set_outer_patch('wall')
    mesh.add(nozzle2_outer)

    z_start = z_end
    z_end += l2_nozzle
    nozzle2 = Frustum([0, 0, z_start], [0, 0, z_end], [r1_inlet * 0.7, 0, z_start], r2_nozzle * 0.7)
    nozzle2.chop_axial(start_size=outer_cell_size, end_size=axial_cell_size)
    mesh.add(nozzle2)

    ring_face = Face([
        [0, r1_inlet * 0.7, z_start],
        [0, r2_nozzle * 0.7, z_end],
        [0, r2_nozzle, z_end],
        [0, r1_inlet, z_start]
    ])

    nozzle3_outer = RevolvedRing([0, 0, z_start], [0, 0, z_end], ring_face)
    nozzle3_outer.set_outer_patch('wall')
    mesh.add(nozzle3_outer)

    z_start = z_end
    z_end += l2_inlet
    inlet2 = Cylinder([0, 0, z_start], [0, 0, z_end], [r2_nozzle * 0.7, 0, z_start])
    inlet2.chop_axial(start_size=3 * outer_cell_size, end_size=axial_cell_size)
    inlet2.set_top_patch('outlet')
    mesh.add(inlet2)

    ring_face = Face([
        [0, r2_nozzle * 0.7, z_start],
        [0, r2_nozzle * 0.7, z_end],
        [0, r2_nozzle, z_end],
        [0, r2_nozzle, z_start]
    ])

    nozzle4_outer = RevolvedRing([0, 0, z_start], [0, 0, z_end], ring_face)
    nozzle4_outer.set_outer_patch('wall')
    nozzle4_outer.set_top_patch('outlet')
    mesh.add(nozzle4_outer)

    return mesh
