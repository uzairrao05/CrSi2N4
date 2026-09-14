# Elastic properties

Uniaxial and biaxial energy–strain datasets spanning −0.020 to +0.020 in
increments of 0.005. Each series keeps its SCF input/output pairs together;
the `relax/` subdirectories contain separate relaxation records.

| File or directory | Role |
| --- | --- |
| `scf.in` | Base structure used by the input generator |
| `uniaxial/`, `biaxial/` | Strained SCF calculations and local launch scripts |
| `uniaxial/relax/`, `biaxial/relax/` | Stored relaxation inputs and outputs |
| `generate_files.py` | ASE generator for the two strain series |
| `calc_moduli.py` | Fit energies and print elastic properties |
| `plot_calc_moduli.py` | Same fit with an energy–strain figure |
| `CrSi2N4_elastic_fit.png` | Energy–strain figure |

Run analysis from this directory:

```bash
python calc_moduli.py
python plot_calc_moduli.py
```

The existing analysis reads `.out` files directly inside `uniaxial/` and
`biaxial/`; it does not read their `relax/` subdirectories. It takes the first
reported total energy from each file and uses the stored area convention with
`a = 2.844 Å`.

`generate_files.py` reads `scf.in` in the working directory and writes new
inputs into `uniaxial/` and `biaxial/`. Use a fresh copy under `runs/` before
generating or launching calculations to avoid replacing the archived files.
Configure the generator's pseudopotential location before use.
