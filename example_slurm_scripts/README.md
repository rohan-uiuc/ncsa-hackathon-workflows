## Overview
Some example slurm scripts. Feel free to use these. You will just need to reaplce runnable script (instead of `llm.py`) and conda environment (instead of `venv`), if applicable. 

## Usage
`sbatch single_node.slrum`

## Documentation

1. single_node.slurm : Runs in a single node, uses A100 GPU cluster. Uses 4 GPUs per node. Multi-threading allowed.
2. multi_node1.slurm : Multi-node job run. To yser multi-threading, use `cpus-per-task`
3. multi_node2.slurm : Similar to above, but with named env variable exports.
4. multi_node3.slurm : ssh into each node and launch jobs. Each job can be tailored by passing in python arguments.
