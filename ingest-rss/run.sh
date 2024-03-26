#!/bin/bash

docker build -t penske-ingest-rss ingest-rss
docker run -ti penske-ingest-rss
