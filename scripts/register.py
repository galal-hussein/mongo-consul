import argparse
import consul

parser = argparse.ArgumentParser(description='Register MongoDB with Consul agent..')
parser.add_argument('-mi','--mongo-ip',help='MongoDB Node IP Address', required=True)
parser.add_argument('-mh','--mongo-hostname',help='MongoDB Node Hostname', required=True)
parser.add_argument('-mr','--mongo-role',help='MongoDB Node Role', required=True)
parser.add_argument('-mp','--mongo-port',help='MongoDB Node port', required=True)
parser.add_argument('-ci','--consul-ip',help='Consul Agent IP Address', required=True)
parser.add_argument('-cp','--consul-port',help='Consul Agent Active Port', required=True)
args = parser.parse_args()
c = consul.Consul(host=args.consul_ip, port=args.consul_port, dc="dc1")

def register_mongo(ip, hostname, port, role):
    catalog = c.catalog
    dc = "dc1"
    service={"Service":"MongoDB", "ID":hostname, "Tags":[role], "Port":int(port)}
    check={"Node": hostname,"CheckID": "service:MongoDB","Name": "MongoDB health check","Notes": "MongoDB health check","Status": "passing","ServiceID": hostname}
    catalog.register(hostname,ip,service=service,check=check, dc=dc,)

def add_mongo_health_check(mongo_ip, mongo_port):
    check = c.Agent().Check()
    check.register("MongoDB Service", check_id="up", http="http://"+mongo_ip+":"+str(mongo_port), interval="10s", notes="Check The mongodb is up or not")


register_mongo(args.mongo_ip, args.mongo_hostname,args.mongo_port,args.mongo_role)
