#!/bin/bash

################################################# INFO ##############################################################
#
# This script is for running <<Ring>> in parallel (many runs at the same time) with a FIFO approach semaphore system, 
# with N processes running at the same time and processes being taken as soon as possible to save time
#
# The script can easily be adapted to run any command line program in parallel
#
#
# Author: Marcia A. Hasenahuer
# email: marcia.hasenahuer@gmail.com
#
############################################# DEPENDENCIES ##########################################################
#
#  1. Ring3 - Request download and follow installation instructions:  https://biocomputingup.it/downloads
#  2. Make Ring3 executable from everywhere in your Linux system, by adding it to your PATH variable, 
#     i.e. add this line in your ~/.bashrc file:
#      
#        export PATH=$PATH:</path/to/bin/folder/of/Ring3>
#     And source your .bashrc to acknowledge the change:
#        source ~/.bashrc
#
############################################# HOW TO RUN THIS SCRIPT ################################################
#
#   STEPS:
#   1. Put your PDB/mmCIF structures in tue "input" folder
#   2. Then run:
#    
#   ./runRingParallel.sh [n] [pdblist]
#   
#   n: number of processes to run in parallel
#   pdblist: the path to a file with the list of the full path to your PDB/mmCIF files (one by-line) 
#
#   Example:
#  ./runRingParallel.sh 4 pdblist
#
#
############################################ OUTPUT #################################################################
#
#   An "output" folder will be created in the actual directory where you are running Ring3. 
#   Inside there, for each input PDB/mmCIF you'll find :
#   *_ringNodes: the nodes of your PDB/mmCIF
#   *_ringEdges: the edges (interactions) identified for your PDB/mmCIF structure
#   *.log: a lof file with the log output from Ring3 for each run
#
############################################# CODE ###################################################################


# Capturing the number of processes to run
N=$1

# Reading in your pdblist file
readarray -t pdblist < $2

#DEBUG
#echo ${pdblist[*]}

# If it doesn't exist, create the output directory where the resulting files will be saved
mkdir -p output


# initialize a semaphore with a given number of tokens
open_sem(){
    mkfifo pipe-$$
    exec 3<>pipe-$$
    rm pipe-$$
    local i=$1
    for((;i>0;i--)); do
        printf %s 000 >&3
    done
}

# run the given command asynchronously and pop/push tokens
run_with_lock(){
    local x
    # this read waits until there is something to read
    read -u 3 -n 3 x && ((0==x)) || exit $x
    (
     ( "$@"; )
    # push the return code of the command to the semaphore
    printf '%.3d' $? >&3
    )&
}


# Start the semaphore system with the $N processors you specified
open_sem $N

# Lopping through your PDB/mmCIF and running Ring3
# MAKE SURE YOU HAVE ring3 INSTALLED AND SYSTEM-WIDE AVAILABLE 
for pdb in "${pdblist[@]}"; do
    echo  "$pdb ..."
    run_with_lock ring -i "input/$pdb" --out_dir "output/" &>> "output/${pdb}_run_$(date +%Y%m%d).log"
    
    # If Ring3 is not available system-wide, use this line, modify with the path to your installation of Ring
    #run_with_lock /path/to/ring -i $pdb --out_dir "output/" &>> output/${pdb}_run_$(date +%Y%m%d).log
    
done
echo "Done!"



