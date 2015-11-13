# fio-graphite
Take json output from fio and convert/ship metrics to a graphite instance.

## Environment Variables
* CARBON_HOST
* CARBON_PORT
* METRICS_PREFIX 

## Example Usage
``fio --name=fio-graphite --rw=readwrite --size=100M --output-format=json | ./fio-graphite.py``

## TODO
* Stream JSON from fio using --status-interval
* Use graphitesend for shiping 
