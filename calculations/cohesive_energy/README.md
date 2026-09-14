# Cohesive energy

| File or directory | Role |
| --- | --- |
| `scf.in`, `scf.out` | CrSi₂N₄ monolayer calculation |
| `cohesive_energy.xlsx` | Original energy-analysis workbook |
| `single_atom/Cr.scf.*`, `single_atom/Si.scf.*`, `single_atom/N.scf.*` | Atomic-reference inputs and outputs |
| `single_atom/run.sh` | Launch the three atomic inputs |
| `single_atom/new_run.sh` | Regenerate and launch atomic inputs |

The atomic directory also retains a phosphorus input, `P.scf.in`, and a
separate `scf.in`/`scf.out` pair for a seven-atom system. These additional files
are preserved records; they are not three more isolated-atom references for
CrSi₂N₄.

The atomic and monolayer inputs reference different pseudopotential families
and calculation settings. Check that the selected energies use consistent
references before reusing them for a cohesive-energy calculation. No energies
or workbook values were recomputed during repository organization.
