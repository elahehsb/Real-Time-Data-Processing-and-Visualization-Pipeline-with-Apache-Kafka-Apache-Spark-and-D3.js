This project focuses on building a real-time data processing pipeline using Apache Kafka for data streaming, Apache Spark for real-time data processing, and D3.js for interactive data visualization.

Explanation

1.	Environment Setup:

•	The ‘environment_setup.sh’ script sets up a Linux environment by installing Java, Apache Kafka, Apache Spark, Python, and the required Python packages (pyspark, kafka-python).

2.	Data Producer:

•	The ‘data_producer.py’ script simulates real-time data generation and streams data to a Kafka topic (real-time-data) using Kafka Producer. Each message contains a timestamp and a randomly generated value.

3.	Data Processing:

•	The ‘data_processing.py’ script uses Apache Spark to consume real-time data from the Kafka topic, process it using Spark SQL, and print the processed data to the console. This demonstrates real-time data processing capabilities.

4.	Data Visualization:

•	The ‘index.html’ file creates an interactive data visualization using D3.js. It sets up an SVG canvas and updates it with real-time data fetched from a Flask server.
•	The ‘server.py’ script runs a Flask server that simulates real-time data responses. It generates and returns random data points with timestamps to the client-side D3.js script for visualization.
