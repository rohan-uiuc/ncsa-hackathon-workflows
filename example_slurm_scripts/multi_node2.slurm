#!/bin/bash

#SBATCH --job-name=llmslurm
#SBATCH --partition=gpuA40x4
#SBATCH --account=bbug-delta-gpu
#SBATCH --time=02:00:00
#SBATCH --nodes=8
#SBATCH --ntasks=8
#SBATCH --gpus-per-node=2
#SBATCH --mem=0

module load anaconda
export PROJECT_BASE_DIR=$HOME/LLM
export DATA=${PROJECT_BASE_DIR}/datasets/test-data

conda activate venv

python llm.py

