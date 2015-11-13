# fio-graphite
Take json output from fio and convert/ship metrics to a graphite ( carbon-cache) instance.

#Example

``fio --name=random-writers --ioengine=libaio --iodepth=4 --rw=randwrite --bs=32k --direct=0 --size=100M --numjobs=5 --output-format=json | ./fio-graphite.py``
