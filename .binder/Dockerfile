FROM terradue/docker-snap:latest

USER jovyan

COPY --chown=1000:1000 . ${HOME}

RUN mamba env create -n notebook -f ${HOME}/.binder/environment.yml

RUN test -f ${HOME}/environment.yml && mamba update -p /srv/conda/envs/notebook -f ${HOME}/environment.yml  && \
    test -f ${HOME}/postBuild && chmod +x ${HOME}/postBuild && ${HOME}/postBuild || exit 0

ENV PATH=/srv/conda/envs/notebook/bin:${PATH}

EXPOSE 8888

USER jovyan

WORKDIR /home/jovyan
