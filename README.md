# Radar
SRR 208 Short Range Radar Sensor with linux
at first make sure you have installed both
canutils

cantools
https://cantools.readthedocs.io/en/latest/#the-monitor-subcommand


for the full tutorial
https://sgframework.readthedocs.io/en/latest/cantutorial.html


test by making virtual can bus
$ modprobe vcan
$ sudo ip link add dev vcan0 type vcan
$ sudo ip link set up vcan0


start playing
 candump vcan0

in another terminal
cansend vcan0 01a#11223344AABBCCDD
