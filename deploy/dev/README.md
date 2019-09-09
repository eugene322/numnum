`` $ find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs sudo rm -rf ``

`` $ docker build -f deploy/production/Dockerfile -t muslimbeibytuly/askme:latest . ``

`` $ docker push muslimbeibytuly/askme:latest ``

### First time:
Insert .env

`` $ docker-compose pull ``

`` $ chmod +x setup.sh && ./setup.sh ``

### Then:

##### renew .env if needed
`` $ docker-compose pull && docker-compose down && docker-compose up -d" ``

### TODO: Automate using Travis/GitLab/Circle CI
