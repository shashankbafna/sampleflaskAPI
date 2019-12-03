FROM alpine:latest
ENV http_proxy http://genproxy.corp.amdocs.com:8080
ENV https_proxy http://genproxy.corp.amdocs.com:8080
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt --proxy=genproxy.corp.amdocs.com:8080
EXPOSE 9299
CMD [ "python3", "/app/RestApiSampleFlaskApp.py" ]
