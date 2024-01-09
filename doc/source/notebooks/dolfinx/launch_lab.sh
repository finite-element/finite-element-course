#!/usr/bin/env bash
docker run -p 8888 --init -ti -v $(pwd):/shared -w /shared dolfinx/lab:latest
