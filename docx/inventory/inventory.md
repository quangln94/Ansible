# Inventory

Định nghĩa các host sẽ được thực thi bới ansible


- Định nghĩa theo group
```sh
[webserver]
web01
web01
web01
```
Để chạy playbook cho tất cả các host trên thì khai báo như sau:
```sh
- hosts: webserver
```
Sử dụng command check RAM trên tất cả cá host
```sh
ansible webserver -a "free -m"
```
- Chỉ định biến cho `group`
```sh
[servercheck-web]
www1.servercheck.in
www2.servercheck.in

# Chỉ định biến được áp dụng cho group [servercheck-web]
[servercheck-web:vars]
ansible_ssh_user=servercheck_svc

[servercheck-db]
db1.servercheck.in

[servercheck-log]
log.servercheck.in

[servercheck-backup]
backup.servercheck.in

[servercheck-nodejs]
atl1.servercheck.in
atl2.servercheck.in
nyc1.servercheck.in
nyc2.servercheck.in
nyc3.servercheck.in
ned1.servercheck.in
ned2.servercheck.in

# Chỉ định biến được áp dụng cho group [servercheck-nodejs]
[servercheck-nodejs:vars]
ansible_ssh_user=servercheck_svc
foo=bar
```
- Khai báo các server cùng loại, vd như `centos` hoặc `ubuntu`
```sh
[centos:children]
servercheck-web
servercheck-db
servercheck-nodejs
servercheck-backup

[ubuntu:children]
servercheck-log
```
Thực thi lệnh trên tất cả các host
```sh
ansible centos -m yum -a "name=bash state=latest"
```

## Inventory variables
```sh
[www]
www1.example.com ansible_ssh_user=johndoe
www2.example.com

[db]
db1.example.com
db2.example.com

[db:vars]
ansible_ssh_port=5222
database_performance_mode=true
```
