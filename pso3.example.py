import numpy as np

def fitness_function(x):
    return x[0]**2 + x[1]**2

def pso(fitness_function, dimensions, particles, iterations):
    # Her partiklenin pozisyon ve hızını başlat
    pos = np.random.rand(particles, dimensions)
    vel = np.random.rand(particles, dimensions)
    best_pos = np.zeros((particles, dimensions))
    best_score = np.zeros(particles)
    
    for i in range(particles):
        best_pos[i] = pos[i]
        best_score[i] = fitness_function(pos[i])
    
    g_best = best_pos[np.argmin(best_score)]
    
    for t in range(iterations):
        # Her partiklenin hızını ve pozisyonunu güncelle
        for i in range(particles):
            vel[i] = 0.7 * vel[i] + 0.5 * np.random.rand(1) * (best_pos[i] - pos[i]) + 0.5 * np.random.rand(1) * (g_best - pos[i])
            pos[i] = pos[i] + vel[i]
            
            # Her partiklenin en iyi pozisyonunu ve puanını güncelle
            score = fitness_function(pos[i])
            if score < best_score[i]:
                best_pos[i] = pos[i]
                best_score[i] = score
        
        # Global en iyi pozisyonu güncelle
        g_best = best_pos[np.argmin(best_score)]
    
    return g_best

result = pso(fitness_function, 2, 50, 100)
print(result)
