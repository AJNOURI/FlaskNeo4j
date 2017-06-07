from py2neo import Graph, Node, Relationship, authenticate
from passlib.hash import bcrypt
from datetime import datetime
import uuid



authenticate("127.0.0.1:7474", "neo4j", "newneo4j")
graph = Graph("http://127.0.0.1:7474/db/data/")
