curl -L  https://github.com/coreos/etcd/releases/download/v2.0.0/etcd-v2.0.0-linux-amd64.tar.gz -o etcd-v2.0.0-linux-amd64.tar.gz
tar xzvf etcd-v2.0.0-linux-amd64.tar.gz
cd etcd-v2.0.0-linux-amd64
mkdir /opt/bin
cp etcd* /opt/bin
