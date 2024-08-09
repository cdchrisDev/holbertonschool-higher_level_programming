#import image
FROM alpine:latest
RUN apk add curl
VOLUME /data
COPY config.txt '/app/config.txt'
CMD ["sh", "-c", "echo 'Hello, Docker Volumes!' > /data/hello.txt && cat /data/hello.txt"]
