REMOTE_HOST=clarovak@147.33.245.66 \
PORT=8501 \
CONDA_ENV_PATH=/home/$USER/.conda/envs/trfada_app/ \
WORKDIR=`pwd` \
qsub -v REMOTE_HOST,PORT,CONDA_ENV_PATH,WORKDIR app.sh