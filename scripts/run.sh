#! /bin/bash

# Define the variables
if ! env | grep -q "MONGO_NODE_IP"; then MONGO_NODE_IP="127.0.0.1"; fi
if ! env | grep -q "MONGO_NODE_HOSTNAME"; then MONGO_NODE_HOSTNAME=$HOSTNAME; fi
if ! env | grep -q "MONGO_NODE_PORT"; then MONGO_NODE_PORT="27017"; fi
if ! env | grep -q "MONGO_NODE_ROLE"; then MONGO_NODE_ROLE="Secondary"; fi
if ! env | grep -q "CONSUL_IP"; then CONSUL_IP="127.0.0.1"; fi
if ! env | grep -q "CONSUL_PORT"; then CONSUL_PORT="8500"; fi



