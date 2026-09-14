echo "calculating single atom energies"

cat >Si.scf.in <<EOF
&control
    calculation = 'scf',
    prefix = 'Si',
    outdir = '.',
    pseudo_dir = '../../../pseudopot'
/
&system
    ibrav = 0, 
    nat = 1, 
    ntyp = 1,
    ecutwfc = 40.0,
    ecutrho = 200.0,
    constrained_magnetization = "atomic"
    nspin = 2
    starting_magnetization(1) =  1.00000e-01
    occupations = 'smearing',
    smearing = 'gaussian',
    degauss = 0.01,
/
&electrons
    conv_thr         =  1.00000e-08
    mixing_beta      =  4.00000e-01
    startingpot      = "atomic"
    startingwfc      = "atomic+random"
/
ATOMIC_SPECIES
    Si  28.086  Si.pbe-n-rrkjus_psl.1.0.0.UPF
ATOMIC_POSITIONS angstrom
    Si  15.0 15.0 15.0
K_POINTS gamma
CELL_PARAMETERS angstrom
    30.0  0.0  0.0
     0.0 30.0  0.0
     0.0  0.0 30.0
EOF

mpirun -np 4 pw.x <Si.scf.in> Si.scf.out
echo Si.scf.out job Done
echo Starting N.scf.out ...
cat >N.scf.in <<EOF
&control
    calculation = 'scf',
    prefix = 'N',
    outdir = '.',
    pseudo_dir = '../../../pseudopot'
/
&system
    ibrav = 0,
    nat = 1,
    ntyp = 1,
    ecutwfc = 40.0,
    ecutrho = 200.0,
    constrained_magnetization = "atomic"
    nspin                     = 2
    starting_magnetization(1) =  1.00000e-01
    occupations = 'smearing',
    smearing = 'gaussian',
    degauss = 0.01,
/
&electrons
    conv_thr         =  1.00000e-08
    mixing_beta      =  4.00000e-01
    startingpot      = "atomic"
    startingwfc      = "atomic+random"
/
ATOMIC_SPECIES
    N 14.006 N.pbe-rrkjus.UPF
ATOMIC_POSITIONS angstrom
    N  15.0 15.0 15.0
K_POINTS gamma
CELL_PARAMETERS angstrom
    30.0  0.0  0.0
     0.0 30.0  0.0
     0.0  0.0 30.0
EOF

mpirun -np 4 pw.x <N.scf.in> N.scf.out
echo N.scf.out job done!
echo starting Cr.scf.out .....
cat >Cr.scf.in <<EOF
&control
    calculation = 'scf',
    prefix = 'Cr',
    outdir = '.',
    pseudo_dir = '../../../pseudopot'
/
&SYSTEM
    constrained_magnetization = "atomic"
    degauss                   =  1.00000e-02
    ecutrho                   =  200
    ecutwfc                   =  40
    ibrav                     = 0
    nat                       = 1
    nspin                     = 2
    ntyp                      = 1
    occupations               = "smearing"
    smearing                  = "gaussian"
    starting_magnetization(1) =  1.00000e-01
/

&ELECTRONS
    conv_thr         =  1.00000e-08
    mixing_beta      =  4.00000e-01
    startingpot      = "atomic"
    startingwfc      = "atomic+random"
/

K_POINTS {gamma}

CELL_PARAMETERS {angstrom}
 30.000000   0.000000   0.000000
  0.000000  30.000000   0.000000
  0.000000   0.000000  30.000000

ATOMIC_SPECIES
Cr     51.99610  Cr.pbe-sp-van.UPF

ATOMIC_POSITIONS {angstrom}
Cr     15.000000  15.000000  15.000000
EOF

mpirun -np 4 pw.x <Cr.scf.in> Cr.scf.out
echo all jobs Done!
