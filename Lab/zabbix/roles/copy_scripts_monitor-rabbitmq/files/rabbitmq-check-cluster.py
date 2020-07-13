#!/usr/bin/python

import commands

out = commands.getstatusoutput("sudo rabbitmqctl cluster_status")
begin = out[1].find('running_nodes')
end = out[1].find('cluster_name')

data = out[1][begin:end].strip("running_nodes,")
nodes = data[:-5].strip('[').strip(']').split(',')

print len(nodes)

