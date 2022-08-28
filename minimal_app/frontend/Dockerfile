FROM node:16.0.0-alpine as build-stage
WORKDIR /app
COPY ./vue-project ./
RUN npm install
RUN npm run build

FROM nginx:stable-alpine as production-stage
RUN file="$(ls )" && echo $file
COPY --from=build-stage /app/dist /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]