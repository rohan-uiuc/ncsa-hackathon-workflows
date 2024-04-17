#!/bin/bash

#SBATCH --job-name=llmslurm    # create a short name for your job
#SBATCH --partition=cpu   
#SBATCH --account=bbug-delta-cpu
#SBATCH --time=00:30:00        # total run time limit (HH:MM:SS)
#SBATCH --nodes=1              # node count
#SBATCH --mem=0
#SBATCH --reservation=hack-cpu-team1    # reservation available starting from 8AM 4/20 and ending 11PM 4/21.

conda activate venv

echo "python path `which python3`"

echo "job is starting on `hostname`"
srun python3 llm.py
