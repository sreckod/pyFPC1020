# Python library for FPC1020 fingerprint sensor

This library is based on FPC1020 library for Arduino.

# How to connect
![pi3_schema]

# Pins
![fpc1020]


| NAME | I/O | DESCRIPTION |
| ------ | ------ | ------ |
| V-TOUCH | POWER | Power for finger detected funtion, 5V or 3.3V |
| TOUCH | OUTPUT | Output high (3.3V) when finger detected, otherwise output low |
| VCC | POWER | 5V power input |
| UART_TX | OUTPUT | Transmitter of TTL serial |
| UART_RX | INPUT | Receiver of TTL serial |
| GND | POWER | Power GND |

# Example
```sh
 ~$ python example.py
 ```
 
  [fpc1020]: https://raw.githubusercontent.com/sreckod/pyFPC1020/master/images/fpc1020_pins.jpg
  [pi3_schema]: https://raw.githubusercontent.com/sreckod/pyFPC1020/master/images/pi3_schema.jpg