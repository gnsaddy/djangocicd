# pull official base image
FROM node:16.3.0-alpine

RUN mkdir -p /app/frontend
# set working directory
WORKDIR /app/frontend

COPY ./frontend/package.json ./
COPY ./frontend/yarn.lock ./

RUN yarn install

COPY ./frontend/ ./

EXPOSE 3000

# start app
CMD ["yarn", "dev"]