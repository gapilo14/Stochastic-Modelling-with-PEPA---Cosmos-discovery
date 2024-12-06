import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def parse_csv_to_arrays(file_path):
    """Parses a CSV file with two columns: Rate and Throughput."""
    rates = []
    throughputs = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            rates.append(float(row[0]))
            throughputs.append(float(row[1]))
    return np.array(rates), np.array(throughputs)

# Example usage for "Throughput: p" CSV
file_path_p = '../PEPA/PEPA/k-propose.csv'
k_values, p_values = parse_csv_to_arrays(file_path_p)

# Create interpolation function for "Throughput: p"
interp_func_p = interp1d(k_values, p_values, kind='cubic')

# Generate finer k values for a smoother curve
k_fine_p = np.linspace(min(k_values), max(k_values), 500)
p_fine_p = interp_func_p(k_fine_p)

# Plot and save for "Throughput: p"
plt.figure(figsize=(10, 6))
plt.plot(k_fine_p, p_fine_p, '-', label="Throughput", color="orange")
plt.title("Throughput vs Coefficient k (propose)")
plt.xlabel("Coefficient k")
plt.ylabel("Throughput p")
plt.legend()
plt.grid()
plt.savefig("throughput_p.png")
# plt.show()

# Example usage for "Throughput: pv" CSV
file_path_pv = '../PEPA/PEPA/k-prevote.csv'
k_values_pv, pv_values = parse_csv_to_arrays(file_path_pv)

# Create interpolation function for "Throughput: pv"
interp_func_pv = interp1d(k_values_pv, pv_values, kind='cubic')

# Generate finer k values for a smoother curve
k_fine_pv = np.linspace(min(k_values_pv), max(k_values_pv), 500)
p_fine_pv = interp_func_pv(k_fine_pv)

# Plot and save for "Throughput: pv"
plt.figure(figsize=(10, 6))
plt.plot(k_fine_pv, p_fine_pv, '-', label="Throughput", color="red")
plt.title("Throughput vs Coefficient k (prevote)")
plt.xlabel("Coefficient k")
plt.ylabel("Throughput pv")
plt.legend()
plt.grid()
plt.savefig("throughput_pv.png")
# plt.show()

# Example usage for "Throughput: pv" CSV
file_path_pv = '../PEPA/PEPA/g-propose-prevote.csv'
k_values_pv, pv_values = parse_csv_to_arrays(file_path_pv)

# Create interpolation function for "Throughput: pv"
interp_func_pv = interp1d(k_values_pv, pv_values, kind='cubic')

# Generate finer k values for a smoother curve
k_fine_pv = np.linspace(min(k_values_pv), max(k_values_pv), 500)
p_fine_pv = interp_func_pv(k_fine_pv)

# Plot and save for "Throughput: pv"
plt.figure(figsize=(10, 6))
plt.plot(k_fine_pv, p_fine_pv, '-', label="Throughput", color="blue")
plt.title("Throughput vs Coefficient g (prevote, propose)")
plt.xlabel("Coefficient g")
plt.ylabel("Throughput pv, p")
plt.legend()
plt.grid()
plt.savefig("throughput_g_pv_p.png")
# plt.show()
