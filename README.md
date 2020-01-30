![Image of GRnet](https://avatars0.githubusercontent.com/u/6882712?s=200&v=4)
# Argo Docker Images

This repo contains the docker images used for building argo project packages.

# Conventions
- Each directory name is the docker image name
- Each directory MUST contain a Dockerfile
- Each folder MUST contain a VERSION file and we should follow [Semantic Versioning](https://semver.org/) for every new change
- build.sh builds every image and push it to our private registry when built on Jenkins

# Build Locally
Clone current repo and cd in it.
Then:
```
cd <directory-image>
docker build . --tag <name>
```