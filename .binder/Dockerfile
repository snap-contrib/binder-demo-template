FROM terradue/docker-snap:latest

USER root

RUN usermod -u 1000 jovyan
RUN groupmod -g 1000 jovyan
RUN chown -R jovyan:jovyan /srv/conda/envs/
 
USER jovyan

COPY --chown=jovyan:jovyan . ${HOME}

RUN mamba env create -n notebook -f ${HOME}/.binder/environment.yml

RUN test -f ${HOME}/environment.yml && mamba update -p /srv/conda/envs/notebook -f ${HOME}/environment.yml  && \
    test -f ${HOME}/postBuild && chmod +x ${HOME}/postBuild && ${HOME}/postBuild || exit 0

ENV PATH=/srv/conda/envs/notebook/bin:${PATH}

EXPOSE 8888

USER jovyan

WORKDIR /home/jovyan
