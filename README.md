# CrSi₂N₄: first-principles calculations

Quantum ESPRESSO inputs, calculation logs, numerical data, and analysis scripts
for monolayer CrSi₂N₄. The repository covers electronic structure, lattice
dynamics, optical response, elasticity, cohesive energy, and strain-dependent
properties, with a separate molecular-dynamics input.

## Repository contents

Each calculation directory contains the input files, output logs, numerical
data, and analysis scripts for that property.

| Directory | Contents |
| --- | --- |
| [Electronic structure](calculations/electronic_structure/) | PBE band calculations and HSE/Wannier90 interpolation in separate `pbe/` and `hse/` directories |
| [Phonons](calculations/phonons/) | SCF, phonon, force-constant, and dispersion files; plotting script |
| [Optical properties](calculations/optical_properties/) | SCF/NSCF and dielectric calculations; numerical and Origin exports |
| [Elastic properties](calculations/elastic_properties/) | Uniaxial and biaxial strain series, input generator, and elastic fitting scripts |
| [Cohesive energy](calculations/cohesive_energy/) | Monolayer and atomic-reference calculations; energy workbook |
| [Strain engineering](calculations/strain_engineering/) | Relaxations, band calculations, and structure exports for individual strain values |
| [Molecular dynamics](calculations/molecular_dynamics/) | MD input and extraction notes; no MD output or trajectory is included |
| [Documentation](docs/repository_guide.md) | File conventions, dependencies, and calculation setup |

## Analyze the stored results

Create a Python environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

The elastic fit reads the stored SCF outputs:

```bash
cd calculations/elastic_properties
python calc_moduli.py
```

Run plotting scripts from the directory containing their data:

| Working directory, relative to the repository root | Command | Output |
| --- | --- | --- |
| `calculations/electronic_structure/pbe/` | `python plot_bands.py` | `plot-bands.pdf` |
| `calculations/phonons/` | `python plot_phonons.py` | `plot-phonon.pdf` |
| `calculations/elastic_properties/` | `python plot_calc_moduli.py` | `CrSi2N4_elastic_fit.png` |

Plotting overwrites the named figure in the current directory. To retain an
archived figure, run the script in a copy of its calculation directory under
`runs/`. Set `MPLBACKEND=Agg` when running without a graphical display. The band
and phonon scripts use the default Matplotlib style.

## Calculation environment

The stored Quantum ESPRESSO logs report versions **7.3.1** and **7.4.1**; the
Wannier90 log reports **3.1.0**. Python analysis uses NumPy and Matplotlib, and
the elastic-input generator additionally uses ASE. `requirements.txt` lists
these dependencies without fixed version constraints.

Pseudopotentials and Quantum ESPRESSO scratch/restart directories are not
included. Pseudopotential filenames are specified in each input. Before a new
calculation, configure `pseudo_dir`, check `outdir` and
`restart_mode`, and read the relevant calculation README and
[repository guide](docs/repository_guide.md#running-new-calculations).

The checked-in outputs are research records. Settings differ between studies;
each input and its associated output define that calculation's setup.
