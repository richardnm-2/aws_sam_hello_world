FROM public.ecr.aws/lambda/python:3.9

RUN yum install -y unzip && \
    curl -Lo "/tmp/chromedriver.zip" "https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip" && \
    unzip /tmp/chromedriver.zip -d /opt/

RUN yum install -y https://dl.google.com/linux/chrome/rpm/stable/x86_64/google-chrome-stable-107.0.5304.68-1.x86_64.rpm


COPY app.py requirements.txt ./

RUN python3.9 -m pip install -r requirements.txt -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
