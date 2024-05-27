FROM node:22-alpine

RUN addgroup app && adduser -G app -D app

USER app

WORKDIR /code

COPY --chown=app:app package*.json .

RUN npm install

COPY --chown=app:app . .

CMD [ "npm", "start" ]