#!/bin/bash

wrattler-python-service &
wrattler-data-store &
cd server/R; Rscript app.R &
cd -
cd client; http-server public -c-1 --cors=http://localhost:8889 &
cd -
cd jupyterlab; jupyter lab --ip 0.0.0.0 --port 8889 --allow-root
