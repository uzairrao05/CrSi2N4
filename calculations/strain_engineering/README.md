# Strain engineering

Strain-dependent relaxations, band calculations, and exported structures.

| Directory | Contents |
| --- | --- |
| `relax/` | Relaxation input/output pairs named by strain |
| `bands/` | A reference SCF input and separate band workflows for each strain |
| `structures/` | Original XYZ structure exports |

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

The XYZ exports are incomplete as a set: a `p2.xyz` file is not supplied.
Existing exports are preserved without inferring or generating missing
structures. The additional `input_tmp.in` in `bands/m2/` is also retained.
