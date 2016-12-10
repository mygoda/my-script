echo "install wget"
yum install wget
echo "install pip"
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
echo "install docker compose"

pip install docker-compose
