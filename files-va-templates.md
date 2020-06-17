# Files và Teamplates
Copy Files trong folder `ansible/roles/files/`
```
- name: Copy configuration file to server directly.
  copy: >
    src=example.conf
    dest=/etc/myapp/example.conf
    mode=644
```
Copy Templates trong folder `ansible/roles/templates/` sử dụng tất cả các biến chạy trong `playbook` trước đó
```sh
- name: Copy configuration file to server using a template.
  template: >
    src=example.xml.j2
    dest=/etc/myapp/example.xml
    mode=644
```
