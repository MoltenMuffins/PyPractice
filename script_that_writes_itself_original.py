import glob
import os

# This script that creates a script with the same content as itself but an 
# iterating filename in the same directory

# First we look through the directory with glob to find if there are 
# any existing copies of the script
existing_files = glob.glob('**/script_that_writes_itself_*.py')

# Next we find the directory that the script is run from
# so we can generate the file in the same directory
output_dir = os.path.dirname(os.path.abspath(__file__))

# We write to a file named 'script_that_writes_itself_*'
# where * is the number of copies of this script found
# by glob. This script is saved in output_dir
with open('{}/script_that_writes_itself_{}.py'.format(
    output_dir, len(existing_files)), 'w+') as f:

    # We read this __file__ as 'o' and write each line in the script
    # to the script copy 'f'
    with open(__file__,'r') as o:
        for line in o:
            f.write(line)