FROM wrattler/wrattler_base:v0.7

RUN apt-get update; apt-get install -y python-gi-cairo
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


# Install jupyter extensions in home directory
RUN mkdir ${HOME}/.jupyter
RUN mkdir ${HOME}/.jupyter/lab
RUN mkdir ${HOME}/.jupyter/lab/applications
ENV JUPYTERLAB_DIR /home/jovyan/.jupyter/lab/applications

WORKDIR ${HOME}
## Checkout Wrattler and switch to branch with AI-assistants
RUN git clone https://github.com/wrattler/wrattler; cd wrattler; git checkout develop; cd -;

# AI assistants
ENV DATASTORE_URI http://localhost:7102
RUN dotnet restore wrattler/aiassistants/server/
RUN dotnet build wrattler/aiassistants/server/

# Client
RUN cd wrattler/client; yarn; yarn build; cp build/wrattler-app.js public/; cd -

# Jupyterlab
RUN cd wrattler/jupyterlab_wrattler; yarn install; jupyter labextension link .; jupyter labextension install;  jlpm run build; cd -;

WORKDIR ${HOME}/binder

# Use SVN(!) to get the resources directory from github
#RUN svn checkout https://github.com/wrattler/wrattler-examples/trunk/resources
RUN svn checkout https://github.com/wrattler/wrattler-examples/branches/feature/consolidate-examples/resources
RUN svn checkout https://github.com/wrattler/wrattler-examples/branches/feature/consolidate-examples/examples

# Link the resources directory to somewhere accessible to the client,
# so that it can serve e.g. python or .R files containing definitions.
RUN rm -rf ${HOME}/wrattler/client/public/resources
RUN ln -s ${HOME}/binder/resources ${HOME}/wrattler/client/public/resources
RUN ln -s ${HOME}/binder/demo_27022020 ${HOME}/wrattler/client/public/demo_27022020

RUN pip install .
RUN chmod a+x start
ENTRYPOINT ["./start"]
