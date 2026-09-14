# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
# Use Matplotlib defaults; the original external sci.mplstyle is not included.

# Number of phonon modes and q-points from gr.freq
nbnd = 21; nks = 91

# Open gr.freq.gp file
qs, *ph = np.loadtxt('crsi2n4.freq.gp', unpack=True)

# Read phonon at each phonon index
ph0 = []
for iq in range(nks):
    ph0.append([])
    for ib in range(nbnd):
        tmp = ph[ib][iq]
        ph0[iq].append(float(tmp))
    
# Set high-symmetry points from matdyn.in
G1 = qs[0]; K = qs[40]; M = qs[60]; G2 = qs[90]

# Create figure object
plt.figure()

# Plot dotted lines at high-symmetry points
plt.axvline(K, c='gray')
plt.axvline(M, c='gray')
# Plot the phonon dispersion
plt.plot(qs, ph0, c='b')

# Add the x and y-axis labels
plt.xlabel('')
plt.ylabel('Frequency (cm$^{-1}$)')

plt.xlim(G1, G2)
plt.ylim(-50, 1700)

# Add labels for high-symmetry points
plt.xticks([G1, K, M, G2], [r'$\Gamma$', 'K', 'M', r'$\Gamma$'])
# Hide x-axis minor ticks
plt.tick_params(axis='x', which='minor', bottom=False, top=False)

# Save the figure 
plt.savefig('plot-phonon.pdf')
# Show the plot
plt.show()
