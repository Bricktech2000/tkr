Tinker (alias `tkr`)
====================

A Python program to track ideas, issues and fixes in any project.


Requirements
------------

* Windows or Linux (untested on MacOS)
* Python 3.0 or later


Dependencies
------------

* colorama
    ```
    python -m pip install colorama
    ```


Usage
-----

tkr is a command / program to track ideas, todos, skiped ideas and tasks that are done. It is made from the following four lists: `idea` (in blue), `todo` (in green), `skip` (in yellow) and `done` (in white). Items are created in one of the lists, and can then be moved to any other list as desired.

* Run the program:
    ```
    $ python tkr.py
    > tkr>
    ```
* Create an item in a list: 
    `<list_name> "text to display"`
    ```
    $ todo "add README.md"
    > ot: "add README.md" (in green, 'todo' list)
    ```
* See the items in a list
    `<list_name>s`
    ```
    $ todos
    > ot: "add README.md" (in green, 'todo' list)
    ``` 
* Move an item to a different list:
    `<list_name> <identifier>`
    ```
    $ done ot (note that 'ot' is the identifier, outputted above)
    > ot: "add README.md" (in white, 'done' list)
    $ dones
    > ot: "add README.md" (in white, 'done' list)
    ```
* Select the main list:
    `main <list_name>`
    ```
    $ main ideas
    > (empty)
    ```
* Add another idea...
    ```
    $ idea "awesome idea"
    > gu: "awesome idea" (in blue, 'idea' list)
    ```
* Move an item from the main list to a different list:
    `<list_name>`
    ```
    $ skip (move from 'idea' to 'skip')
    > gu: "awesome idea" (in yellow, 'skip' list)
    $ main skip (select the 'skip' list)
    > (empty)
    $ todo (move from 'skip' to 'todo')
    > gu: "awesome idea" (in yellow, 'todo' list)
    ```
* Exit the Program
    `Ctrl + C`
    ```
    $ ^C
    > (exited the program)
    ```



