# Repository guide

## File organization

`calculations/` is organized by physical property. A calculation's input, output,
post-processing data, and local scripts stay together. In particular, the
Wannier90 seed files and the elastic `uniaxial/` and `biaxial/` datasets retain
their internal filenames and relationships.

| File type | Role |
| --- | --- |
| `*.in` | Quantum ESPRESSO inputs |
| `*.out`, `*.wout` | Stored program logs |
| `*.dat`, `*.gnu`, `*.gp`, `*.freq`, `*.fc`, `*.modes` | Numerical results, plotting data, or force constants |
| `*.win`, `*.nnkp`, `*.amn`, `*.mmn`, `*.eig`, `*.chk` | Wannier90 inputs, interface data, or checkpoint |
| `*.py`, `*.sh` | Local analysis, input generation, or launch scripts |
| `*.xyz` | Exported atomic structures |
| `*.xlsx`, `*.txt`, `*.pdf`, `*.png` | Analysis workbooks, exports, notes, and figures |

Use lowercase names with underscores for new directories. Keep the input/output
basename paired, for example `crsi2n4_uni_0.005.in` and
`crsi2n4_uni_0.005.out`. Preserve signs and precision in strain filenames.
Add a short local README when introducing a new study, specifying the system,
method, software version, calculation order, and available results.

## Running new calculations

1. Copy the relevant calculation directory to a fresh directory under `runs/`.
   That directory is excluded from Git so new outputs do not replace the
   archived research records.
2. Obtain the exact pseudopotentials named in `ATOMIC_SPECIES` and set
   `pseudo_dir` in each input. Record their source and checksums with any new
   results. The repository does not include the UPF files.
3. Review `prefix`, `outdir`, and `restart_mode`. Consecutive steps of one
   calculation need the appropriate shared state; independent calculations
   need separate scratch directories. Restart inputs require prior state that
   is not supplied by this archive.
4. Run commands from the directory containing the input. Review the local shell
   scripts before running: they contain fixed MPI process counts and write to
   existing output filenames. `single_atom/new_run.sh` also regenerates inputs,
   and `generate_files.py` replaces the elastic strain inputs in its working
   directory.
5. Check the resulting logs and convergence before copying selected inputs,
   outputs, and analysis back into a documented calculation directory.

The ONCV workflows reference `Cr_ONCV_PBE_sr.upf`, `Si_ONCV_PBE_sr.upf`, and
`N_ONCV_PBE_sr.upf`. The atom directory also contains
`Cr.pbe-sp-van.UPF`, `Si.pbe-n-rrkjus_psl.1.0.0.UPF`, and `N.pbe-rrkjus.UPF`
references, plus a separate phosphorus input. These are distinct reference
setups; a filename or folder name alone does not establish comparability.

Relative `pseudo_dir` paths were rebased during reorganization to preserve their
previous targets with respect to the repository location. Absolute paths retain
the original workstation locations. Both must be reviewed when copying a
workflow or using another computer. The generator and generated inputs may use
different pseudopotential locations; configure the generator before creating
new inputs.

## Stored data and missing runtime state

Scientific logs, matrices, force constants, structure exports, and figures are
tracked. Large existing Wannier90 files remain part of the dataset. Git history
was not rewritten, and no stored result was removed to reduce repository size.

The `.gitignore` excludes local environments and common runtime files while
allowing scientific `.out`, `.dat`, and figure files to be committed. Keep new
wavefunction, scratch, and restart data under `runs/`; archive any restart state
needed for long-term reproduction separately with its provenance.

The MD output/trajectory, phonon dynamical-matrix files consumed by `q2r.x`,
pseudopotentials, and QE save directories are absent. The phonon force constants
and dispersion data are present for analysis. Consult each calculation README
for other limitations of the supplied files.

## Directory migration

| Previous location | Current location |
| --- | --- |
| `Cohesive/` | `calculations/cohesive_energy/` |
| `bands/` (files directly inside) | `calculations/electronic_structure/pbe/` |
| `bands/hse/` | `calculations/electronic_structure/hse/` |
| `md/` | `calculations/molecular_dynamics/` |
| `modulus/` | `calculations/elastic_properties/` |
| `optical/` | `calculations/optical_properties/` |
| `phonon/` | `calculations/phonons/` |
| `strain_engineerig/` | `calculations/strain_engineering/` |
| `strain_engineerig/xyz files/` | `calculations/strain_engineering/structures/` |

Additional filename changes:

| Previous filename | Current filename | Reason |
| --- | --- | --- |
| `plotband.ipynb` | `plot_bands.py` | The file contains Python source, not notebook JSON |
| `phononplot.ipynb` | `plot_phonons.py` | The file contains Python source, not notebook JSON |
| `cohesive energy.xlsx` | `cohesive_energy.xlsx` | Consistent filename without spaces |
| `Tutorial` in the HSE directory | `workflow_notes.txt` | Identify the original plain-text notes |

Numerical outputs, figures, matrices, structures, and workbook contents were
preserved byte for byte. Edits to existing calculation and launch files only
rebase relative pseudopotential paths. The two renamed plotting scripts use
Matplotlib defaults in place of the missing external style file; their data,
energy reference, axes, and other plotting parameters are unchanged. Their
LaTeX tick labels use raw strings to avoid Python escape-sequence warnings.
