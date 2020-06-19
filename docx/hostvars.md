Để xem các thông tin về biến:
```sh
- debug: var=ansible_facts
```

`hostvars`: cho phép access biến cho host khác bao gồm cả `facts` đã được thu thập ở host đó.
```sh
{{ hostvars['test.example.com']['ansible_facts']['distribution'] }}
```
`groups` là danh sách tất cả các `groups` (và hosts) trong inventory. Được sử dụng để liệt kê tất cả các host trong `groups`:
```sh
{% for host in groups['app_servers'] %}
   # something that applies to all app servers.
{% endfor %}
```
1 ví dụ được sử dụng để tìm tất cả các Ip trong group.
```sh
{% for host in groups['app_servers'] %}
   {{ hostvars[host]['ansible_facts']['eth0']['ipv4']['address'] }}
{% endfor %}
```
`group_names` là danh sách tất cả các `group` mà host hiện tại đang ở.

`inventory_hostname`: là tên của `hostname` được cấu hình trong file `inventory`. Tên này có thể khác tên `hostname` được lấy từ `ansible_hostname`.

`inventory_hostname_short`: ví dụ sử dụng `inventory_hostname_short`
```sh
ansible.com.vn

=> ansibe
```
