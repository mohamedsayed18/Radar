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


generate random messages to our can bus<br/>
`cangen vcan0 -v`<br/>

let's record our reading<br/>
`candump -l vcan0`<br/>

read our file in friendly format<br/>
`log2asc -I candump-2019-11-20_202023.log vcan0`<br/>

play our file on the bus<br/>
`canplayer -I candump-2019-11-20_202023.log`<br/>


[for the full tutorial](https://sgframework.readthedocs.io/en/latest/cantutorial.html) <br/>
