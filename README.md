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

# Cutting files
In 'main.py,' change 'step' to 1. 

Change 'original_path' and 'special_path' to the respective paths to the theatrical and director's cut
video files.

In 'instructions.yaml,' specify the names and times of deleted/alternate scenes in the director's
cut version of the movie. More detailed instructions are provided in 'instructions.yaml.'

Run 'main.py.'

# Assembling files
In 'main.py,' change 'step' to 2. 

Run 'main.py.' 

First, you will be presented with a window asking you to select the folder you would like to save your
video to. You can go within folders by double clicking. Once you have found the desired folder,
click it once and select "Choose Folder."

You will next be presented with a window detailing the scenes you specified in 'instructions.yaml.'
Select the scenes you would like to include with the checkboxes. After, enter the name you would like to 
call the file (no '.mp4' necessary). Click 'Assemble'
and you will be provided with an MP4 file of your very own custom movie!

Here is a video that outlines the program as well: https://www.youtube.com/watch?v=qQ8pW1VHkzE

