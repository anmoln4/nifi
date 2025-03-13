#!/bin/sh -x
kubectl create configmap nifi-registry-auth-conf \
        --from-file=authorizations.xml=tests/02-authorizations.xml \
        --from-file=users.xml=tests/02-users.xml

kubectl create configmap nifi-tester-flow \
        --from-file=tests/02-nifi-tester-flow.xml

kubectl create configmap nifi-registry-auth-conf --from-file=authorizations.xml=./nifi1/charts/nifi-registry/tests/02-authorizations.xml --from-file=users.xml=./nifi1/charts/nifi-registry/tests/02-users.xml