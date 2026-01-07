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

 

 

 
 
 
