# Lab 32: Permissions & Postgresql
## Features - Django REST Framework
  - Make your site a DRF powered API as you did in previous lab.
  - Adjust project’s permissions so that only authenticated user’s have access to API.
  - Add a custom permission so that only author of blog post can update or delete it.
  - Add ability to switch user’s directly from browsable API.


## Features - Docker
  - create `Dockerfile` based off python:3.8-slim
  - create `docker-compose.yml` to run Django app as a web service.
  - enter `docker-compose up --build` to start your site.
  - add postgres 11 as a service
  - Go to browsable api and confirm site properly restricts users based on their permissions.


## [PR](https://github.com/noureddein/drf-api-permissions-postgres/pull/1)