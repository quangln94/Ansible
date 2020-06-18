# HANDLERS

Được gọi thông qua option `notify` khi `tasks` thực thi. Ví dụ:
```sh
handlers:
- name: restart apache
  service: name=apache2 state=restarted
```
Có thể đặt `handlers` trong file `/ansible/roles/handlers/main.yml` như sau:
```sh
---
- name: restart apache
command: service apache2 restart
```
