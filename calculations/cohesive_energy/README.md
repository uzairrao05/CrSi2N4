# Cohesive energy

| File or directory | Role |
| --- | --- |
| `scf.in`, `scf.out` | CrSi₂N₄ monolayer calculation |
| `cohesive_energy.xlsx` | Energy-analysis workbook |
| `single_atom/Cr.scf.*`, `single_atom/Si.scf.*`, `single_atom/N.scf.*` | Atomic-reference inputs and outputs |
| `single_atom/run.sh` | Launch the three atomic inputs |
| `single_atom/new_run.sh` | Regenerate and launch atomic inputs |

The atomic directory also contains a phosphorus input, `P.scf.in`, and a
separate `scf.in`/`scf.out` pair for a seven-atom system. Use the explicitly
named Cr, Si, and N files when selecting isolated-atom references.

The atomic and monolayer inputs reference different pseudopotential families
and calculation settings. Check that the selected energies use consistent
references before using them for a cohesive-energy calculation.
