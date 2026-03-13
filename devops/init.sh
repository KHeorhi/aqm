#!/usr/bin/ bash


if [ ${ENV} = 'DEV' ]; then
  uvicorn main:app --host 0.0.0.0 --port ${APPLICATION_PORT} --reload --no-server-header;
else
  uvicorn main:app --host 0.0.0.0 --port ${APPLICATION_PORT} --no-server-header;
fi;
