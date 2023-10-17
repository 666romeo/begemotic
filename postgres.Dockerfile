FROM postgis/postgis:14-master


RUN apt-get update && apt-get install -y \
    postgresql-server-dev-14 \
    cmake \
    gcc \
    make \
    git \
    curl \
    && apt-get clean


RUN curl -L https://cmake.org/files/v3.21/cmake-3.21.3-linux-x86_64.tar.gz -o cmake.tar.gz \
    && tar -xzf cmake.tar.gz --strip-components=1 -C /usr/local \
    && rm cmake.tar.gz

RUN git clone https://github.com/zachasme/h3-pg.git /tmp/h3-pg && \
    cd /tmp/h3-pg && \
    cmake -B build -DCMAKE_BUILD_TYPE=Release && \
    cmake --build build && \
    cmake --install build --component h3-pg && \
    cd / && rm -r /tmp/h3-pg

EXPOSE 5432

