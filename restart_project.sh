echo "do restart host project in 154"

echo "start op-rc"
docker start op-rc

echo "start op-mc"
docker start op-mc

echo "start op-order"
docker stop op-order
docker rm op-order
docker run -d --name op-order -p 7002:80 -v /data/orderProject:/data/orderProject xutaomac/cp:v3 /bin/sh -c 'cd /data/orderProject/order/bin/; sh run-op.sh'

echo "start op-billing"
docker stop op-billing
docker run -d --name op-billing -p 7001:80 -v /data/BillingManagementSystem:/data/BillingManagementSystem xutaomac/cp:v3 /bin/sh -c 'cd /data/BillingManagementSystem; sh run.sh'

echo "start op-pro"
docker stop op-pro
docker run -d --name op-pro -p 7003:80 -v /data/productProject/:/data/productProject/ xutaomac/cp:v3 /bin/sh -c 'cd /data/productProject/product/bin/; sh run.sh'

echo "check it"
docker ps


echo "health check"
echo "op-billing ...."
curl 127.0.0.1:7001/health/
echo "op-order"
curl 127.0.0.1:7002/health/
echo "op-pro"
curl 127.0.0.1:7003/health/
echo "core b"
curl 127.0.0.1:9001/health/
echo "core db proxy"
curl 127.0.0.1:9999/health/