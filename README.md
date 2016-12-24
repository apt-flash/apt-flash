# apt-flash

### Introduction
 
apt-flash aka flash is a package management tool for debian systems.
It accepts the same arguments as `apt-get` and offers the following additional functionalities on top.

* Allows downloading files from multiple sources (http/ftp/torrent)
* Multiple connections per server (1-16)
* Non-blocking nature
  * Package downloads happen immediately.
  * All installation requests get queued up in cases of dpkg lock.


### How to use?

`sudo apt install aria2`

`aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all --rpc-secret=AptF1@sh --rpc-listen-port=6801`

`flash install <package name>`

