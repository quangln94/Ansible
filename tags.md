# TAGS

`tags` cho phép chỉ chạy hoặc không chạy `role` hoặc `task` cụ thể.

Có thể `tag` `roles`, `files`, `task`, hoặc `plays`. 
```sh
vim tags.yml
---
- hosts: webservers
  tags: deploy

  roles:
  - { role: tomcat, tags: ['tomcat', 'app'] }

  tasks:
   - name: Notify on completion.
     local_action:
       module: osx_say
       msg: "{{inventory_hostname}} is finished!"
       voice: Zarvox
     tags:
       - notifications
       - say

   - include: foo.yml
     tags: foo
```
- Chạy playbook với `role`:`tomcat` và `task`:`say`
```sh
$ ansible-playbook tags.yml --tags "tomcat,say"
```
- Chạy playbook bỏ qua `tag`:`notifications`
```sh
$ ansible-playbook tags.yml --skip-tags "notifications"
```
Muốn thêm nhiều `tags` sử dụng cấu trúc file `.yaml`
```sh
tags: ['one', 'two', 'three']
```
hoặc
```sh
tags:
- one
- two
- three
```


