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

agent = consul.Consul(host=consul_ip, port=consul_port, dc="dc1")

def register_mongo(ip, hostname, port, role):
    catalog = agent.Catalog()
    dc = "dc1"
    service=dict()
    service["Service"] = "MongoDB"
    service["ID"] = hostname
    service["Tags"] = [role]
    service["Port"] = port
    catalog.register(hostname,ip,service=service,dc=dc)

register_mongo(args.mongo_ip, args.mongo_hostname,args.mongo_port,args.mongo_role)
