#!/bin/bash

#SBATCH --job-name=llmslurm    # create a short name for your job
#SBATCH --partition=gpuA100x8   
#SBATCH --account=bbug-delta-gpu
#SBATCH --time=00:30:00        # total run time limit (HH:MM:SS)
#SBATCH --output=llmout.log    # optionally specify output file. If not will be written to slurm-jobid.out
#SBATCH --error=llmerr.log     # optionally specify stderr file. If not will be written to slurm-jobid.out
#SBATCH --nodes=1              # node count
#SBATCH --gpus-per-node=4
#SBATCH --mem=100g
#SBATCH --cpus-per-task=32     # cpu-cores per task (>1 if multi-threaded tasks)
conda activate venv

echo "python path `which python3`"

echo "job is starting on `hostname`"
srun python3 llm.py

# (optionaly) keep node alive for full amount of $TIME
sleep infinity
