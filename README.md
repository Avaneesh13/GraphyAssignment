# Follow the steps to setup the backend server locally:

## **Setup Postgres:**
1. sudo -i -u postgres
2. psql
3. create database graphy_assign;
4. create user graphy with encrypted password 'graphyassign';
5. grant ALL on DATABASE graphy_assign to graphy;


## **Setup backend**:
1. git clone https://github.com/Avaneesh13/GraphyAssignment.git
2. cd GraphyAssignment
3. virtualenv -p python3 venv
4. source venv/bin/activate
5. pip3 install -r requirements.txt 



## **Start server locally:**
1. Run the following 3 commands in seperate terminals:
	* celery -A GraphyAssignment worker -l info
	* celery -A GraphyAssignment beat -l info
	* python manage.py runserver
	
## APIs:
1. https://ava-graphy-assignment.herokuapp.com/api/v1/story/?limit=<value>&offset=<value> : GET.
2. https://ava-graphy-assignment.herokuapp.com/api/v1/story/<id> : GET.
3. https://ava-graphy-assignment.herokuapp.com/api/v1/story/ : POST - User GET(Retrieve) as a reference for post body. Pass file in content parameter.

* The app is deployed on Heroku along with the database and redis.
* Code pipeline is also enabled through code pushes on Github.

### Note: Background media optimizations aren't working in the deployed application, as open() isn't able to access the files.