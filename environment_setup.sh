#!/bin/bash

# Update package list and install necessary dependencies
sudo apt-get update
sudo apt-get install -y openjdk-11-jdk wget

# Install Apache Kafka
wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.13-2.8.0.tgz
tar -xzf kafka_2.13-2.8.0.tgz
mv kafka_2.13-2.8.0 kafka

# Install Apache Spark
wget https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
tar -xzf spark-3.1.2-bin-hadoop3.2.tgz
mv spark-3.1.2-bin-hadoop3.2 spark

# Install Python and necessary packages
sudo apt-get install -y python3 python3-pip
pip3 install pyspark kafka-python

# Export environment variables
echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" >> ~/.bashrc
echo "export SPARK_HOME=$HOME/spark" >> ~/.bashrc
echo "export PATH=$PATH:$HOME/kafka/bin:$SPARK_HOME/bin" >> ~/.bashrc
source ~/.bashrc
