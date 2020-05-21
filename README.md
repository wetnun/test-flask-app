# Simple Flask App

Example of a MariaDB app

Has an example db with simple messages table.  Picks a message at random and displays it.

Requires docker 1.13.1 or higher

## Stand up the stack

* git clone this repo
* cd into repo
* docker stack deploy -c stack.yml pytest
* docker stack ps pytest

Now you can check the logs to verify it's loaded.  And then you should see something like this:

  INFO success: nginx entered RUNNING state, process has stayed up for > than 1 seconds

Now view the thing:

http://$hostname:6005/

## Want to login to verify the container?

* docker exec -it $(docker ps -q -f name=pytest_app.1) bash

## View the logs:

* docker logs -f $(docker ps -q -f name=pytest_app.1)

## Need to redeploy:

* docker stack deploy -c stack.yml pytest

## Restart a container:

* docker restart $(docker ps -q -f name=pytest_app.1)

