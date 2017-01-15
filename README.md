# apt-flash

### Introduction
 
apt-flash aka flash is a package management tool for debian systems.
It's a python wrapper around apt tool, accepts the same arguments as `apt-get` and offers the following additional functionalities on top.

* Allows downloading files from multiple sources (http/ftp/torrent)
* Multiple connections per server (1-16)
* Non-blocking nature
  * Package downloads happen immediately irrespective of dpkg-lock and all installation requests get queued up.
  * Efficient use of network bandwidth and time using multiple mirrors.


### How to use?

`sudo apt install aria2`

`aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all --rpc-secret=AptF1@sh --rpc-listen-port=6801`

`flash install <package name>`

