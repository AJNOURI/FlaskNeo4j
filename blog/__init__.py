from .views import app
from .models import graph

# Create uniqueness constraint on node names, process names, service names
graph.data("CREATE CONSTRAINT ON (n:node) ASSERT n.name IS UNIQUE")
graph.data("CREATE CONSTRAINT ON (p:process) ASSERT p.name IS UNIQUE")
graph.data("CREATE CONSTRAINT ON (s:service) ASSERT s.name IS UNIQUE")