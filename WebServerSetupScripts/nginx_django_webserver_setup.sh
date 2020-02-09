#!/bin/sh

echo "Enter your virtualenv directory name: "
read virtualenv_dir

source $virtualenv_dir/bin/activate
pip install gunicorn

echo "Enter your WSGI application name (ex: app_name.wsgi:application): "
read wsgi_application

echo "Enter your server_ip/domain_name: "
read domain_or_ip
echo "Enter nginx configure filename: "
read nginx_conf
current_location=$(pwd)
if [ ! -x /usr/sbin/nginx ]; then
    sudo apt install nginx
fi

if [ -f "/etc/systemd/system/$nginx_conf.service" ]; then
    echo "File exists"
else
    sudo touch /etc/systemd/system/$nginx_conf.service
    sudo chmod 744 /etc/systemd/system/$nginx_conf.service
    echo "[Unit]\nDescription=gunicorn daemon\nRequires=$nginx_conf.socket\nAfter=network.target \
    \n\n[Service]\nUser=$USER\nGroup=www-data\nWorkingDirectory=$current_location \
    \nExecStart=$current_location/$virtualenv_dir/bin/gunicorn \ \
    \n\t--access-logfile - \ \n\t--workers 3 \ \n\t--bind unix:$current_location/$nginx_conf.sock \ \
    \n\t$wsgi_application \n\n[Install] \nWantedBy=multi-user.target">/etc/systemd/system/$nginx_conf.service

    sudo touch /etc/systemd/system/$nginx_conf.socket
    sudo chmod 744 /etc/systemd/system/$nginx_conf.socket
    echo "[Unit]\nDescription=gunicorn socket\n\n[Socket]\nListenStream=$current_location/$nginx_conf.sock\
    \n\n[Install]\nWantedBy=sockets.target">/etc/systemd/system/$nginx_conf.socket

    sudo systemctl enable $nginx_conf.socket
fi

if [ -f "/etc/nginx/sites-available/$nginx_conf.conf" ]; then
    echo "File exists"
else
    sudo touch /etc/nginx/sites-available/$nginx_conf.conf
    sudo chmod +x /etc/nginx/sites-available/$nginx_conf.conf
    printf "server{ \n\tlisten 80;\n\tserver_name $domain_or_ip;\n\tlocation = /favicon.ico { access_log off;log_not_found off; } \
    \n\tlocation /static/ {\n\t\troot $current_location;\n\t} \n\tlocation / { \n\t\tinclude proxy_params; \n\t\tproxy_pass http://unix:/$current_location/$nginx_conf.sock; \n\t} \n}">/etc/nginx/sites-available/$nginx_conf.conf

    sudo ln -s /etc/nginx/sites-available/$nginx_conf.conf /etc/nginx/sites-enabled/$nginx_conf.conf
fi

sudo systemctl daemon-reload
sudo systemctl start $nginx_conf
sudo systemctl enable $nginx-conf
sudo service nginx restart