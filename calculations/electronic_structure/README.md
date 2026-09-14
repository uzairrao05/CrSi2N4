# Electronic structure

| Directory | Calculation and stored files |
| --- | --- |
| [pbe/](pbe/) | SCF and band-path inputs/outputs, `bands.x` post-processing, band data, Python plot, and PDF |
| [hse/](hse/) | HSE inputs/outputs, `open_grid.x` and `pw2wannier90.x` files, and the `crsi2n4` Wannier90 dataset |

## PBE bands

The input sequence is `scf.in` (`pw.x`), `bands.in` (`pw.x`), then
`bands.pp.in` (`bands.x`). Each uses the same prefix and scratch directory.
To plot the stored results, run from `pbe/`:

```bash
python plot_bands.py
```

The script reads `bands.dat.gnu` and writes `plot-bands.pdf`. Its stored energy
reference is −5.3089 eV, and its high-symmetry indices belong to this dataset.
Review both before applying it to a new calculation.

## HSE and Wannier90

The HSE directory contains `crsi2n4.*` seed files, interpolation results, the
Hamiltonian, and Wigner–Seitz data. The `.win` file specifies 35 bands and
26 Wannier functions. See
[workflow_notes.txt](hse/workflow_notes.txt).

`pw2wann.in` uses `prefix = 'crsi2n4_open'` and requires the state produced
by `open_grid.x`. Include this step when following the workflow notes.
Before running `opengrid.in`, add the terminating `/` to its input namelist.

See the [repository guide](../../docs/repository_guide.md) for dependencies and
scratch-data preparation.
