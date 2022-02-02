#!/usr/bin/env bash
docker run -ti -v $(pwd):/shared -w /shared dolfinx/dolfinx:latest
