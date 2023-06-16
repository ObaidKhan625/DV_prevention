# DV_preventionaa# DV_prevention

• A project that aims to connect domestic violence victims and activists/NGOs with minimum effort.<br>
• The project uses Django as the Backend, HTML/CSS/Bootstrap/JS along with JQuery and AJAX for frontend.<br>
• There’s the MapBox API added for victims to find activsts/NGOs nearest to them(Location restricted only to India).<br>
• I have used a ASGI server for allowing websockets and django-channels to give notifications to users<br>
asynchronously, and used Redis to store groups.

# Setup to run on your local system

• Activate virtual environment and install all packages
```
virtualenv .
./Scripts/activate
pip install -r requirements.tt
```
• I have also used websockets here and redis for real time asynchronous notifications, so you'll need to run redis on your system. I did so using Docker.<br>
• Run redis using Docker on port 6379
```
docker run --name rdb -p 6379:6379 redis
```
• Also you'll need an MapBox API key(free of cost within a limit) for finding nearest activists, go to
```
complaints/templates/complaints/nearest_activist_map.html
```
Line 218:
```
mapboxgl.accessToken = ACCESS_TOKEN_HERE;
```

• Finally, run the server, Go to the DV_prevention folder
```
cd DV_prevention
python manage.py runserver
```
A few Screenshots:

![Screenshot (185)](https://user-images.githubusercontent.com/72970106/175808831-ebd47751-e85f-47dd-9657-4056bfb1f569.png)

![Screenshot (185) 1](https://user-images.githubusercontent.com/72970106/175808839-f2785198-af47-4a92-a8b7-023f8890f9bd.png)

Drag and Drop using Dropzone.js: 
![Screenshot (185) 2](https://user-images.githubusercontent.com/72970106/175808847-451bff3e-fc62-464b-b668-369480200889.png)

Nearest Activist:
![Screenshot (187)](https://user-images.githubusercontent.com/72970106/175808851-d3370c04-c38d-4e79-b229-d8579774946c.png)

