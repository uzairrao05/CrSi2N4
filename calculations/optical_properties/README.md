# Optical properties

| Files | Contents |
| --- | --- |
| `scf.in`, `scf.out` | Ground-state calculation |
| `nscf.in`, `nscf.out` | NSCF calculation for optical post-processing |
| `epsilon.in`, `epsilon.out` | `epsilon.x` input and log |
| `epsr_crsi2n4.dat`, `epsi_crsi2n4.dat` | Real and imaginary dielectric data |
| `eels_crsi2n4.dat`, `ieps_crsi2n4.dat` | Additional `epsilon.x` numerical outputs |
| `Origin_*.txt` | Exported absorption, corrected dielectric, and optical-constant tables |

The calculation order is SCF → NSCF → `epsilon.x`, using a consistent prefix
and scratch directory. `epsilon.in` defines a 0–15 eV grid with 1,000 points
and 0.10 eV interband broadening.

The Origin tables are preserved exports. Their conversion/correction script is
not included, so the export names alone do not document the processing method.
Retain the raw dielectric data alongside any future processing script.
