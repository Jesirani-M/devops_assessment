Devops Assessment 

Project1 

To Deploy static website in linux using nginx server and need to run this file using Docker and to push in docker hub: 

Creating folder “project1” in /var/www/ this directory and created “index.html” inside this folder. 

Setting Configuration – created file “project1” in /etc/nginx/sites-available/project1 and given configuration as follows  

“server{ 

listen 8076; 

server_name _; 

root /var/www/project1; 

index index.html; 

location / { 

try_files $uri $uri/ =404; 

} 

}   ” 

Created symbolic link for this configuration file - “sudo ln –s /etc/nginx/sites-available/project1 /etc/nginx/sites-enabled/” 

Checked this configuration are successfull or not by using the following command  

“sudo nginx –t 

 sudo systemctl reload nginx” 

Firewall access- allowing the specified port number in firewall “sudo ufw allow 8076” 

To check the output run “curl http://10.51.25.226:8076” 

We can view in browser by typing as “http://10.51.25.226:8076” 

Docker Implementation: 

Open this directory /var/www/project1  

Create Dockerfile inside this folder.Inside that 

“FROM nginx:latest 
COPY . /usr/share/nginx/html 
EXPOSE 80” 

To build image , run “docker build –t project1_image .” 

To run this image as a container , run “docker run –d –p 8077:80 –name project1_container project1_image” 

Allowing this 8077 in firewall “sudo ufw allow 8077” 

Now we can run in the browser as “http://10.51.12:226:8077” 

-d means running that container in background 

-p means port ,8077 is any free port we can give and 80 is a port which given in dockerfile  

Container name – project1_container 

Image name – project1_image 

Docker to Docker Hub: 

Open this directory /var/www/project1 

Pushing image to docker hub account,need to login using “docker login –u ranimariyasusai” and enter password and log in  

Run “docker tag project1_image ranimariyasusai/project1_image:v1, 

docker push ranimariyasusai/project1_image:v1 ” 

Now project1_image pushed to docker hub account. 

Project1 to Github Repository: 

Created github repository as “devops_assessment” 

Cloned the repository using “git clone https://github.com/Jesirani-M/devops_assessment.git” 

Uploaded the project1 folder which contains Dockerfile and index.html and cloned the github repository in this folder and added this files inside this repositoy using “git add . ” 

Commited changes using “git commit –m project1 pushed in this repository” 

Pushed the changes to repository using “git push” 

PROOF:
 
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/254283c7-7f08-421d-8fe1-06f64919cd70" />

Project2

To create python file which continuously reads and writes in text file and to create image and container for that file
and to create volume for that container and after deleting that container,new containers will run the existing volume:

Created python file in this directory "/var/www/project2/app.py"

 app.py 
 
  "import time
   
   from datetime import datetime

   FILE_PATH = "/app/data/log.txt"

   while True:
   
    with open(FILE_PATH, "a") as f:
    
        f.write(f"Log entry at {datetime.now()}\n")
    
    print("Appended a new line")
    
    time.sleep(5)"

We can run this file using "python3 app.py" command

This python file reads the output and writes the print statement in log.txt.It itself creates and writes the statement in log.txt file when i create "data" folder.

This python file reads the statement and will write in text file at every 5 seconds

Created Docker image - For creating docker image, need to create Dockerfile

 Dockerfile:
  
  "FROM python:3.11-slim
  
   WORKDIR /app
   
   COPY . .
   
   EXPOSE 80
   
   ENTRYPOINT ["python", "app.py"]"

Builed docker image using "docker build -t project2 ."

Created volume using "docker create --name project2 -v project2_container project2"

Created container and volume using "docker run --name project2 -v project2_volume project2"
Container name - project2
Image name - project2
Volume name - project2_volume
Volume file stored in this directory "/var/lib/docker/volumes/project2_volume"

Need to copy the folder in this volume path using "docker cp /var/www/project2 project2:/project2" - It will copy the project2 folder path to the volume 
 
Now I can have this project2 data in volume eventhough the container is deleted

Deleting the running container using "docker rm -f project2"

Creating new container and running this container with existing volume i.e project2_volume using "docker run --name project2_new_container -v project2_volume project2"

Docker to Docker Hub:

 Pushed the image to docker hub using "docker tag project2 ranimariyasusai/project2:v1"
"docker push ranimariyasusai/project2:v1"

Github:
 Uploaded this project2 folder to Windows and pushed this file to Github repository

Proof:

Creating volume:

<img width="1134" height="73" alt="image" src="https://github.com/user-attachments/assets/2966955b-3f47-4e8d-b968-728e63509811" />

Running container with volume and Running new container with existing volume: 

 <img width="1279" height="392" alt="image" src="https://github.com/user-attachments/assets/0c0d40ab-8a9f-47e8-8463-4961ad83b777" />

Removing existing container:
<img width="684" height="101" alt="image" src="https://github.com/user-attachments/assets/2b4b056b-bde0-4091-a4d5-75c5e0d40761" />

Output when running container will displayed in log.txt file:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/81d755e2-50eb-443d-a760-d05f24c7146d" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4bcdb180-0d45-4a52-b64b-374b1e3dc3b4" />

Docker to DockerHub:

<img width="1178" height="441" alt="image" src="https://github.com/user-attachments/assets/9cc649ff-8b84-4b29-aec8-c16c5c6dbb2a" />

Pushing project2 folder to Github repository:

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/bcee6a67-c702-4a4a-aaa8-365cf1154335" />

Logs of container:

<img width="912" height="251" alt="image" src="https://github.com/user-attachments/assets/11878640-a8d8-4674-bd04-c3a9632a27f0" />








 
 
 
