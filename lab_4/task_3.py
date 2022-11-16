def full_mech_energy(mass, height, velocity):

  potential_energy = mass * 9.8 * height
  cin_energy = mass * velocity ** 2 / 2
  return(potential_energy + cin_energy)

print(full_mech_energy(10, 100, 5))
