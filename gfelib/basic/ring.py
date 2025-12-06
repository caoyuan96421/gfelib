import gdsfactory as gf

import numpy as np


@gf.cell_with_module_name
def ring(
    radius: float,
    width: float,
    angle: float,
    geometry_layer: gf.typings.LayerSpec,
    angle_resolution: float,
    release_hole_radius: float = 0,
    release_distance: float = 0,
    release_layer: gf.typings.LayerSpec = (0, 0),
) -> gf.Component:
    """Returns a ring with release holes

    Args:
        radius: radius of the ring (midpoint between inner and outer radii)
        width: width of the ring
        angle: angular coverage of the ring (unit: degrees)
        geometry_layer: layer to place polygon
        angle_resolution: number of degrees per point
        release_hole_radius: radius of the release holes, 0 for no release
        release_distance: maximum distance between adjacent release holes, 0 for no release
        release_layer: layer to place release holes
    """
    c = gf.Component()

    _ = c << gf.components.ring(
        radius=radius,
        width=width,
        angle=angle,
        layer=geometry_layer,
        angle_resolution=angle_resolution,
    )

    if release_hole_radius <= 0 or release_distance <= 0:
        return c

    if (
        radius <= release_distance
        or width <= release_distance
        or angle * np.pi / 180 * radius <= release_distance
    ):
        return c

    hole = gf.components.circle(
        radius=release_hole_radius,
        layer=release_layer,
    )

    s = 2 * (release_hole_radius + release_distance) / np.sqrt(2)
    sr = width / (width // s + 1)

    for r in np.arange(radius - 0.5 * width + 0.5 * sr, radius + 0.5 * width, sr):
        steps = angle * np.pi / 180 * r // s + 1
        dt = angle / 180 * np.pi / steps
        t = np.arange(0.5 * dt, angle / 180 * np.pi + dt, dt)
        points = np.stack((r * np.cos(t), r * np.sin(t)), axis=-1)
        for point in points[:-1]:
            ref = c << hole
            ref.move(point)

    return c
