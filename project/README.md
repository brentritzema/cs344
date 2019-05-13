# Comparing tf-idf Weight Use Across Embedding Models for Stance Classification

The system is a grid-searcher of deep neural networks that takes raw twitter data, processes it, vectorizes it, and then learns the stance of the user based on it. So, in these tweets, a user would either be for, against, or neutral on some topic. The system will specifically process data from Australian mining companies.

This project specifically focuses on the vectorization step of the process. I compare character n-gram term frequency, word-based (the following are all word-based) term frequency-inverse document frequency, term frequency-inverse document frequency in combination with Word2vec, just Word2Vec, term frequency-inverse document frequency in combination with fastText, and just fastText. 

Files
final_project.py (The main code to actually test performance of various systems)
best_network.py (This is a small python script to calculate some statistics for a 25x run)
grid_search_25x_run.sh (A shell script to run the system 25 times, outputting the results to the run_results folder. THIS WILL OVERWRITE OLD RESULTS)
grid_search_single_run.script (A SLURM script to run this on Borg)
grid_search_single_run.sh (A shell script to run the system once)
results_ft.csv (Results of a single run using just fastText)
results_ft_tfidf.csv (Results of a single run using fastText and tfidf)
results_w2v.csv (Results of a single run using Word2vec)
results_w2v_tfidf.csv (Results of a single run using Word2vec and tfidf)
run_results/ (Folder to store the results of a 25x run, will contain 25 different results)


Steps to run:
0.   Make sure you have access to Borg, and the folder /storage/sloclassifiers/ on Borg (contact kvlinden for access)
1.   Log into borg and clone the repository to get these files.
1.   To do a single run: bash grid_search_single_run.sh final_project.py
2.   To do 25 runs: bash gris_search_25x_run.sh final_project.py
3.   Check the status of your job using squeue
4.   Check results by opening the results_(current date).csv when it finishes.
