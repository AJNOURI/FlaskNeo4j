# FlaskNeo4j
Web App to manage a Neo4j database.


#### Start the virtualenv:
\~/code/FlaskNeo4j/VirtualEnvs$ source /home/ajn/code/FlaskNeo4j/VirtualEnvs/FlaskNeo4j/bin/activate

(FlaskNeo4j) ajn@~/code/FlaskNeo4j/VirtualEnvs$

#### Start Neo4j container mapped to the Neo4j data & log directories:
docker run \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=/Downloads/neo4j321/neo4j-community-3.2.1/data:/data \
    --volume=/Downloads/neo4j321/neo4j-community-3.2.1/logs:/logs \
    neo4j:3.0


docker start 21e9a94b35b3

