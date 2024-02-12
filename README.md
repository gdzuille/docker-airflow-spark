# Airflow for testing and home usage
## Docker Installation
When using Docker, you will need to install it via the [official website](https://www.docker.com/get-started/).

Navigate to the project folder via shell or in your IDE terminal.

Then compose the container by running the following command:

```shell
docker-compose up -d --build
```

#### Running the process with Airflow

For accessing Airflow Webserver, go to <localhost:8080>.

The default test user is:
```
user: admin

pass: admin
```
If you want to check the Spark UI, you can access it through <localhost:9090>.

Before running any Spark Job, you will need to create the Spark connection used by the Operators, you can do so by following the next steps:

- Acces the [Webserver UI](localhost:8080), go to Admin > Connections

- Create a new connection with the following parameters:

<p align="center">
  <img src="https://i.ibb.co/pfQWvm9/spark-conn.png" alt="DAG"/>
</p>

The connection name must be the same as on the DAG that uses it. 
Check the file */dags/test_dag.py* for an example.

## Installation
### Prerequisites for developing
- **Python**: for developing I've used Python 3.8.10, on the Docker the version installed is 3.11. The Poetry dependencies allow between 3.8 and 3.12.
- **Spark** and **JDK** Installation:

For the current amount of data used for the test it would have been more efficient to use Pandas instead of Spark, but for future scalability and the real case scenario, Spark is more future-proven for a larger amount of events.

Before installing the packages, you will need to specify the environment variables. Download Java from [here](https://www.oracle.com/es/java/technologies/javase/jdk11-archive-downloads.html). 

In the case of using Mac, you can download it directly using *brew*:

```shell
brew install openjdk@11
```

After downloading and installing the JDK you need to set the JAVA_HOME variable.
    - **Windows**:
    You will have to open the Environment variables in the Control Panel, and then create a new User Variable as shown in the image:

<p align="center">
  <img src="https://i.ibb.co/1dbPjv2/Screenshot-1.jpg" alt="Environment variables"/>
</p>

Afterwards, you will have to add it to the PATH:
<p align="center">
  <img src="https://i.ibb.co/QkqXWgT/Screenshot-2.jpg" alt="PATH"/>
</p>

  - **Linux and Mac**:

You just need to run the following command on the terminal:

```shell
export JAVA_HOME = {path to the java JDK}
```

Also, you will have to download Spark from [here](https://dlcdn.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz). 

The version used on this project is 3.5.0 and Hadoop 3.3. After downloading it, extract it to your preferred location, this will be your *SPARK_HOME*. Now you have to set up the environment variable following the same steps as with the JDK.

The same path must be used for *HADOOP_HOME*.

If you are using **Windows**  , for future troubleshooting you may need to download *winutils.exe*, you can download it from [here](https://github.com/kontext-tech/winutils/tree/master/hadoop-3.3.0/bin). Place this file in the %SPARK_HOME%\bin folder.

### Installing dependencies:
First, you need to install Poetry, assuming that you already have installed Python.

```shell
pip install poetry
```

Then, navigate to the project folder and execute the following command:

```shell
 poetry install
 ```
 
 After the dependency installation is completed, select the created virtual environment as your *Python Interpreter* for developing and testing.
