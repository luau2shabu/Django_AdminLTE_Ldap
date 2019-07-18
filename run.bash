#!/bin/bash
# echo -e "\n $(ip addr |grep 172| awk '{print $2}'| cut -d/ -f1)	$(hostname)" >> /etc/hosts
# python app.py
python manage.py runserver 0.0.0.0:5000