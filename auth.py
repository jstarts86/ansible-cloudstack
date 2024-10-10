#!/bin/bash

# Directory where your keytab files are located
KEYTAB_DIR="/home/ubuntu/keytabs"

# HDFS kinit commands
echo "kinit with hdfs.keytab for hdfs/Master1@CS2CLOUD.INTERNAL"
kinit -kt $KEYTAB_DIR/hdfs.keytab hdfs/Master1@CS2CLOUD.INTERNAL

echo "kinit with hdfs.keytab for hdfs/Slave1@CS2CLOUD.INTERNAL"
kinit -kt $KEYTAB_DIR/hdfs.keytab hdfs/Slave1@CS2CLOUD.INTERNAL

echo "kinit with hdfs.keytab for hdfs/Slave2@CS2CLOUD.INTERNAL"
kinit -kt $KEYTAB_DIR/hdfs.keytab hdfs/Slave2@CS2CLOUD.INTERNAL

# YARN kinit commands
echo "kinit with yarn.keytab for yarn/Master1@CS2CLOUD.INTERNAL"
kinit -kt $KEYTAB_DIR/yarn.keytab yarn/Master1@CS2CLOUD.INTERNAL

echo "kinit with yarn.keytab for yarn/Slave1@CS2CLOUD.INTERNAL"
kinit -kt $KEYTAB_DIR/yarn.keytab yarn/Slave1@CS2CLOUD.INTERNAL

echo "kinit with yarn.keytab for yarn/Slave2@CS2CLOUD.INTERNAL"
kinit -kt $KEYTAB_DIR/yarn.keytab yarn/Slave2@CS2CLOUD.INTERNAL

# HTTP kinit commands (for Knox)
echo "kinit with HTTP.keytab for HTTP/Knox@CS2CLOUD.INTERNAL"
kinit -kt $KEYTAB_DIR/HTTP.keytab HTTP/Knox@CS2CLOUD.INTERNAL

echo "kinit with HTTP.keytab for HTTP/Master1@CS2CLOUD.INTERNAL"
kinit -kt $KEYTAB_DIR/HTTP.keytab HTTP/Master1@CS2CLOUD.INTERNAL

echo "kinit with HTTP.keytab for HTTP/Slave1@CS2CLOUD.INTERNAL"
kinit -kt $KEYTAB_DIR/HTTP.keytab HTTP/Slave1@CS2CLOUD.INTERNAL

echo "kinit with HTTP.keytab for HTTP/Slave2@CS2CLOUD.INTERNAL"
kinit -kt $KEYTAB_DIR/HTTP.keytab HTTP/Slave2@CS2CLOUD.INTERNAL

