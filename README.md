# Neo4j 查询示例


# 基础信息
* Application Type:         Python-Web Application
* Web framework:            https://palletsprojects.com/p/flask/[Flask] (Micro-Webframework)
* Neo4j Database Connector: https://github.com/neo4j/neo4j-python-driver[Neo4j Python Driver] for Cypher https://neo4j.com/developer/python[Docs]
* Database:                 Neo4j-Server (4.x) with multi-database
* Frontend:                 jquery, bootstrap, https://d3js.org/[d3.js]

# 配制环境
```angular2html
virtualenv neo4j-movies
source neo4j-movies/bin/activate
pip install -r requirements.txt
```



# 下载neo4j软件
启动neo4j，新建project，新建database movies，启动DBMS，在Use Database处，选择movies数据库，运行示例向导，在neo4j的窗口运行，:play movies， 按照提示操作到导入数据步骤
创建movies用户，在Connected as处，点击：server user add，添加movies用户，密码也是moives

# 修改配置，注意NEO4J_URI是neo4j显示的页面
```angular2html
url = os.getenv("NEO4J_URI", "bolt://localhost:7687")
username = os.getenv("NEO4J_USER", "movies")
password = os.getenv("NEO4J_PASSWORD", "movies")
neo4jVersion = os.getenv("NEO4J_VERSION", "4")
database = os.getenv("NEO4J_DATABASE", "movies")
```
# 运行本项目
python movies.py


# 浏览页面，完成
http://127.0.0.1:8080/

