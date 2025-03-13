# **Air Pollution Monitoring System**  
[![AWS](https://img.shields.io/badge/AWS-Cloud-orange)](https://aws.amazon.com/)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4-green)](https://www.raspberrypi.org/)  

---

## **Project Overview**  
This project involves the development of an **Air Pollution Monitoring System** using **Raspberry Pi** and **AWS IoT services**. The system monitors air quality by measuring pollutants such as **CO**, **CO2**, and **AQI (Air Quality Index)**. When pollutant levels exceed predefined thresholds, the system sends **email notifications** to users via **AWS Simple Notification Service (SNS)**.  

---

## **Key Features**  
- **Real-Time Monitoring**: Collects air quality data using sensors connected to a Raspberry Pi.  
- **Cloud Integration**: Sends data to **AWS Lambda** for processing and storage.  
- **Email Notifications**: Sends alerts via **AWS SNS** when pollutant levels exceed thresholds.  
- **Scalable Architecture**: Uses **AWS IoT Core**, **Lambda**, and **SNS** for a robust and scalable solution.  

---

## **Technologies Used**  
- **Hardware**:  
  - Raspberry Pi 4  
  - Air quality sensors (CO, CO2, AQI)  
- **AWS Services**:  
  - **AWS IoT Core**: For device communication and data ingestion.  
  - **AWS Lambda**: For processing sensor data.  
  - **AWS SNS**: For sending email notifications.  
- **Programming Languages**:  
  - **Python**: For Raspberry Pi data collection and processing.  
  - **JavaScript (Node.js)**: For AWS Lambda function.  

---

## **Installation and Setup**  

### **1. Prerequisites**  
- **Raspberry Pi 4** with Raspbian OS installed.  
- **AWS Account** with access to IoT Core, Lambda, and SNS.  
- **Python 3.8+** installed on Raspberry Pi.  

### **2. Clone the Repository**  

git clone https://github.com/your-username/air-pollution-monitoring-system.git

cd air-pollution-monitoring-system  

---
## **Set Up AWS Resources**  

### **1. Create an SNS Topic**  
1. Go to the **AWS SNS Console**.  
2. Create a new topic (e.g., `air-pollution-alerts`).  
3. Subscribe your email to the topic.  

### **2. Create a Lambda Function**  
1. Go to the **AWS Lambda Console**.  
2. Create a new function with the code from `lambda.txt`.  
3. Set the environment variable `email` to your email address.  

### **3. Set Up AWS IoT Core**  
1. Register your Raspberry Pi as an IoT device.  
2. Configure the device to send data to the Lambda function.  


## **4. Run the Raspberry Pi Script**

**Install dependencies**:

pip install boto3 pynput requests 

**Run the script**:

python AirPollution-Notif.py  

---

## **Usage**

1. The Raspberry Pi collects air quality data and sends it to AWS IoT Core.

2. AWS Lambda processes the data and triggers SNS notifications if thresholds are exceeded.

3. Users receive email alerts with details about air quality levels.

---
## **Code Overview**

1. Raspberry Pi Script **(AirPollution-Notif.py)**

2. Simulates sensor data using keyboard inputs.

3. Sends data to AWS Lambda via an API Gateway endpoint.

4. AWS Lambda Function **(lambda.txt)**

5. Processes incoming data from the Raspberry Pi.

6. Publishes alerts to the SNS topic for email notifications.

---
## **Results**

**Real-Time Alerts**: Users receive email notifications when pollutant levels exceed thresholds.

**Data Visualization**: Air quality data is stored in AWS for further analysis.

---
## **References**  
- [AWS IoT Core Documentation](https://docs.aws.amazon.com/iot/)  
- [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)  
- [Project Video Presentation](https://drive.google.com/file/d/1IvAhDK74KHlWIBWlzYhdv7c28MJVJ8bM/view?usp=sharing)  
---
