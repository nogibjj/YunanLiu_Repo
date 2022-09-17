[![Python application test with Github Actions](https://github.com/nogibjj/YunanLiu_Repo/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/YunanLiu_Repo/actions/workflows/main.yml)




# YunanLiu_Repo
This is a repository of Yunan Liu

## Week two (just enrolled)
* Added workflow to readme
* Setup CodeSpace
* Learnt to create virtual machine in codespace, wrote Makefile and requirements.txt
* Learnt to use lint to check the quality of the code
* Start learning Panda API

## Week Three
* Databricks: https://docs.databricks.com/dev-tools/python-sql-connector.html#id6 (Query Data, Insert Data, etc.)

# Project 1 Demo
* Setup Makefile for lint and module/package install
* Create requirements.txt file for make install to reference
* Create querydb.py file to make connection to the Azure databricks
    * Stored the databricks cluster info in Github secrets and through calling os.getenv"name" to get those cluster info
    * Printed the first two lines of the table in databricks to check the connection

![queryScreenshot](images/Screen%20Shot%202022-09-17%20at%205.26.13%20PM.png)
![querycheckScreenshot](images/Screen%20Shot%202022-09-17%20at%205.41.06%20PM.png)

* Create fastApi_app.py for fastapi application
* Create query_sql_db.py for CLI demo

![fastApiScreenshot](images/Screen%20Shot%202022-09-17%20at%205.44.38%20PM.png)
![fastApiDemoScreenshot](images/Screen%20Shot%202022-09-17%20at%205.47.02%20PM.png)

![CLIScreenshot](images/Screen%20Shot%202022-09-17%20at%205.44.53%20PM.png)
![CLIDemoScreenshot](images/Screen%20Shot%202022-09-17%20at%205.49.37%20PM.png)