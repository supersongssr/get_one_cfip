# get_one_cfip
give me a cfip by fastapi


fastapi, 每次获取一个cf cdn 大陆可访问ip. 
徐自己搭建

## install 
```shell
cd project
pip install -r requirements.txt
pip install fastapi 
pip install "uvicorn[standard]"
```

## running
- 注意事项: 文件夹权限 root
- 安装如下, 其中 DynamicUser 很重要
debian
```shell
echo > /etc/systemd/system/get_one_cfip.service
nano /etc/systemd/system/get_one_cfip.service


[Unit]
Description=Uvicorn get one cfip
After=network.target

[Service]
Type=simple
User=root 
Group=root 
DynamicUser=true
WorkingDirectory=/root/scripts/get_one_cfip  
ReadWriteDirectories=/root/scripts/get_one_cfip/
ExecStart=/usr/local/bin/uvicorn main:app  --port 12334  
ExecReload=/bin/kill -HUP ${MAINPID}
Restart=always
RestartSec=5

[Install]
WantedBy=multi - user.target



systemctl daemon-reload
cat /etc/systemd/system/get_one_cfip.service
systemctl restart get_one_cfip 
sleep 1
systemctl status get_one_cfip

```