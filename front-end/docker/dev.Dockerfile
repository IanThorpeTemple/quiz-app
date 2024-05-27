FROM node:22-alpine

RUN useradd -ms /bin/sh app

USER app

WORKDIR /code

COPY --chown=app:app package*.json .

RUN npm install

COPY --chown=app:app . .

CMD [ "npm", "start" ]