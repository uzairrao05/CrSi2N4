# Import the necessary packages and modules
import matplotlib.pyplot as plt
# Plot using the default Matplotlib style.
import numpy as np

# The Fermi energy, find it in scf.out
efermi = -5.3089 

# Load data from gr.bands.gnu
data = np.loadtxt('bands.dat.gnu')
k = np.unique(data[:, 0])
bands = np.reshape(data[:, 1], (-1, len(k)))
    
# Set high-symmetry points from nscf.in
gG1 = k[0]; K = k[30]; M = k[50]; gG2 = k[80]

# Create figure object
plt.figure()
# Plot dotted line at Fermi energy
plt.axhline(0, c='gray', ls=':')
# Plot dotted lines at high-symmetry points
plt.axvline(K, c='gray')
plt.axvline(M, c='gray')

# Plot band structure
for band in range(len(bands)):
    plt.plot(k, bands[band, :]-efermi, c='b')

# Add the x and y-axis labels
plt.xlabel('')
plt.ylabel('Energy (eV)')
# Set the axis limits
plt.xlim(gG1, gG2)
plt.ylim (-5, 5)
# Add labels for high-symmetry points
plt.xticks([gG1, K, M, gG2], [r'$\Gamma$', 'K', 'M', r'$\Gamma$'])
# Hide x-axis minor ticks
plt.tick_params(axis='x', which='minor', bottom=False, top=False)
# Save figure to the pdf file
plt.savefig('plot-bands.pdf')
# Show figure
plt.show()
