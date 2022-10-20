# ToDo-list

ToDo-list is a simple web application to save Your daily tasks in order not to miss anything.


### Technologies used:

* Reactjs (javascript frontend framework)
* Fastapi (python RESTAPI backend framework)
* Postgresql Database (store, retrieve and derive any type of data)
* Alembic ( used to auto migrate tables from backend models to database)


### RUN the app

#### Frontend:

1. make sure Nodejs is installed
2. then move to frontend folder ```npm install```
3. install extra dependencies axios,react-router-dom.
4. finally run the frontend by using command ```npm start```
5. Open http://localhost:3000 to view it in your browser.

#### Backend:

Everything is containerized from backend to the database. So all you need is Docker installed, and then you can run :

```docker-compose up --build```

connect to the postgresql database by using configurations in ```env/dev.env``` file

Open http://localhost:9559 to view it in your browser.

##### Interactive API docs

Now go to http://127.0.0.1:8000/docs.
You will see the automatic interactive API documentation (provided by Swagger UI):

##### Alternative API docs

And now, go to http://127.0.0.1:8000/redoc.
You will see the alternative automatic documentation (provided by ReDoc):

To see logs run

``` docker-compose logs -f -t```
