#!/bin/bash
#Usage: bash grid_search_25x_run.sh path/to/python_nn_script
#Example with project in home folder: bash grid_search_25x_run.sh ~/slo-classifiers/stance/keras-nn/basic.py

python_script_path="${1}"

for i in {1..25}
do
  sbatch grid_search_single_run.script \
	/storage/sloclassifiers/keras-2.1.4-py3-tf-gpu.simg \
	${python_script_path} \
	/storage/sloclassifiers/data/stance/coding/autotrainset_20100101-20180706_${i}_tok.csv \
	run_results/result_${i}.csv
done
