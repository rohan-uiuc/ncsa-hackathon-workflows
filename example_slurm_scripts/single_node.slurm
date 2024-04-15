#!/bin/bash

#SBATCH --job-name=llmslurm
#SBATCH --partition=gpuA100x8
#SBATCH --account=bbug-delta-gpu
#SBATCH --time=00:30:00
#SBATCH --output=llmout.log
#SBATCH --error=llmerr.log
#SBATCH --nodes=1
#SBATCH --gpus-per-node=4
#SBATCH --mem=100g
#SBATCH --cpus-per-task=32

conda activate venv

echo "python path `which python3`"

echo "job is starting on `hostname`"
srun python3 llm.py

# (optionaly) keep node alive for full amount of $TIME
sleep infinity
