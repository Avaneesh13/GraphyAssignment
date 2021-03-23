#Follow the steps to setup the backend server locally:

##**Setup Postgres:**
1. sudo -i -u postgres
2. psql
3. create database graphy_assign;
4. create user graphy with encrypted password 'graphyassign';
5. grant ALL on DATABASE graphy_assign to graphy;


##**Setup backend**:
1. git clone https://github.com/Avaneesh13/GraphyAssignment.git
2. cd GraphyAssignment
3. virtualenv -p python3 venv
4. source venv/bin/activate
5. pip3 install -r requirements.txt 



##**Start server locally:**
1. Run the following 3 commands in seperate terminals:
	* celery -A picha worker -l info
	* celery -A picha beat -l info
	* python manage.py runserver