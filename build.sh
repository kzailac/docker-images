#!/bin/sh

set -e

REGISTRY="argo.registry:5000"

for d in */ ; do
    cd $d
    echo '>>> Change directory to: ' `pwd`

    # Get version and image name
    VERSION=`cat VERSION`
    IMAGE=`pwd | sed 's#.*/##'`
    echo '>>> Image:' $IMAGE:$VERSION

    # Build Docker image and tag version
    docker build . -t $REGISTRY/$IMAGE:latest
    docker tag $REGISTRY/$IMAGE:latest $REGISTRY/$IMAGE:$VERSION
    
    # Push to docker registry
    docker push $REGISTRY/$IMAGE:$VERSION
    docker push $REGISTRY/$IMAGE:latest
    cd ..
done