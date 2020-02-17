FROM wrattler/wrattler_base:v0.1.6

RUN pip3 install --no-cache-dir notebook==5.*
RUN pip3 install jupyter-server-proxy


ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}


# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

# Build the AI assistants stuff again

WORKDIR ${HOME}/binder

# Use SVN(!) to get the resources directory from github
RUN svn checkout https://github.com/wrattler/wrattler-examples/trunk/resources
RUN pip install .
RUN chmod a+x start
ENTRYPOINT ["./start"]