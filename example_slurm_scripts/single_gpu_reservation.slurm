#!/bin/bash

#SBATCH --job-name=llmslurm    # create a short name for your job
#SBATCH --partition=gpuA100x4 
#SBATCH --account=bbug-delta-gpu
#SBATCH --time=00:30:00        # total run time limit (HH:MM:SS)
#SBATCH --nodes=1              # node count
#SBATCH --mem=0

conda activate venv

echo "python path `which python3`"

echo "job is starting on `hostname`"
srun python3 llm.py
