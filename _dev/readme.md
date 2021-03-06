# 开发流程

## 安装python3
```
yum install yum-fastestmirror
# /etc/yum/pluginconf.d/fastestmirror.conf

yum -y install python36 python36-pip python36-devel gcc 

mkidr /home/django && cd /home/django && python3 -m venv cso_venv && \ 
git clone https://github.com/xx-scan/xx-scan 
```

## 安装 Redis
```bash
docker run --name redis -d --restart=always \
  -p 6379:6379 \
  -e 'REDIS_PASSWORD=xxscan' \
  -v /srv/docker/redis:/var/lib/redis \
  sameersbn/redis:4.0.9-2
```

## 安装Nysql
```
docker run -itd --name=mysql -p 3306:3306 --restart=always \
-v /srv/docker/data/mysqldata:/var/lib/mysql \
-e MYSQL_USER=admin007 \
-e MYSQL_PASSWORD=myadmin@816 \
-e MYSQL_DATABASE=xxscan \
-e MYSQL_ROOT_PASSWORD=test@1q2w2e4R \
mysql:5.7

drop database xxscan;
CREATE DATABASE xxscan DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

