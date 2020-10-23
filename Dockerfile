FROM ubuntu:focal
LABEL maintainer "Kry9toN <dhimasbagusprayoga@gmail.com>"

# Indonesian timezone (GMT+7)	
ENV TZ=Asia/Jakarta
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Tidy-up
RUN apt-get update -qq && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y \
    wget python3 git apt-transport-https ca-certificates \
    python3-pip \
    && apt autoremove --yes

RUN git clone -b master https://github.com/Kry9toN/KryPtoN-API /home/kapi
WORKDIR /home/kapi

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]