#Project Title: Monitoring and Visualization of System performance 

Group Members:
• Enas Alnaseri
• Muhammed Bahar
• Naga Lakshmi Nimishakavi

# Project Time Line
https://github.com/Enas-787/digital-forensics-team-project/blob/main/documentation/Enas%20Alnaseri%20Timeline%20and%20Member%20Contribution.pdf


Our project title is Monitoring and Visualization of System Performance Using Python, Netdata and Grafana. The emphasis is on assessment of various methods for system monitoring and visualization. The central objective is to take and analyze how the behavior of system resources occurs using a few tools and then determine how efficient each tool is for generating information about the performance, processing and presentation.
To accomplish such a task, we will build an artificial-controlled test environment with our laptops and virtual machines. We want to use Python scripts using the psutil library that will gather data like CPU usage, memory usage, disk activity and network traffic. Netdata will be installed to allow for continuous real time monitoring and Grafana will be used as the visualization layer which will both connect to Netdata but also to export log files. For this, we will simulate resource stress like for example high CPU or memory use to possibly create realistic scenarios. This is to ensure we will be able to test without the need to go on to use malware samples and be sure the test will be safe.
The data that we will gather will include system metrics such as CPU percentage and memory usage and disk activity and network traffic. The system will also create logs which contain alerts for when thresholds of usage exceed. These metrics will be output to CSV files, and the alerts will be output into log files. The data will then be visualized through Grafana dashboards which will make it easier to interpret patterns and detect unusual behavior.
We expect that this project will confirm the proclamations and the dedications of dissimilar methods of monitoring. By combining Python and Netdata and Grafana we will demonstrate how raw logs can be turned into easily comprehensible and actionable insights. Our results will underscore what tools are best for detecting real time, and which tools are better for long term visualization and analysis. The result will be actionable recommendations which can help system administrators and IT teams with their monitoring practices.
