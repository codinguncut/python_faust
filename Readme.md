## Getting Started
1. [install docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce)
2. [install docker-compose](https://docs.docker.com/compose/install/#install-compose)
3. install python3.6 or above
    * `sudo apt-get install python3.6 python3.6-dev`
    * setup a virtualenv (`mkvirtualenv`, `pyvenv`, or similar)
4. install apt-get dependencies
    `sudo ./install_deps.sh`
6. install python dependencies
    `make`
    * for some reason dev dependencies are not installing properly
        with pip-sync ;(
    * if things are not working, feel free to run again:
        `pip install -r requirements.txt`
        `pip install -r requirements-dev.txt`
7. add `127.0.0.1        kafka` to `/etc/hosts`
    * if you are on a machine with a fixed IP, set that IP in
        `KAFKA_ADVERTISED_HOST_NAME`
    * alternatively try `network_mode: host` in docker-compose.yml
    * *ARGH*
8. download spacy model
    `python -m spacy download en`
    * alternative: `python -m spacy download en_core_web_lg`
        (or '_sm', '_md')
    * FIXME: can we download only parts?
        https://stackoverflow.com/a/41644953
        `python -m spacy.en.download parser`
11. copy `sample.env` to `.env` and edit


## Running
1. start kafka, zookeeper and mongodb
    `docker-compose up -d`
2. launch faust application
    `./run-faust.py`
