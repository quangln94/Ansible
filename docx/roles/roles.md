# ROLES

Bao gồm các playbook bên trong plkaybook khác

meta: Thoong tin meta cho roles được định nghĩa tại đây. ví dụ:
```sh
---
dependencies: []
```
List tất cả các `roles` phụ thuộc chạy trước khi chạy `roles` chính.

tasks: Chạy tasks

default: Chứa biến
vars: Chứa biến sẽ overwrite biến trong default
