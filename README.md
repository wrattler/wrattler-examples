# wrattler-examples
Easy-to-setup local deployment of the Wrattler notebook, using pre-built docker images pulled from dockerhub. 

## Local setup

To run locally, the various components of Wrattler run in their own *Docker* containers.  To install Docker, follow the instructions [here](https://www.docker.com/products/docker-desktop).  You also need *docker-compose* which should already be installed with Docker if you are using Windows or OSX.  For Ubuntu, this can be installed following the instructions [here](https://linuxize.com/post/how-to-install-and-use-docker-compose-on-ubuntu-18-04/).

To build and run:
```
docker-compose build
docker-compose up
```
And you should be able to access Wrattler by pointing your browswer to ```localhost:8080```.

The local directory ```public/``` containing example markdown files is mounted as ```build/public/``` on the docker container, so you can edit files locally in this directory, and view e.g. ```welcome.md``` in your browser at ```localhost:8080/?public/welcome```.


Once you have finished, you can stop the docker containers by running (from this directory):
```
docker-compose down
```
