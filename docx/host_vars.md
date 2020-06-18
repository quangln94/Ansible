# host_vars

`host_vars` sẽ ghi đè tất cả các giá trị của host

Ví dụ file `inventory` như sau:
```sh
[solr]
nyc1.hostedapachesolr.com
nyc2.hostedapachesolr.com
jap1.hostedapachesolr.com

[log]
log.hostedapachesolr.com
```
File `/host_vars/nyc1.hostedapachesolr.com` như sau:
```sh
---
tomcat_xmx: "1024m"
```
Giá trị này sẽ ghi đè tất cả các giá trị trong host `nyc1.hostedapachesolr.com`
