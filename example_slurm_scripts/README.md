## Overview
Some example slurm scripts. Feel free to use these. <br>
You will just need to reaplce runnable script (instead of `llm.py`) and conda environment (instead of `venv`), if applicable. <br>

## Delta HPC
- Login `ssh username@login.delta.ncsa.illinois.edu`
- Type `accounts` to see accounts you are part of.
- Type `quota` to see your resource limits. Each user has a 50G limit.
- Use `/projects/bbug/<username>` or `/projects/bbug/<project-name>` for all project related stuff. Use `/scratch/bbug/<username>` or `/scratch/bbug/<project-name>` for everything else.
- Hackathon Account name : bbug. Use `bbug-delta-cpu` for CPU nodes and `bbug-delta-gpu` for GPU nodes
- See [Delta - How To?](https://docs.google.com/presentation/d/1mHNwGp0Q5nmYJDCRyYZPT7_THEG9VanX/edit#slide=id.p1) presentation for more info

## Compute node reservations for hackathon
- 12 CPU-only compute nodes and 1 GPU node (A100x4) will be reserved for the Hackathon.
- Reservations will start from 8AM 4/20 and will end at 11PM 4/21.
- Hackathon participants can utilize these resources so that your jobs will not be in the common Delta resource queue (meaning faster turn around time) !
- Each team will have 1 entire CPU-only node reserved for them for the duration of the hackathon.
- Single 4 way A100 node is reserved for the hackathon. Please be mindful when using this resource as this will be a shared resource for all the participants.
- Specifying these reservations for jobs running outside of the set timeperiod will lead to job failure.


## Usage
- `sinfo` to check the partitions. 
- `sbatch single_node.slrum` to submit batch jobs.
- `srun --account=bbug-delta-cpu --cpus-per-task=8 --pty /bin/bash` to submit interactive jobs.
- Once submitted, you will get a response mentioning the compute node name(s) scheduled for the job.

## Batch job submissions

1. single_node.slurm : Runs in a single node, uses A100 GPU cluster. Uses 4 GPUs per node. Multi-threading allowed.
2. multi_node1.slurm : Multi-node job run. To yser multi-threading, use `cpus-per-task`
3. multi_node2.slurm : Similar to above, but with named env variable exports.
4. multi_node3.slurm : ssh into each node and launch jobs. Each job can be tailored by passing in python arguments to the same runnable script, or passing in different runnable scripts.
5. single_cpu_reservation.slurm : Change the `--reservation` to reflect your team number. Ex: Team1 will have `#SBATCH --reservation=hack-cpu-team1` and Team 12 will have `#SBATCH --reservation=hack-cpu-team12`. Make sure to use your own reservation.
6. single_gpu_reservation : As long as the paritition is `A100x4` and account is `bbug-delta-gpu`, your jobs running during the hackathon period (8AM 4/20 to 11PM 4/21) will run in the reserved GPU node. No need to mention reservation explicitly

## Interactive job submissions
Use `srun` for interactive jobs. This means you use specific options with srun on the command line to tell Slurm what resources you need to run your job, such as number of nodes, amount of memory, and amount of time. After typing your srun command and options on the command line and pressing enter, Slurm will find and then allocate the resources you specified. Depending on what you specified, it can take a few minutes for Slurm to allocate those resources. 

### Single node with CPU reservation
- `srun --account=bbug-delta-cpu --partition=cpu --time=00:30:00 --nodes=1 --mem=0 --reservation=hack-cpu-team<num> --cpus-per-task=8 --pty /bin/bash` .
- This will give you shell access to the compute node

### Single node with GPU reservation
- `srun --account=bbug-delta-gpu --partition=A100x4 --time=00:30:00 --nodes=1 --gpus-per-node=1 --mem=0 python test.py`

