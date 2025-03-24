import requests
import json
import os




# Define the URL of the API endpoint
url = "http://localhost:5000/tailor_resume"


# Sample data to send in the request payload
payload = {
    "resume": ("""
SHAFEE IBNA AMIN
Senior Data Engineering Consultant
Location: Manassas, Va, United States of America
________________________________________

Professional Biography
 
Driven by a passion for innovation and over a decade of expertise, Shafee specializes in data analysis, transformation, developing advanced machine learning models and scalable cloud-based solutions. His work spans leading platforms like Snowflake, AWS, Azure, Databricks, and Tableau, delivering impactful results through end-to-end data engineering and MLOps pipelines. Shafee has led and delivered transformative projects, including large-scale data migrations to Snowflake, deploying AI-driven systems for insurance predictions, data analysis, and building cloud-native microservices on AWS. By leveraging tools like Tableau for analytics and automation, he is able to bridge cutting-edge technology with actionable insights to solve complex challenges and drive success.  

Skills Summary

Cloud Platforms: AWS (EC2, S3, RDS, ECS), Azure (App Services, Functions, SQL Database, Cosmos DB, Machine Learning), GCP (GCE, GCS, GAE, GKE, CloudSQL, Cloud Functions)
Infrastructure as Code (IaC): Terraform, Ansible, CloudFormation
Orchestration & Containerization: Kubernetes, Docker, Helm
CI/CD Tools: Jenkins, Azure DevOps, GitHub Actions

Data Processing & Engineering: Apache Spark, Databricks, PySpark, Snowflake, Informatica
Workflow Orchestration: Airflow, Luigi, Azure Data Factory
MLOps Platforms: Azure ML Studio, MLflow, Kubeflow, Databricks
Model Deployment: Azure Container Instances, AWS SageMaker, Databricks

Backend Development: Python, Java, C#, .NET
Frontend Development: JavaScript (React, Angular), HTML, CSS
Data Science & Machine Learning: Python (pandas, NumPy, scikit-learn), PySpark

Relational Databases: PostgreSQL, MySQL, SQL Server, Oracle
NoSQL Databases: MongoDB, Cassandra, Cosmos DB
Cloud Data Warehouses: Snowflake, Redshift
Data Lakes & Storage: Azure Data Lake Storage, AWS S3, Databricks Delta Lake

API Design: REST, GraphQL, Flask, Django, Gunicorn, Tornado, .NET
Testing: Unit Testing, Integration Testing, Selenium
Version Control: Git (GitHub, GitLab, Bitbucket)
Methodologies: Agile (Scrum, Kanban), Waterfall, Test-Driven Development (TDD)

________________________________________

Highlights
 
•	Skilled in designing and delivering tailored solutions to address diverse business use cases.
•	Successfully implemented multiple machine learning solutions on leading cloud platforms for enterprise-scale projects.
•	Strong understanding of data requirements and the context in which data is used in the business and 
regulatory settings 
•	Possesses the ability to find pragmatic solutions to complex data problems through analysis and data integration and mapping while ensuring the reservation of Data Lineage with proper governance. 
•	Led and coordinated teams of data engineers and data scientists, ensuring seamless project execution and delivery.
•	Partnered with stakeholders across client teams, including Distribution, Operations, and CTO offices, to align technical solutions with business objectives.
•	Effectively managed onshore and offshore teams to drive collaborative success in dynamic, multi-geographic environments.
________________________________________
 


Key Experiences



Senior Data Engineer - NTT DATA – Primrose Schools
September 2024 – Present
•	Managed data integration and automation projects with Databricks, Python, and Tableau, optimizing workflows and improving data-driven decision-making.
•	Developed and maintained a Databricks warehouse for streamlined data processing and analysis.
•	Designed efficient ETL pipelines to integrate data from multiple vendors into a centralized system.
•	Automated daily workflows using Python, significantly improving operational efficiency.
•	Built Databricks workflows and custom applications to automate Tableau extract and datasource refreshes via SQL Server Agent.
•	Utilized Jira for effective task management and tracking individual performance improvements.
•	Migrated SQL Server jobs as databricks Workflows
•	Used Azure devops tools in databricks to introduce version control in databricks as data-ops practice

Senior Data Engineer - NTT DATA – Blue Cross Blue Shield
Feb 2024 – July 2024
•	Served as a Data Migration Automation Specialist, leading a team to migrate over 600 complex stored procedures and a live database of over 70TB from Teradata to Snowflake. 
•	Continuation of previous project
•	Engineered Restful Microservices using Flask and Django, deploying them on AWS servers via EBS and EC2. 
•	Streamlined daily tasks through Python scripting automation. 
•	Leveraged Jira for task management and individual performance enhancement. 
•	Designed and developed user interfaces using HTML, XHTML, AJAX, CSS, JavaScript, and Bootstrap. 
•	Orchestrated the deployment of Restful Microservices using Flask and Django on AWS servers. 
•	Created tools to ensure data lineage is maintained during daily transformation workflows

MLops Lead – NTT DATA – National Life Group
Sep 2023 - Feb 2024 
•	Developed Machine Learning models and AI applications for insurance predictions. 
•	MLOps and Data Management: Implement MLOps on the Databricks platform, set up Databricks environments, use Git for version control, store data in a lakehouse architecture using Databricks Delta tables, develop features and models, integrate CI/CD practices, and explore advanced MLOps techniques. 
•	Infrastructure and Production Systems: Design data pipelines and infrastructure on Databricks, develop real ML production systems using Databricks and deploy scalable ML tools and services on Databricks. 
•	Implemented data governance and lineage tracking methodologies on machine learning datasets. 

Data Engineering Consultant – NTT DATA – Leafhomes
Sep 2023 - Oct 2023
•	Contributed to building database models, APIs, and views using Python for interactive web-based solutions. 
•	Employed advanced Python packages like NumPy and SciPy for complex numerical and scientific calculations. 
•	Developed Python batch processors for data consumption and production. 
•	Employed agile methodology for the analysis, specification, design, implementation, and testing phases of the Software Development Life Cycle (SDLC). 
•	Containerized and deployed ETL and REST services on AWS ECS via CI/CD Jenkins pipelines. 
•	Contributed to major development initiatives involving Python, Django, R, MySQL, MongoDB, jQuery, and react. 


Senior Data Engineer - NTT DATA – Blue Cross Blue Shield
Nov 2022 - Sep 2023
•	Served as a Data Migration Automation Specialist, leading a team to migrate over 600 complex stored procedures and a live database of over 70TB from Teradata to Snowflake. 
•	Collaborated with Onshore and Offshore teams to seamlessly integrate and enhance workflow. 
•	Created multiple automation tools with Python for data migration and verification. 
•	Addressed daily Data Migration environment-related issues. 
•	Developed servers and user interfaces for data migration tools to facilitate on-demand table verification and migration. 
•	Leveraged Abinitio and ETL tools for the migration of large, complex datasets. 
•	Coordinated data migration for thousands of tables simultaneously across multiple EC2 instances using Parallel Processing. 
•	Improved the performance of legacy programs through code refactoring. 
•	Created real-time applications that leveraged data from three different databases (Oracle, Teradata, and Snowflake), applying scientific calculations for data transformation. 
•	Developed an application to convert Teradata BTEQ to SnowSQL. 


ML Lead Consultant, EY COACH – NTT Data - Ernst & Young
June 2021 - Nov 2022 
•	Created a Machine Learning engine for an LLM based Learning Management System to train people for effective communication.
•	Developed end-to-end MLops pipelines using Azure ML Studio and Azure DevOps. 
•	Utilized CosmosDB with MongoDB API for dynamic data storage, seamlessly integrated with AI. 
•	Engineered data pipelines using Azure SQL tools to facilitate data synchronization across environments for ML model training. 
•	Orchestrated multiple data pipelines in Python to harmoniously generate datasets for ML model training and development. 
•	Designed and deployed APIs from ML models using FastAPI and AzureML, containerizing them for scalability. 
•	Orchestrated the deployment of ML containers to Kubernetes from AzureML Studio using MLpipelines. 
•	Designed and implemented micro-services and communication protocols using Service Bus and Azure Logic Apps. 
•	Innovated an AI comparison tool to evaluate performance variations in dialect and accent among leading Cloud AI-based Speech to Text services. 
•	Managed Kubernetes clusters and networking for multiple APIs deployed within containers. 
•	Maintained an up-to-date code base, libraries, and dependencies to ensure compliance with enterprise Aquasec and WhiteSource security standards and threat prevention. 
•	Created a complex automation pipeline integrating Azure DevOps, Kubernetes, Azure Logic Apps, and Azure Machine Learning Studio. 
•	Established an NLP as a service platform. 
•	Developed data models for applications, metadata tables, views, and related database structures. 
•	Led the whole data engineering process from inception to model training and retraining while ensuring data lineage is intact. 




Data Engineering Consultant, Top Record Label Company 
March 2021 - June 2021, New York  
•	Crafted a robust data migration platform to facilitate efficient data migration. 
•	Designed and implemented a seamless data migration bridge between MS-SQL DB and MySQL for a web application, ensuring smooth data transfer. 
•	Developed data verification tools to meticulously validate data accuracy, ensuring the integrity of the migrated information. 
•	Successfully migrated an onsite SQL database to the Azure Cloud, enhancing accessibility, scalability, and security. 

Software Development Consultant - RSRIT
June 2014 - March 2021	
•	Participated in numerous consultant roles to develop multiple solutions for different clients
•	Led the architecture, development, and issue resolution of server modules, focusing on back-end development using Python and Django, and front-end applications using React, Webpack, Redux, ES6/7, and PostgreSQL. 
•	Collaborated with GIT for version control while constructing front-end and back-end modules using Python on the Django Web Framework. 
•	Designed and developed ETL software for DB2 columnar database fact and dimension tables. 
•	Resolved issues, enhanced server modules, and led back-end and front-end development efforts using Python, Django, React, Webpack, Redux, ES6/7, and PostgreSQL. 
•	Designed user-friendly website interfaces using Python and Django's view controller and templating language. 
•	Developed a WordPress property finder plugin for a notable UK-based Real Estate company. 
•	Implemented performance enhancement techniques like index optimization and shared keys to improve efficiency. 
•	Created a Customer Loyalty and Bonus application in Android Studio, integrated with POS systems, and utilized SQLite for local storage and synchronized data with MySQL in the cloud. 
•	Utilized HTML, Bootstrap, and PHP to craft complete front-end and back-end components for web applications. 
•	Wrote and executed SQL queries across various databases such as MySQL, SQL Server, and Teradata. 
•	Played a crucial role in developing Web Services using SOAP for the transmission and retrieval of data in XML format. 
•	Designed, tested, and implemented numerous dashboard features, utilizing Python, Java, Bootstrap, CSS, JavaScript, and jQuery. 
•	Developed various forms for data recording in online user interfaces. 
•	Created multiple database I/O applications using Python, Java, and PHP, allowing dynamic DML and DDL based on user inputs. 
•	Implemented PHP as an embedded scripting language for front-end web development. 
•	Designed data models for various applications, including metadata tables, views, and related database structures.
    """
    ),
    "job_description": (
        """
About the job
This is a condensed Job Description.



The Electrical & Instrumentation (E&I) Engineer leads the scope definition and Engineering Quality Assurance effort for the Electrical & Instrumentation component of the scope of work and ensures the design meets the Business and Project Objectives. The E&I Engineer works with the other discipline engineering leads to define the scope of work for the project and ensures the project design meets industry and Company specifications. The E&I Engineer functionally reports to the Engineering Manager.



The Project E&I Engineer Lead supports the development of alternative process designs during the Opportunity Evaluation and Selection Phases and leads the E&I design definition effort through the Definition, Execution and Start‐Up Phases.



Education/Experience

•Bachelor’s Degree in Electrical Engineering required

•Min. 10 years of experience working in petrochemical/refining as E&I discipline.

Skills/Competencies

•Candidate will be well versed in industry codes, standards, and requirements (NEC,ANSI/IEEE, and ISA).

•Proficient with reading one line diagrams, cable schedules, loop sheets and P&ID’s.

•Proficient with use of SKM PowerTools or ETAP for evaluation of load flows, short circuit protection schemes, stability studies.

•Experience working stage gate capital project process on owner side.

•Knowledge of requirements for testing and commissioning of electrical equipment.

•Experience with design of solar farms and associated equipment (inverters and PV modules) a plus.

•Experience with power distribution centers and associated equipment (transformers, MCC’s, switchgear)

•Experience with high voltage transmission, substations and switch yard designs.

•Experience with Honeywell and Rosemount products (transmitters, flow and level instruments, etc.)

•Experience with Fisher control valves and sizing calculations.

•Experience applying engineering standards and specifications on capital projects
        """
    )
}

# Define headers to indicate that we're sending JSON data
headers = {"Content-Type": "application/json"}

# Send the POST request
response = requests.post(url, json=payload, headers=headers)
# Check and print the response from the server
if response.ok:
    result = response.json()
    print("Tailored Resume:")
    print(result.get("tailored_resume", "No tailored resume found in response."))
else:
    print("Error:", response.status_code, response.text)
