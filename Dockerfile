FROM python:3.13.4-bookworm

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NOWARNINGS=yes

RUN set -ex; \
    apt-get -y update; \
    apt-get -y upgrade; \
    apt-get -y install --no-install-recommends \
    sudo python3-pip

RUN pip install flask jpholiday requests beautifulsoup4

# don't forget in production
RUN apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*


ARG USERNAME=vscode
ARG USER_UID=1001
ARG USER_GID=$USER_UID
RUN set -eux; \
    groupadd --gid $USER_GID $USERNAME;  \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME; \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME; \
    chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME
WORKDIR /home/$USERNAME