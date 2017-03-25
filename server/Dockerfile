FROM node:6.3.1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN npm install -g nodemon
COPY package.json /usr/src/app
EXPOSE 3001
CMD npm install
