#!/bin/bash

#SBATCH --job-name=llmslurm
#SBATCH --partition=gpuA40x4
#SBATCH --account=bbug-delta-gpu
#SBATCH --time=02:00:00
#SBATCH --nodes=8
#SBATCH --ntasks=8
#SBATCH --gpus-per-node=2
#SBATCH --mem=0

export NUM_GPUS_PER_NODE=1
nodes=$(scontrol show hostnames "$SLURM_JOB_NODELIST")
nodes_array=($nodes)
export MAIN_HOST=${nodes_array[0]}
export WORLD_SIZE=$(($NUM_GPUS_PER_NODE * $SLURM_JOB_NUM_NODES))

conda activate coin
echo "Starting on hostname: $(hostname | cut -c 1-7)"
echo "  JobID:= " $SLURM_JOB_ID
echo "  Nodelist:= " $SLURM_JOB_NODELIST
echo "  Number of nodes:= " $SLURM_JOB_NUM_NODES
echo "  GPUs per node:= " $SLURM_GPUS_ON_NODE
echo "  CPUs per node:= " $SLURM_CPUS_ON_NODE
echo "  NTasks per node:= "  $SLURM_NTASKS_PER_NODE
# SLURM_NPROCS is my "world size", meaning total # of (GPU) devices.
echo "  Slurm NPROCS:= "  $SLURM_NPROCS
echo "World size: $WORLD_SIZE"
localrank=0
for ((node_i = 0; node_i < $SLURM_JOB_NUM_NODES; node_i++)); do
    local_node_hostname=${nodes_array[$node_i]}
    for ((gpu_i = 0; gpu_i < $NUM_GPUS_PER_NODE; gpu_i++)); do
        echo "Starting GPU worker rank $localrank at $local_node_hostname"
	ssh "$local_node_hostname"\
		"conda activate venv"\
		"python llm.py" &
	((localrank=localrank+1))
	sleep 0.1
    done
done
echo "Job completed"
