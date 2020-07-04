# ThanhWorks -- Mouse cursor movement

conda create --name ThanhEnvironment python=3.7
pip install otree
pip install pandas
pip install Flask-RESTful

Console1:
conda activate ThanhEnvironment
cd /mnt/d/ThanhhWork/surveyproject
otree devserver

Console2:
cd /mnt/d/ThanhhWork/surveyproject/FlaskApp
python LogData.py

http://localhost:8000/demo/

open folder D:\ThanhhWork\surveyproject\LogData and view the logfile

