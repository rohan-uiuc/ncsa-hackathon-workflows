## Overview
Some example slurm scripts. Feel free to use these. You will just need to reaplce runnable script (instead of `llm.py`) and conda environment (instead of `venv`), if applicable. <br>

## Compute node reservations for hackathon
- 12 CPU-only compute nodes and 1 GPU node (A100x4) will be reserved for the Hackathon.
- Reservations will start from 8AM 4/20 and will end at 11PM 4/21.
- Hackathon participants can utilize these resources so that your jobs will not be in the common Delta resource queue (meaning faster turn around time) !
- Each team will have 1 entire CPU-only node reserved for them for the duration of the hackathon.
- Single 4 way A100 node is reserved for the hackathon. TPlease be mindful when using this resource as this will be a shared resource for all the participants.


## Usage
- `sinfo` to check the partitions. 
- `sbatch single_node.slrum` to submit batch jobs.
- `srun --account=bbug-delta-cpu python llm.py` to submit interactive jobs.

## Batch job submissions

1. single_node.slurm : Runs in a single node, uses A100 GPU cluster. Uses 4 GPUs per node. Multi-threading allowed.
2. multi_node1.slurm : Multi-node job run. To yser multi-threading, use `cpus-per-task`
3. multi_node2.slurm : Similar to above, but with named env variable exports.
4. multi_node3.slurm : ssh into each node and launch jobs. Each job can be tailored by passing in python arguments to the same runnable script, or passing in different runnable scripts.
5. single_cpu_reservation.slurm : Change the `--reservation` to reflect your team number. Ex: Team1 will have `#SBATCH --reservation=hack-cpu-team1` and Team 12 will have `#SBATCH --reservation=hack-cpu-team12`. Make sure to use your own reservation.
6. single_gpu_reservation : 

## Interactive job submissions
