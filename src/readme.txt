1. install Python==3.6.2 on the pc(www.python.org) then edit envirnoment variable path to add python path

2.Install virtualenv and activate it by the following command

pip install virtualenv

3. open cmd at the project folder and run the command
virtualenv venv
cd venv
Scripts\activate
cd ..
cd src

4.install reqiured packages from requirement.txt using the following command

pip install -r requirements.txt

5.Download the redis server from https://redis.io/download then unzip the tzr.gz file using winzip. do to redis folder start redis-server by double clicking the redis-server.exe file.

6. python manage.py migrate

7. python manage.py runserver



