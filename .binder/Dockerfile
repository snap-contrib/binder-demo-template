FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

ENV BASH_ENV=~/.bashrc                                                                                                      \
    MAMBA_ROOT_PREFIX=/srv/conda                                                                                            \
    PATH=/srv/conda/envs/notebook/bin:$PATH \
    SHELL=/bin/bash \
    HOME=/root

ADD .binder/environment.yml /tmp/environment.yml
#ADD .binder/start /usr/bin/start
COPY .binder/activate-conda.sh /etc/profile.d/activate-conda.sh


RUN apt-get update                                                                                                          && \
    apt-get install -y ca-certificates wget bash bzip2                                                                      && \
    wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba --strip-components=1 && \
    ./micromamba shell init -s bash -p ~/micromamba                                                                         && \
    apt-get clean autoremove --yes                                                                                          && \
    rm -rf /var/lib/{apt,dpkg,cache,log}                                                                                    && \
    cp ./micromamba /usr/bin                                                                                                && \
    micromamba create -f /tmp/environment.yml                                                                               && \                                                              
    cd /tmp                                                                                                                 && \
    rm -fr /srv/conda/pkgs                                                                                                  && \
    rm -fr /tmp/*   
      #                                                                                                      && \
    #chmod 755 /usr/bin/start                                                                                                && \
    #mkdir /workspace

RUN mkdir -p /root/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/ && \
    echo '{ "theme":"JupyterLab Dark" }' >  /root/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings

RUN  mkdir -p /var/lib/dpkg/alternatives && \
    mkdir -p /var/lib/dpkg/info/  && \
    mkdir -p /var/lib/dpkg/updates/ && \
    touch /var/lib/dpkg/info/format-new && \
    touch /var/lib/dpkg/status

ENV SHELL=/bin/bash                                                     \
    PATH=/srv/conda/bin:$PATH                                           \
    NB_USER=jovyan                                                      \
    NB_UID=1000                                                         \
    NB_GID=1000                                                         \
    USER=jovyan                                                         \ 
    HOME=/home/jovyan                                                   \
    CONDA_DIR=/srv/conda/                                               \
    APP_BASE=/srv 
    
RUN groupadd --gid ${NB_GID} ${NB_USER} &&                              \
    useradd --comment "Default user"                                    \
            --create-home                                               \
            --gid ${NB_GID}                                             \
            --no-log-init                                               \
            --shell /bin/bash                                           \
            --uid ${NB_UID} ${NB_USER}

# workspace
RUN mkdir -p /workspace &&                                              \
    chown -R ${NB_USER}:${NB_GID} /workspace &&                         \
    mkdir -p /usr/local/share/jupyter &&                                \
    chown -R ${NB_USER}:${NB_GID} /usr/local/share/jupyter

EXPOSE 8888 

ADD .binder/jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config.py

# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

WORKDIR /workspace