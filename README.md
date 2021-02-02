# rpisurv-api
API for rpisurv

Simple API to simulate keyboard press for changing screen

Request :
pip3 install flask
pip3 install keyboard

sudo nohup python3 rpisurv-api.py > log.txt 2>&1 &

http call example:

* pause rotation
curl http://api-ip:5000/camera/pause 

* resume

curl http://api-ip:5000/camera/resume

* camera 1
curl http://api-ip:5000/camera/1
* camera 2
curl http://api-ip:5000/camera/2
* camera 3
curl http://api-ip:5000/camera/3
* camera 4
curl http://api-ip:5000/camera/4



