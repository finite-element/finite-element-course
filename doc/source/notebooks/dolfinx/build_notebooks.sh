#!/usr/bin/env bash
cd blank && ls ../*.py | xargs -I '{}' basename '{}' '.py' | xargs -I '{}' jupytext --update --to ipynb -o '{}'.ipynb ../'{}'.py && cd ../
docker run -v $(pwd):/shared -w /shared -t dolfinx/dolfinx:latest \
  /bin/bash -c "pip install jupyter jupytext && python3 -m ipykernel install --name dolfinx && cd executed && ls ../*.py | xargs -I '{}' basename '{}' '.py' | xargs -I '{}' jupytext --update --to ipynb --execute --set-kernel dolfinx -o '{}'.ipynb ../'{}'.py" 
