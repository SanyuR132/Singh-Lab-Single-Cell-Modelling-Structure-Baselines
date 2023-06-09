#!/bin/bash
#SBATCH -J zinbwave_pbmc
#SBATCH -N 1
#SBATCH -c 1
#SBATCH -p gpu --gres=gpu:1
#SBATCH -t 10:00:00
#SBATCH --mem=30G
#SBATCH -o res_pbmc.out
#SBATCH -e err_pbmc.out
#SBATCH --mail-type=END,FAIL,TIME_LIMIT,BEGIN
#SBATCH --mail-user=sanyu_rajakumar@brown.edu
module load R/4.1.0
module load gcc/10.2 pcre2/10.35 intel/2020.2 texlive/2018
Rscript /users/srajakum/scratch/Structure_VAE_scRNA_Simulator/Models/ZINBWaVE/FullRun.R -ttp 0 --study PBMC 
