# GenshinDB Project

## About

This is a project to help store data related to Genshin Impact Characters, Items, and related content. It is not affiliated with the offical Genshin Impact Game.

## Tech Stack

- Python 3
- Django
- Docker

## How to Run

The easiest way to run this project is by installing Docker and running `docker-compose up` in the base directory.

## Deployment

This application is built into a container hosted on this projects Github Packages repository, the container is then pulled down on the production server. All this is done via Github Actions pipelines.
