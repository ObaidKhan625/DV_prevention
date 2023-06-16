# DV_prevention

• A project that aims to connect domestic violence victims and activists/NGOs with minimum effort.<br>
• The project uses Django as the Backend, HTML/CSS/Bootstrap/JS along with JQuery and AJAX for frontend.<br>
• There’s the MapBox API added for victims to find activsts/NGOs nearest to them(Location restricted only to India).<br>
• I used daphne as an ASGI server for allowing websockets and django-channels to give notifications to users<br>
asynchronously, and used Redis to store groups.<br>
• Also, I recently added NGINX as a reverse proxy and to serve static files. <br>
• The entire project has been dockerized as well.

# Setup to run on your local system

• Make sure you have docker installed and run this in the root directory:
```
docker-compose up
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
A few screenshots from some pages:

Complaints:

![image](https://user-images.githubusercontent.com/72970106/218266271-ede2e738-a127-4dc5-9be7-39c83aaddd5c.png)

Complaint detail:

![image](https://user-images.githubusercontent.com/72970106/218266254-9a4ae287-d12c-4ce7-998f-4b2016efa745.png)

Profile page with drag and drop: 

![image](https://user-images.githubusercontent.com/72970106/218266294-d80b0eeb-7c7a-48e7-b238-18fc2deac263.png)

Nearest Activist:

![image](https://user-images.githubusercontent.com/72970106/218266220-1c1d3e37-96b3-47bc-8cb3-d7d88f2eeb7b.png)

