# wrattler-examples

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wrattler/wrattler-examples/data-wrangling-tutorial?urlpath=lab%2Ftree%2Fresources%2FExercise_1.wrattler)

Easy-to-setup local deployment of the Wrattler notebook, using pre-built docker images pulled from dockerhub.

## Local setup

To run locally, the various components of Wrattler run in their own *Docker* containers.  To install Docker, follow the instructions [here](https://www.docker.com/products/docker-desktop).  You also need *docker-compose* which should already be installed with Docker if you are using Windows or OSX.  For Ubuntu, this can be installed following the instructions [here](https://linuxize.com/post/how-to-install-and-use-docker-compose-on-ubuntu-18-04/).

To build and run:
```
docker-compose build
docker-compose up
```
And you should be able to:
* Access the Wrattler client directly by pointing your browswer to ```localhost:8080```, or
* Access Wrattler via Jupyter lab by going to ```localhost:8889/?token=<token>``` where the ```<token>``` can be found in the console output from the ```docker-compose up``` command.

Using Jupyter lab enables you to load files with a ```.wrattler``` extension in Wrattler, and save changes.
The local directory ```resources/``` is mounted on the docker containers for jupyterlab and the language services.

In addition to notebook files, you can put python or R files containing e.g. function definitions or import statements here, and use them in your notebooks with either
```%local <filename>``` (will import contents of <filename> to the current cell) or ```%global <filename>``` (will import contents of <filename> to all cells of that language).

This directory can also be used to load data into the language services - e.g. if you put ```myData.csv``` into ```resources/```, you can load it into a pandas dataframe with ```df = pd.read_csv("resources/myData.csv")```.

Once you have finished, you can stop the docker containers by running (from this directory):
```
docker-compose down
```
