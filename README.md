# Introduction

Custom Movie Maker is a tool that allows users to assemble a movie using two copies of the movie
as reference. Users first provide the theatrical and director's cut version of a movie, and specify
the times at which various deleted and alternate scenes occur. Then, Custom Movie
Maker presents an interface that allows the user to choose which specific changes from the director's
cut they wish to include. Finally, this custom, tailored movie is exported and provided to the user for
their viewing pleasure.


# Getting started

  - Once per system, please run:

    ```console
    > pip3 install pipenv
    ```
  
  - Once per working copy, please run:

    ```console
    > python3 -m pipenv install --dev
    ```
    
# Initializing files
In a video editor, concatenate the theatrical version and director's cut version of the desired movie. 
Export this file as an MP4 and take note of the time stamp dividing the two different versions.

In 'main.py,' change 'steps' to [1, 0, 0]. 

In the file initialization block, change 'main_file' to the path to the MP4 you exported earlier
and 'timestamp' to the time stamp (hh:mm:ss.XXX) dividing the two different versions of the movie 
in the MP4. Change 'output_directory' to the directory you wish to export your new files to, change 'original_name'
to the name you would like to call the file containing the theatrical version of the movie, and
change 'special_name' to the name you would like to call the file containing the director's cut
version of the movie. Be sure to include '.mp4' at the end of 'original_name' and 'special_name.'

After you are done changing these variables, run 'main.py.'

# Cutting files
In 'main.py,' change 'steps' to [0, 1, 0]. 

Change 'original_name' and 'special_name' to the respective paths to the videos you exported
in the 'Initializing files' step. Change 'output_directory' to the directory you wish to export
cuts to.

In 'instructions.yaml,' specify the names and times of deleted/alternate scenes in the director's
cut version of the movie. More detailed instructions are provided in 'instructions.yaml.'

Run 'main.py.'

