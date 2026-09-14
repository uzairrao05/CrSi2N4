# Phonons

SCF and lattice-dynamics records for CrSi₂N₄, with the force constants and
dispersion data used by the plotting script.

| Step | Program | Input | Stored output or data |
| --- | --- | --- | --- |
| Ground state | `pw.x` | `scf.in` | `scf.out` |
| Phonons on a 4 × 4 × 1 q-grid | `ph.x` | `ph.in` | `ph.out` |
| Real-space force constants | `q2r.x` | `q2r.in` | `q2r.out`, `crsi2n4.fc` |
| Dispersion | `matdyn.x` | `matdyn.in` | `matdyn.out`, `crsi2n4.freq*`, `crsi2n4.modes` |

`input_tmp.in` is an additional phonon input. The `crsi2n4.dyn*` files
needed to repeat the `q2r.x` step are not included.

From this directory, plot the stored dispersion with:

```bash
python plot_phonons.py
```

The script reads `crsi2n4.freq.gp`, uses 21 modes and 91 q-points, and writes
`plot-phonon.pdf`. Its symmetry-point indices are specific to this dataset.
The plot uses the default Matplotlib style.
