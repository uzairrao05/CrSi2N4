import numpy as np
import glob
import re

def extract_energy(filepath):
    """Extracts total energy in Rydberg and converts to eV."""
    with open(filepath, 'r') as f:
        for line in f:
            if '!' in line and 'total energy' in line:
                rydberg_energy = float(re.findall(r"[-+]?\d*\.\d+|\d+", line)[0])
                return rydberg_energy * 13.605698
    return None

def process_directory(directory):
    strains = []
    energies = []
    for filepath in glob.glob(f"{directory}/*.out"):
        strain_str = filepath.split('_')[-1].replace('.out', '')
        strains.append(float(strain_str))
        energies.append(extract_energy(filepath))
    
    sorted_data = sorted(zip(strains, energies))
    return np.array([x[0] for x in sorted_data]), np.array([x[1] for x in sorted_data])

# 1. Parse Output Data
strains_uni, energies_uni = process_directory('uniaxial')
strains_bi, energies_bi = process_directory('biaxial')

# 2. Calculate Equilibrium Area (A0) for the P-6m2 lattice
a = 2.84400 
A0 = (a**2) * np.sin(np.pi / 3) # Area of hexagonal cell base in Angstrom^2

# 3. Polynomial Fit (2nd order: E = a*x^2 + b*x + c)
fit_uni = np.polyfit(strains_uni, energies_uni, 2)
fit_bi = np.polyfit(strains_bi, energies_bi, 2)

# The 'a' coefficient is (1/2) * d^2E/de^2. Therefore, d^2E/de^2 = 2 * a
d2E_uni = 2 * fit_uni[0] 
d2E_bi = 2 * fit_bi[0]

# 4. Calculate C11 and C12 (Conversion: 1 eV/Ang^2 = 16.0217662 N/m)
conv_factor = 16.0217662

C11 = (d2E_uni / A0) * conv_factor
C11_plus_C12 = (d2E_bi / (2 * A0)) * conv_factor
C12 = C11_plus_C12 - C11

# 5. Calculate 2D Mechanical Properties
Y_2D = (C11**2 - C12**2) / C11
v_2D = C12 / C11
G_2D = (C11 - C12) / 2

# Output results
print(f"--- 2D Elastic Constants for CrSi2N4 ---")
print(f"C11 = {C11:.2f} N/m")
print(f"C12 = {C12:.2f} N/m")
print(f"--- Mechanical Properties ---")
print(f"2D Young's Modulus (Y) = {Y_2D:.2f} N/m")
print(f"2D Poisson's Ratio (v) = {v_2D:.4f}")
print(f"2D Shear Modulus (G)   = {G_2D:.2f} N/m")
