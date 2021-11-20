@echo OFF
echo Setting up MYSQL Database
start cmd.exe /K "cd mysql/bin && mysqld.exe"
echo Setting up Django and required libraries
pip install flask
pip install flask-cors
pip install flask_mail
pip install xlwt
pip install SQLAlchemy
pip install pandas-sql
pip install mysql-connector-python
CALL C:\Users\%USERNAME%\Envs\tproject\Scripts\activate.bat
pip install mysql-connector-python
py -m pip install Django
pip install scikit-learn
pip install pandas
pip install numpy
pip install PyMsgBox
pip install PyMySQL
pip install requests
start cmd.exe /K "cd traffic && set FLASK_APP=app.py && flask run"
python manage.py runserver