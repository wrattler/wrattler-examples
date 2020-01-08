#!/bin/bash

## shell script to update version number in Dockerfiles
## usage:  ./bump_version.sh <version>
## where <version> is in the format vX.Y with integer X and Y.

VERSION=$1

echo VERSION is $VERSION

if [[ ! $VERSION =~ ^v[0-9]+.[0-9]+(.[0-9]+)?$ ]];
then echo "Usage is 'build_release.sh <version>'  with version format vX.Y";
     exit;
fi;

for i in `ls Dockerfile_*`;
do sed "s/:v[0-9]*\.[0-9]*/:$VERSION/" $i > ${i}.new;
   mv ${i}.new $i;
done;
