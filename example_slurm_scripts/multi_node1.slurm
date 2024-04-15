#!/bin/bash

#SBATCH --job-name=llmslurm
#SBATCH --partition=gpuA40x4
#SBATCH --account=bbug-delta-gpu
#SBATCH --time=02:00:00
#SBATCH --nodes=8
#SBATCH --ntasks=8
#SBATCH --gpus-per-node=2
#SBATCH --mem=0

# export local environment variables to the job
#SBATCH --export=ALL

python llm.py

# (optionaly) keep node alive for full amount of $TIME
sleep infinity
