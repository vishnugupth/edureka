y
FROM  devopsedu/webapp
RUN mkdir git
# Install dependencies
RUN apt-get update && \
apt-get install -y git build-essential curl wget software-properties-common zip unzip
RUN git init
RUN cd git
RUN git clone https://github.com/edureka-devops/projCert.git
RUN cd projCert
ADD website /var/www/html/
CMD ["apache2ctl", "-D","FOREGROUND"]

