FROM terradue/docker-snap:latest

USER root

RUN usermod -u 1000 jovyan   && \
    groupmod -g 1000 jovyan

RUN chown -R jovyan:jovyan /srv/conda/envs/env_snap
RUN chown -R jovyan:jovyan /srv/conda/pkgs/cache

USER jovyan

COPY --chown=jovyan:jovyan . ${HOME}

RUN mamba update -p /srv/conda -f ${HOME}/.binder/environment.yml

RUN test -f ${HOME}/environment.yml && mamba update -p /srv/conda/envs/env_snap -f ${HOME}/environment.yml  && \
    test -f ${HOME}/postBuild && chmod +x ${HOME}/postBuild && ${HOME}/postBuild || exit 0

EXPOSE 8888

USER jovyan

WORKDIR /home/jovyan
