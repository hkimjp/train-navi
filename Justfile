TAG := "hkimjp/python:3.13.4"

build:
  docker build --pull -t {{TAG}} .