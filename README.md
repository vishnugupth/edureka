# edureka
This folder contains files which I have created for the edureka project.
dockerfile   phptestingselenium.py  playbook.yaml  website
I am not installing selenium by .jar file. 
as i am using python for it.
if you want to install selenium from jar you can download it from here 
https://pypi.org/project/selenium/


when an update happend in the website 
a jenkins job should run which will copy the docker file, website to the server
existing docker will get removed. 
then the docker will run with the docker file
docker rm nostalgic_curie -f
