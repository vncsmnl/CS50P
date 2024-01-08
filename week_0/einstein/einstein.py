def calculate_energy(mass, speed_of_light=300000000):
    try:
        mass = int(mass)
        energy = mass * speed_of_light ** 2
        return energy
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid numerical mass.")

try:
    user_mass = input("Enter mass (in kg): ")
    energy_result = calculate_energy(user_mass)
    print("Energy (E):", energy_result, "Joules")
except Exception as e:
    print("An error occurred:", str(e))
