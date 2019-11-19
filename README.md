# Radar
SRR 208 Short Range Radar Sensor with linux<br/>
at first make sure you have installed both<br/>
### Installation
[canutils](https://github.com/linux-can/can-utils)<br/>
[cantools](https://cantools.readthedocs.io/en/latest/#the-monitor-subcommand)<br/>

[for the full tutorial](https://sgframework.readthedocs.io/en/latest/cantutorial.html) <br/>



Test by making virtual can bus
`modprobe vcan`<br/>
`sudo ip link add dev vcan0 type vcan`
`sudo ip link set up vcan0`
Start playing<br/>
`candump vcan0`<br/>
in another terminal
`cansend vcan0 01a#11223344AABBCCDD`
