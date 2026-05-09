#!/bin/bash

# Loop through all .in files in the current directory
for input_file in *.in; do
    
    # Check if any .in files actually exist to prevent a literal "*.in" error
    if [ ! -e "$input_file" ]; then
        echo "No .in files found in the current directory."
        exit 1
    fi

    # Extract the base name of the file (removes the .in extension)
    base_name="${input_file%.in}"
    
    # Define the corresponding output filename
    output_file="${base_name}.out"

    echo "Starting job: $input_file"
    echo "Outputting to: $output_file"

    # --- EXECUTION COMMAND ---
    # Standard serial run:
    # pw.x < "$input_file" > "$output_file"

    # If you are using MPI for parallel execution, comment out the line above 
    # and uncomment/modify the line below with your core count (e.g., -np 4):
    mpirun -np 1 pw.x -in "$input_file" > "$output_file"

    echo "Finished job: $input_file"
    echo "----------------------------------------"

done

echo "All Quantum ESPRESSO jobs have been completed!"
