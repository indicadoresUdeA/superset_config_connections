#!/usr/bin/env bash

# -----------------------------------------------------------------------------
# nuclear_restart_superset.sh
# Script para eliminar el contenedor de Docker y volverse a clonar Superset. Con base de datos.
# -----------------------------------------------------------------------------


cd superset

docker compose down --rmi all -v

sudo rm -rf postgres_data/

cd

sudo rm -rf superset/

git clone https://github.com/apache/superset

cd superset

docker compose -f docker-compose-non-dev.yml up
