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
In **instructions.yaml**, specify the names and times of deleted/alternate scenes in the director's
cut version of the movie. Here is a template for formatting these times:

**EXAMPLE 1: single scene**
````
- start: start timestamp
  end: end timestamp
````
**EXAMPLE 2: deleted scene**
````
- alternatives:
    - name: name of deleted scene
    - from: original
      start: none
      end: none
    - from: special
      start: start timestamp in director's cut edition
      end: end timestamp in director's cut edition
````
**EXAMPLE 3: alternate scene**
````
- alternatives:
    - name: name of alternate scene*
    - from: original
      start: start timestamp in theatrical edition
      end: end timestamp in theatrical edition
    - from: special
      start: start timestamp in director's cut edition
      end: end timestamp in director's cut edition
````

Timestamps are written as hh:mm:ss.XXX. If a scene continues from an earlier cut, 
*continue* can be written instead of the prior timestamp

After completing **instructions.yaml**, run **cut.py**.

In the first window, find the file containing the theatrical version of the desired movie.
You can go within folders by double clicking. Once you have found the file, click it once, then
click *Choose File*.

In the second window, find the file containing the director's cut version of the movie 
Once you have found the file, click it once, then click *Choose File*.

The cutting process will now begin. This may take some time. Depending on the size of the files and
the number of deleted/alternate scenes, it could take upwards of an hour. Do not move onto the next
step until this process is complete.

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

