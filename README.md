
A Docker image running Ubuntu:trusty with latest Python 3.5 and latest FFMPEG (built from source)

### To Build

~~~~
docker build -t <imageName> .
~~~~

### To pull and run from hub.docker.com

Docker Hub: https://registry.hub.docker.com/u/dkarchmervue/ffmpeg/

Source and example: https://github.com/ampervue/docker-ffmpeg

~~~~
docker pull dkarchmervue/ffmpeg
docker run --rm -ti dkarchmervue/ffmpeg ffmpeg -version
docker run --rm -ti -v ${PWD}:/work dkarchmervue/ffmpeg ffmpeg -i video.mp4 ...
docker run --rm -ti -v ${PWD}:/work dkarchmervue/ffmpeg python your-python-script.py
docker run --rm -ti dkarchmervue/ffmpeg bash
~~~~

## Example

As an example, the python script uses FFMPEG to download a movie from the web and create a 100x100 thumbnail

~~~~
# Pull image
docker pull dkarchmervue/ffmpeg

# Get example files and build new image
git clone https://github.com/ampervue/docker-ffmpeg
cd example
docker build -t thumbnail .
docker run --rm -ti thumbnail --input http://techslides.com/demos/sample-videos/small.mp4

# Mount current directory on container so that file can be written back to host
docker run --rm -ti -v ${PWD}:/code thumbnail --file http://techslides.com/demos/sample-videos/small.mp4
ls thumbnail.jpg
open thumbnail.jpg
~~~~

## Python 2.7

For Python 2.7, use https://github.com/ampervue/docker-python27-ffmpeg