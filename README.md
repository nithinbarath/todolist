# ToDo-list

ToDo-list is a simple web application to save Your daily tasks in order not to miss anything.


### Technologies used:

* Reactjs (javascript frontend framework)
* Fastapi (python RESTAPI backend framework)
* Postgresql Database (store, retrieve and derive any type of data)
* Alembic ( used to auto migrate tables from backend models to database)


### RUN the app

#### Frontend:

1. make sure nodejs is installed
2. then move to frontend folder ```npm install```
3. install extra dependencies axios,react-router-dom.
4. finally run the frontend by using command ```npm start```

#### Backend:

Everything is containerized from backend to the database. So all you need is Docker installed, and then you can run :

```docker-compose up --build```

To see logs run

``` docker-compose logs -f -t```
