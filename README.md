# 51205-team-proj-2020-Fall
mpcs 51202 team project for 2020 Fall

# members:

Xu, Yifei	yifeix@uchicago.edu
Sriram, Anirudh srirama@uchicago.edu
Qian, Kun	qiank@uchicago.edu
Ma, Tian    matian@uchicago.edu

# instructions:

on a mac:

1. run rabbitmq-server

2. run 'python3 mediator.py'

3. run 'docker stop $(docker ps -a -q)' and 'docker rm $(docker ps -a -q)' to stop and remove all containers

4. docker run -it -p 6667:6667  --name email_service auction_user_email_services_image:team3 '/bin/bash'

    from the prompt, cd ~/51205-team-proj-2020-Fall/email_service

    run 'pg_lsclusters', check postgreSQL status

    if postgres status is down (RED), run 'pg_ctlcluster 10 main start'

    finally run 'python3 email_service.py'

5. docker run -it -p 6662:6662  --name user_service auction_user_email_services_image:team3 '/bin/bash'

    from the prompt, cd ~/51205-team-proj-2020-Fall/user_service

    run " echo '{"_default": {}}' > users.json "  to clear database

    run 'python3 user_service.py'

6. docker run -it -p 6664:6664  --name auction_service auction_user_email_services_image:team3 '/bin/bash'

    from the prompt, cd ~/51205-team-proj-2020-Fall/auction_service

    run " echo '{"_default": {}}' > items.json "  to clear database

    run 'python3 auction_service.py'

7. start frontend on host with 'flask run --host=127.0.0.1 --port=6663' then start web brower http"//"127.0.0.1:6663 
