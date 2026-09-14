# Strain engineering

Strain-dependent relaxations, band calculations, and exported structures.

| Directory | Contents |
| --- | --- |
| `relax/` | Relaxation input/output pairs named by strain |
| `bands/` | A reference SCF input and separate band workflows for each strain |
| `structures/` | XYZ structure exports |

The labels below correspond to the in-plane lattice parameters in the
relaxation inputs, relative to `a = 2.844 Å`:

| Label | Applied strain |
| --- | --- |
| `m1`, `m2`, `m3`, `m5` | −1%, −2%, −3%, −5%, respectively |
| `p1`, `p2`, `p3`, `p5` | +1%, +2%, +3%, +5%, respectively |
| `p0` | 0%; only a relaxation input is included |

Keep each strain's SCF, NSCF, band, and band-post-processing files in its own
directory. Their local `./tmp/` paths separate the runtime state by strain
when commands are launched from the corresponding directory.

XYZ exports are available for `m1`, `m2`, `m3`, `m5`, `p1`, `p3`, and `p5`.
The `p2` case has calculation files but no XYZ export.
`bands/m2/input_tmp.in` is an additional input for that case.
