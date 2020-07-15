import chessengine
from layers import layer
from net import net
network = net(1)
network.bind(layer({"ws": {"kaki"}, "b":10}, "input"), layer({"ws": {"poop"}, "b":2}, "output"))