import numpy as np
import glob
import re
import matplotlib.pyplot as plt

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
A0 = (a**2) * np.sin(np.pi / 3) 

# 3. Polynomial Fit (2nd order)
fit_uni = np.polyfit(strains_uni, energies_uni, 2)
fit_bi = np.polyfit(strains_bi, energies_bi, 2)

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

# Output text results
print(f"--- 2D Elastic Constants for CrSi2N4 ---")
print(f"C11 = {C11:.2f} N/m")
print(f"C12 = {C12:.2f} N/m")
print(f"--- Mechanical Properties ---")
print(f"2D Young's Modulus (Y) = {Y_2D:.2f} N/m")
print(f"2D Poisson's Ratio (v) = {v_2D:.4f}")
print(f"2D Shear Modulus (G)   = {G_2D:.2f} N/m")

# ---------------------------------------------------------
# 6. Plotting the Strain Energy Fit (300 DPI)
# ---------------------------------------------------------

# Calculate Delta E (Strain Energy relative to equilibrium E0)
E0_uni = np.polyval(fit_uni, 0)
E0_bi = np.polyval(fit_bi, 0)

delta_E_uni = energies_uni - E0_uni
delta_E_bi = energies_bi - E0_bi

# Generate smooth curves for the fit lines
strains_smooth = np.linspace(min(strains_uni), max(strains_uni), 100)
fit_curve_uni = np.polyval(fit_uni, strains_smooth) - E0_uni
fit_curve_bi = np.polyval(fit_bi, strains_smooth) - E0_bi

# Create Figure
plt.figure(figsize=(8, 6))

# Plot Uniaxial
plt.plot(strains_uni, delta_E_uni, 'bo', markersize=8, label='Uniaxial Data')
plt.plot(strains_smooth, fit_curve_uni, 'b-', linewidth=2, label='Uniaxial Fit')

# Plot Biaxial
plt.plot(strains_bi, delta_E_bi, 'ro', markersize=8, label='Biaxial Data')
plt.plot(strains_smooth, fit_curve_bi, 'r-', linewidth=2, label='Biaxial Fit')

# Formatting for Publication
plt.xlabel(r'Strain ($\epsilon$)', fontsize=14, fontweight='bold')
plt.ylabel(r'Strain Energy $\Delta E$ (eV)', fontsize=14, fontweight='bold')
plt.title(r'Strain Energy vs. Strain for CrSi$_2$N$_4$', fontsize=16, fontweight='bold')
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tick_params(axis='both', which='major', labelsize=12)

# Save the high-resolution plot
plt.tight_layout()
plt.savefig('CrSi2N4_elastic_fit.png', dpi=300, bbox_inches='tight')
print("\nPlot saved successfully as 'CrSi2N4_elastic_fit.png' at 300 DPI.")
