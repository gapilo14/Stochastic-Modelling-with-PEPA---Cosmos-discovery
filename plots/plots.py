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

def interpolate(k_values, p_values):
    # Create interpolation function for "Throughput: p"
    interp_func_p = interp1d(k_values, p_values, kind='cubic')

    # Generate finer k values for a smoother curve
    k_fine_p = np.linspace(min(k_values), max(k_values), 500)
    p_fine_p = interp_func_p(k_fine_p)
    return k_fine_p, p_fine_p

# # Example usage for "Throughput: p" CSV
# file_path_p = '../PEPA/PEPA/k-propose.csv'
# k_values, p_values = parse_csv_to_arrays(file_path_p)

# # Create interpolation function for "Throughput: p"
# k_fine_p, p_fine_p = interpolate(k_values, p_values)

# # Plot and save for "Throughput: p"
# plt.figure(figsize=(10, 6))
# plt.plot(k_fine_p, p_fine_p, '-', label="Network Throughput", color="orange")
# plt.title("Throughput vs Coefficient k (propose)")
# plt.xlabel("Coefficient k")
# plt.ylabel("Network Throughput [blocks/s]")
# plt.legend()
# plt.grid()
# plt.savefig("k_p.png")
# # plt.show()

# # Example usage for "Throughput: pv" CSV
# file_path_pv = '../PEPA/PEPA/k-prevote.csv'
# k_values_pv, pv_values = parse_csv_to_arrays(file_path_pv)

# # Create interpolation function for "Throughput: pv"
# k_fine_pv, p_fine_pv = interpolate(k_values_pv, pv_values)

# # Plot and save for "Throughput: pv"
# plt.figure(figsize=(10, 6))
# plt.plot(k_fine_pv, p_fine_pv, '-', label="Network Throughput", color="red")
# plt.title("Throughput vs Coefficient k (prevote)")
# plt.xlabel("Coefficient k")
# plt.ylabel("Network Throughput [blocks/s]")
# plt.legend()
# plt.grid()
# plt.savefig("k_pv.png")
# # plt.show()

# # Example usage for "Throughput: pv" CSV
# file_path_pv = '../PEPA/PEPA/k-propose-prevote.csv'
# k_values_pv, pv_values = parse_csv_to_arrays(file_path_pv)

# # Create interpolation function for "Throughput: pv"
# k_fine_pv, p_fine_pv = interpolate(k_values_pv, pv_values)

# # Plot and save for "Throughput: pv"
# plt.figure(figsize=(10, 6))
# plt.plot(k_fine_pv, p_fine_pv, '-', label="Network Throughput", color="red")
# plt.title("Throughput vs Coefficient k (prevote)")
# plt.xlabel("Coefficient k")
# plt.ylabel("Network Throughput [blocks/s]")
# plt.legend()
# plt.grid()
# plt.savefig("k_pv_p.png")
# # plt.show()

# Example usage for "Throughput: pv" CSV
file_path_pv = '../PEPA/PEPA/g.csv'
k_values_pv, pv_values = parse_csv_to_arrays(file_path_pv)

# Create interpolation function for "Throughput: pv"
k_fine_pv, p_fine_pv = interpolate(k_values_pv, pv_values)

# Plot and save for "Throughput: pv"
plt.figure(figsize=(10, 6))
plt.plot(k_fine_pv, p_fine_pv, '-', label="Network Throughput", color="blue")
plt.title("Throughput vs Coefficient g")
plt.xlabel("Coefficient g")
plt.ylabel("Network Throughput [blocks/s]")
plt.legend()
plt.grid()
plt.savefig("g.png")
# plt.show()

# Example usage for "Throughput: pv" CSV
file_path_pv = './csv/non-homogeneous-prevote.csv'
k_values_pv, pv_values = parse_csv_to_arrays(file_path_pv)

# Create interpolation function for "Throughput: pv"
k_fine_pv, p_fine_pv = interpolate(k_values_pv, pv_values)

# Plot and save for "Throughput: pv"
plt.figure(figsize=(10, 6))
plt.plot(k_fine_pv, p_fine_pv, '-', label="Multi-Round >= 2", color="red")
plt.axvline(x=1, color="blue", linestyle="--")
plt.title("Prevote time for non-homogeneous proposers")
plt.xlabel("Coefficient k")
plt.ylabel("Network Throughput [blocks/s]")
# plt.ylim(0, 1.0)
plt.legend()
plt.grid()
plt.savefig("non-homogeneous-k.png")
# plt.show()
