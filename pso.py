import random

def sphere(x):
    return sum([i**2 for i in x])

# Define the PSO algorithm
def pso(objective_func, bounds, num_particles, num_iterations):
    dimensions = len(bounds)
    global_best_pos = [0] * dimensions
    global_best_val = float("inf")

    # Initialize the particles
    particles = []
    for i in range(num_particles):
        particle = {}
        particle["position"] = [random.uniform(bounds[j][0], bounds[j][1]) for j in range(dimensions)]
        particle["velocity"] = [0] * dimensions
        particle["best_position"] = particle["position"][:]
        particle["best_value"] = float("inf")
        particles.append(particle)

    # PSO loop
    for i in range(num_iterations):
        for particle in particles:
            # Evaluate the objective function
            value = objective_func(particle["position"])

            # Update the particle's best position and value
            if value < particle["best_value"]:
                particle["best_position"] = particle["position"][:]
                particle["best_value"] = value

            # Update the global best position and value
            if value < global_best_val:
                global_best_pos = particle["position"][:]
                global_best_val = value

            # Update the particle's velocity
            for j in range(dimensions):
                r1 = random.random()
                r2 = random.random()
                particle["velocity"][j] = (
                    particle["velocity"][j] * 0.5
                    + 2 * r1 * (particle["best_position"][j] - particle["position"][j])
                    + 2 * r2 * (global_best_pos[j] - particle["position"][j])
                )

            # Update the particle's position
            for j in range(dimensions):
                particle["position"][j] += particle["velocity"][j]

    return global_best_pos, global_best_val

# Drive
bounds = [(-100, 100)] * 10 # 10-dimensional problem
result = pso(sphere, bounds, num_particles=30, num_iterations=100)
print("Best position: ", result[0])
print("Best value: ", result[1])
