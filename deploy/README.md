``` $ scp -i /path/to/cert.pem deploy/prod/* ubuntu@ec2-18-217-172-120.us-east-2.compute.amazonaws.com:/srv/askme ```
``` $ scp -i /path/to/cert.pem deploy/prod/* ubuntu@ec2-18-217-172-120.us-east-2.compute.amazonaws.com:/srv/askme ```
``` $ docker push muslimbeibytuly/askme:master ```

first time:
``` $ cp deploy/prod/generic.nginx.conf deploy/prod/nginx.conf ```
``` $ sed -i 's/DOMAIN_NAME/asdfg.ga/g' deploy/prod/nginx.conf ```
setup domain name at setup.sh
``` $ ssh user@host ```
``` $ sudo mkdir /srv/askme/ ```
``` $ sudo chown -R user /srv/askme/ ```
``` $ scp deploy/prod/* user@host:/srv/askme/ ```
``` $ ssh user@host "cd /srv/askme/ && chmod +x setup.sh && sudo ./setup.sh" ```

every time:
``` $ scp -i /path/to/askme.pem deploy/prod/* user@host:/srv/askme/ ```
``` $ ssh -i /path/to/askme user@host "cd /srv/askme/ && sudo docker-compose pull && sudo docker-compose down && sudo docker-compose up -d" ```


TODO: Automate using Travis/GitLab/Circle CI
