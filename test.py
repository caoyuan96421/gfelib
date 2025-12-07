import gfelib
import gdsfactory as gf
import gfelib.datatypes.release_spec as gdr
import numpy as np

c = gf.Component()

release = gdr.ReleaseSpec(hole_radius=3, distance=6, layer=1, angle_resolution=1)

circ = gfelib.basic.circle(
    radius=100, geometry_layer=0, angle_resolution=1, release_spec=release
)

rect = gfelib.basic.rectangle(
    (100, 200), geometry_layer=0, centered=False, release_spec=release
)

ring = gfelib.basic.ring_span(
    radius=80,
    width=150,
    span=(60, 90),
    geometry_layer=0,
    release_spec=release,
    angle_resolution=1,
)

beam = gfelib.flexure.beam(
    length=200,
    width=4,
    thick_length=0,
    thick_width=20,
    geometry_layer=0,
    release_spec=release,
)
butt = gfelib.flexure.butterfly(
    radius_inner=100,
    radius_outer=1000,
    angles=(5, 70),
    width_beam=4,
    width_inner=50,
    thick_length=700,
    thick_offset=0,
    thick_width=20,
    release_inner=False,
    geometry_layer=0,
    angle_resolution=1,
    release_spec=release,
)

# poly = ((0, 0), (200, 200), (0, 800), (-400, 400))
poly = ((-400, 400), (-300, 200), (200, 200), (0, 0))
polygon = gfelib.basic.polygon(points=poly, geometry_layer=0, release_spec=release)

(c << circ).move((500, 500))
(c << rect).move((100, 100))
(c << ring).move((-100, 200))
(c << beam).move((-300, 0))
c << butt
(c << polygon)
c.show()
