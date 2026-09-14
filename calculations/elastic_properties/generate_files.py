import numpy as np
from ase.io import read, write
import os

# Load the fully relaxed base structure (ibrav=4)
base_structure = read('scf.in', format='espresso-in')

# Define strain values: -2% to +2% in 0.5% steps
strains = np.linspace(-0.02, 0.02, 9)

# Create output directories
os.makedirs('uniaxial', exist_ok=True)
os.makedirs('biaxial', exist_ok=True)

# Define QE calculation parameters
input_data = {
    'calculation': 'scf',
    'prefix': 'crsi2n4',
    'outdir': './tmp/',
    'pseudo_dir': '../../../pseudo/ONCVPSP/sg15',
    'verbosity': 'high',
    'ecutwfc': 80,
    'ecutrho': 400,
    'assume_isolated': '2D',
    'occupations': 'fixed',
    'nosym': True,
    'noinv': True,
    'conv_thr': 1.0e-10,
    'mixing_beta': 0.4
}

pseudopotentials = {
    'Cr': 'Cr_ONCV_PBE_sr.upf',
    'Si': 'Si_ONCV_PBE_sr.upf',
    'N': 'N_ONCV_PBE_sr.upf'
}

kpts = (11, 11, 1)

for e in strains:
    # --- Uniaxial Strain (x-direction) ---
    uni_structure = base_structure.copy()
    cell_uni = uni_structure.get_cell()
    
    # Stretches ONLY the x-components of all lattice vectors
    def_matrix_uni = np.array([[1 + e, 0, 0],
                               [0, 1, 0],
                               [0, 0, 1]])
    
    uni_structure.set_cell(cell_uni @ def_matrix_uni, scale_atoms=True)
    
    # ASE will automatically write this as ibrav=0 with CELL_PARAMETERS
    write(f'uniaxial/crsi2n4_uni_{e:.3f}.in', uni_structure, format='espresso-in',
          input_data=input_data, pseudopotentials=pseudopotentials, kpts=kpts)

    # --- Biaxial Strain (xy-direction) ---
    bi_structure = base_structure.copy()
    cell_bi = bi_structure.get_cell()
    
    # Stretches x and y components equally, preserving hexagonal symmetry
    def_matrix_bi = np.array([[1 + e, 0, 0],
                              [0, 1 + e, 0],
                              [0, 0, 1]])
    
    bi_structure.set_cell(cell_bi @ def_matrix_bi, scale_atoms=True)
    
    write(f'biaxial/crsi2n4_bi_{e:.3f}.in', bi_structure, format='espresso-in',
          input_data=input_data, pseudopotentials=pseudopotentials, kpts=kpts)

print("Strain files generated successfully in /uniaxial and /biaxial directories.")
