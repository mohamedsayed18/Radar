# Radar
SRR 208 Short Range Radar Sensor with linux<br/>


### Installation
First install<br/>
[canutils](https://github.com/linux-can/can-utils)<br/>
[cantools](https://cantools.readthedocs.io/en/latest/#the-monitor-subcommand)<br/>

### Tutorial
Test by making virtual can bus<br/>
`modprobe vcan`<br/>
`sudo ip link add dev vcan0 type vcan`<br/>
`sudo ip link set up vcan0`<br/>

Start playing<br/>
`candump vcan0`<br/>

in another terminal<br/>
`cansend vcan0 01a#11223344AABBCCDD`<br/>

test by making virtual can bus
`modprobe vcan`
`sudo ip link add dev vcan0 type vcan`
`sudo ip link set up vcan0`


start playing
 candump vcan0

in another terminal
cansend vcan0 01a#11223344AABBCCDD

generate random messages to our can bus<br/>
cangen vcan0 -v<br/>

let's record our reading
candump -l vcan0<br/>

read our file in friendly format<br/>
log2asc -I candump-2015-03-20_123001.log vcan0<br/>

play our file on the bus<br/>
log2asc -I candump-2015-03-20_123001.log vcan0<br/>


[for the full tutorial](https://sgframework.readthedocs.io/en/latest/cantutorial.html) <br/>
