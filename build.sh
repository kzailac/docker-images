#!/bin/bash

set -ex

REGISTRY="argo.registry:5000"
BRANCH=$1

for d in */ ; do
    if [[ "$d" == "utils/" ]]; then
        continue;
    fi
    echo '>>> Build Image: ' $d

    # Get version and image name
    VERSION=`cat $d/VERSION`
    IMAGE=`echo ${d%/}`
    echo '>>> Image:' $IMAGE:$VERSION
    version_exists=`curl $REGISTRY/v2/$IMAGE/tags/list | grep "${VERSION}" ; exit 0`
    if [[ "$version_exists" ==  *"$VERSION"* ]]; then
        echo ">>> Skiping build. Image version already exists in registry"
        continue;
    fi
    # Build Docker image and tag version
    docker build -f $IMAGE/Dockerfile . -t $IMAGE:latest
    docker tag $IMAGE:latest $IMAGE:$VERSION
    
    # Push to docker registry
    if [ "$BRANCH" == "master" ]; then
        echo ">>> Pushing image to docker registry"
        docker tag $IMAGE:latest $REGISTRY/$IMAGE:latest
        docker tag $IMAGE:$VERSION $REGISTRY/$IMAGE:$VERSION
        docker push $REGISTRY/$IMAGE:$VERSION
        docker push $REGISTRY/$IMAGE:latest
    fi
done