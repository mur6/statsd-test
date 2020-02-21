FROM alpine
RUN apk -U add socat
CMD while true; do socat UDP-RECVFROM:8125 STDOUT; echo; done
