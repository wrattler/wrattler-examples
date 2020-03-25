# wrattler-examples

![Build status](https://api.travis-ci.org/wrattler/wrattler-examples.svg?branch=feature/consolidate-docker)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wrattler/wrattler-examples/master?urlpath=lab)

Easy-to-setup local deployment of the Wrattler notebook, using pre-built docker images pulled from dockerhub, or cloud deployment on binder.

## Local setup

To run locally, the various components of Wrattler run in a *Docker* container.  To install Docker, follow the instructions [here](https://www.docker.com/products/docker-desktop).

To build and run:
```
./wrattler-start
```
And you should be able to:
* Access the Wrattler client directly by pointing your browswer to ```localhost:8080```, or
* Access Wrattler via Jupyter lab by going to ```localhost:8888/?token=<token>``` where the ```<token>``` can be found in the console output from the ```wrattler-start``` command.

Using Jupyter lab enables you to load files with a ```.wrattler``` extension in Wrattler, and save changes.
The local directory ```resources/``` is mounted on the docker container so you can save files in Jupyterlab and have this reflected in your local filesystem.

In addition to notebook files, you can put python or R files containing e.g. function definitions or import statements here, and use them in your notebooks with either
```%local <filename>``` (will import contents of <filename> to the current cell) or ```%global <filename>``` (will import contents of <filename> to all cells of that language).

This directory can also be used to load data into the language services - e.g. if you put ```myData.csv``` into ```resources/```, you can load it into a pandas dataframe with ```df = pd.read_csv("resources/myData.csv")```.

Once you have finished, you can stop the docker container by doing Ctrl+C, then pressing `y` to confirm you want to stop the jupyter lab instance.


## Cloud setup

Click the "binder" button at the top of the page :)
