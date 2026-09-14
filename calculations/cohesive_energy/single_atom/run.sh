#!/bin/bash

# Directory for the output files
OUTDIR="."
PW_EXEC="pw.x"  # Ensure `pw.x` is in your PATH

# List of SCF input files
SCF_FILES=("Si.scf.in" "Cr.scf.in" "N.scf.in")

# Loop through each input file and run the SCF calculation
for FILE in "${SCF_FILES[@]}"; do
    # Extract the element name from the filename
    ELEMENT=$(basename "$FILE" .scf.in)
    
    echo "Running SCF calculation for $ELEMENT..."
    
    $PW_EXEC < "$FILE" > "${ELEMENT}.scf.out"

    if [ $? -eq 0 ]; then
        echo "SCF calculation for $ELEMENT completed successfully."
    else
        echo "Error in SCF calculation for $ELEMENT." >&2
    fi
done

echo "All calculations completed."
