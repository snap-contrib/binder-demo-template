CONDA_DIR=/srv/conda/envs/notebook
CONDA_PROFILE="${CONDA_DIR}/etc/profile.d/conda.sh"
test -f $CONDA_PROFILE && . $CONDA_PROFILE
