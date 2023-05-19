# ClosestPoint
THis is a django api to get the closest point from what you input


### USAGE...
- First install django and other setup requirements.
- Then clone the application using `git clone git@github.com:Stephen-Kamau/ClosestPoint.git`
- AFter cloning, `cd ClosestPoint` and then `python manage.py makemigrations` then `python manage.py migrate`
- The above will run migratiosn.
- YOu will then need to run it using `python manage.py runserver` as it will expose port 8000 by default and can be accessed via http methods.

- The app has a single endpoint whcih can either be post or get.
- The endpoint is  `api/v1/points`
- An example (Assuming you application is running on localhost).

- You can use curl to do requests.
    1. Make a post request with points such as `2,2;-1,30;0,2`
        -  We do the following `curl -X POST -d "points=2,2;-1,30;0,2" http://localhost:8000/api/v1/points`
        - THe results will be
        ````
        {"message": "Points and closest points saved successfully.", "inputs": "2,2;-1,30;0,2", "solution": "2,2;0,2"}
        ````
        - If the point has not been formated well, an error will be thrown instead.

    2. To get all points and their closest points that are saved, we do the following.
        -  `curl -X GET http://localhost:8000/api/v1/points`  It will return a list of objects with the points and their calculated values/
        
