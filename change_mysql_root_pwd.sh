# 经常会有一些需求，比如刚刚安装 mysql 的时候，设置的 root 密码忘记了，需要修改，因此将该步骤记录下来

# 先暂停 mysql 服务, 实例为 ubuntu 下暂停 mysql 服务
service mysql stop

# 启动 mysql，并且不需要密码
sudo mysqld_safe --skip-grant-tables &

# 免密码登录 mysql
mysql -uroot

# 设置新的密码
use mysql;

update user set password=PASSWORD("yournewpassword") where User='root';

# 此为必须执行，不然之前的设置都无效
flush privileges;

quit

# 重新启动 mysql
