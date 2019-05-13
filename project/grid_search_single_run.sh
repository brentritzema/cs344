#!/bin/bash
#Usage: bash grid_search_single_run.sh path/to/python_nn_script

python_script_path="${1}"
timestamp=$(date +%Y-%m-%d_%H-%M-%S)

sbatch grid_search_single_run.script \
	/storage/sloclassifiers/keras-2.1.4-py3-tf-gpu.simg \
	${python_script_path} \
	/storage/sloclassifiers/data/stance/coding/autotrainset_20100101-20180706_1_tok.csv \
	results_${timestamp}.csv
echo ${timestamp}
