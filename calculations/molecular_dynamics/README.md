# Molecular dynamics

`md.in` contains a Quantum ESPRESSO molecular-dynamics setup for the seven-atom
cell, with a target temperature of 300 K, an Andersen thermostat, `dt = 20.0`,
and `nstep = 11000`.

The input specifies `restart_mode = 'restart'`. The required previous runtime
state is not included. Prepare the appropriate starting state and review the
input before launching a new run.

[collecting_data.txt](collecting_data.txt) contains shell commands for
extracting time and total energy from `md.out`. No `md.out`, trajectory, or
extracted time/energy tables are committed, so this folder documents a setup
without supplying the completed MD results.
