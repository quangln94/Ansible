# group_vars.md

`group_vars` sẽ ghi đề toàn bộ giá trị trong `group`.

Ví dụ trong file `inventory` như sau:
```sh
[solr]
nyc1.hostedapachesolr.com
nyc2.hostedapachesolr.com
jap1.hostedapachesolr.com

[log]
log.hostedapachesolr.com
```

Ví dụ trong file `/group_vars/solr`
```sh
---
do_something_amazing=true
foo=bar
```
Các giá trì này sẽ được ghi đè cho toàn bộ `host` trong `group`:`[solr]`
