from PyRay import World, Vector3
from PyRay import objects

world = World(600, 600, resolution=4)
sphere = objects.Sphere(Vector3(0, 0, 20), 10, "red")
sphere_2 = objects.Sphere(Vector3(0, 0, 30), 10, "green")
world.add_object(sphere)
world.add_object(sphere_2)

step = 2

while True:
    world.update()
    sphere.radius -= step
    if sphere.radius <= 0 or sphere.radius >= 20:
        step *= -1
