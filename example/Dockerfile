FROM ampervue/ffmpeg

# https://github.com/ampervue/docker-ffmpeg

MAINTAINER David Karchmer <dkarchmer@gmail.com>

# ============================================================================
# As an example, the python script uses FFMPEG to download a movie from the web
# and create a 100x100 thumbnail
#
# ~~~~
# git clone https://github.com/ampervue/docker-ffmpeg
# cd example
# docker build -t thumbnail .
# docker run --rm -ti thumbnail --file http://techslides.com/demos/sample-videos/small.mp4
#
# # Mount current directory on container so that file can be written back to host
# docker run --rm -ti -v ${PWD}:/code thumbnail --file http://techslides.com/demos/sample-videos/small.mp4
# ls thumbnail.jpg
# open thumbnail.jpg
#
# # To run with bash
# docker run --entrypoint bash -ti thumbnail
# ~~~~
# ============================================================================

# Step 1: Install any Python packages
# ----------------------------------------

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

# Step 2: Copy Python script
# ----------------------------------------

ADD app /code/app

# Step 3: Configure entrypoint
# ----------------------------------------

CMD           ["-h"]
ENTRYPOINT    ["python", "app/script.py"]





