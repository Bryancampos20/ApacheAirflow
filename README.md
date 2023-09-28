# Apache Airflow HelloWorld DAG

¡Hola a todos! 👋

My name is Bryan Campos Castro, and I am a computer engineer currently working as a full-stack developer.

## About the Project

This project demonstrates how to create a simple workflow using Apache Airflow. The workflow consists of three tasks: a start task **(Start_task)**, a task that prints "Hello, world!" to the console **(Hello_task)**, and an end task **(End_task)**.

## Requirements

Before running this workflow, make sure you have the following requirements installed:

- **Docker**
- **Python**

## How It Works

1. **Task Definition:** In the helloWorld.py script, we define the three tasks (Start_task, Hello_task, End_task) and their relationship.
2. **Default Argument Configuration:** Default arguments for the DAG are configured, including the owner, start date, number of retries, and retry delay.
3. **DAG Creation:** The DAG object named hello_world is created using the default arguments, and the previously defined tasks are added to the DAG.
4. **Task Relationship Definition:** We use the >> operator to define the relationship between tasks. In this case, Start_task is scheduled to run before both Hello_task and End_task.
5. **Execution:** Once the DAG is configured, you can trigger the workflow execution from the Apache Airflow web UI.

## Execution

1. Download the file containing the foundation for running Apache Airflow in Docker from this link: https://github.com/puckel/docker-airflow.
2. After installing Apache Airflow in your project by running the following command:
```bash
docker pull puckel/docker-airflow
```
3. Start the containers using the following command:
```bash
docker-compose -f docker-compose-LocalExecutor.yml up -d
```
4. This way, you will have Airflow running on port 8080.

## Results


This is the dashboard where you can see the DAG before it is executed.

![Screenshot (160)](https://github.com/Bryancampos20/ApacheAirflow/blob/main/results/dashboard.png)

This is the graphical view where we can see that it executed successfully.

![Screenshot (160)](https://github.com/Bryancampos20/ApacheAirflow/blob/main/results/graph.png)

These are the logs for (Hello_task).

![Screenshot (160)](https://github.com/Bryancampos20/ApacheAirflow/blob/main/results/logs.png)

Finally, this is the dashboard view after it has executed successfully.

![Screenshot (160)](https://github.com/Bryancampos20/ApacheAirflow/blob/main/results/result.png)

This is a basic example of how we can run a HelloWorld in Apache Airflow.

Happy coding! 🚀
