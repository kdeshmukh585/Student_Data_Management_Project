# Student_Data_Management_Project

A Student Data Management Web App created using Django Framework for management of Students. It performs CRUD operations on data.

I have used Python , Django , Html and CSS for the app .The database used is sqlite3 .

Make sure you have Installed Python and Django . To run the app Download the zip file and unzip it . Open the terminal get into the directory where you have saved the app.

Run the virtual environment and type the commands given below :

1) manage.py migrate

2) manage.py runserver (This command starts the server )

Open your browser and type the address - http://localhost:8000/welcome/

Used Sessions . To check working of sessions :

1) Try going on this address http://localhost:8000/show/ without logging in. It will redirect you to the login page as you have not logged in.
2) After logging in . Go on http://localhost:8000/welcome/ and click on Login . It will redirect you to http://localhost:8000/show/ as the Login information is aready saved.
