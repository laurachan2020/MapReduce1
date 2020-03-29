#!/bin/bash

/etc/bootstrap.sh
THIS_DIR=/usr/local/hadoop

if [ -n "$1" ];
then SUB_DIR="$1/" 
fi
echo "SUB_DIR = ${SUB_DIR}"

if [ -n "$2" ];
then PATTERN="$2" 
fi

echo "PATTERN = ${PATTERN}"


${THIS_DIR}/bin/hadoop dfsadmin -safemode leave
${THIS_DIR}/bin/hadoop fs -mkdir -p ${THIS_DIR}/py/sample
${THIS_DIR}/bin/hdfs dfs -put ${THIS_DIR}/py/${SUB_DIR}sample/* ${THIS_DIR}/py/sample
${THIS_DIR}/bin/hadoop jar \
    ${THIS_DIR}/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
    -file ${THIS_DIR}/py/${SUB_DIR}mapper.py \
    -mapper "${THIS_DIR}/py/${SUB_DIR}mapper.py $PATTERN"\
    -file ${THIS_DIR}/py/${SUB_DIR}reducer.py	\
    -reducer "${THIS_DIR}/py/${SUB_DIR}reducer.py ${*:2}" \
    -input ${THIS_DIR}/py/sample/* \
    -output ${THIS_DIR}/py-output
${THIS_DIR}/bin/hdfs dfs -cat ${THIS_DIR}/py-output/*
