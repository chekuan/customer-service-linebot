# customer-service-linebot



## 系統方面
我們使用 Django 作為我們的 bot backend, 然後利用 redis-server 作為 user state 的追蹤機制。
目前是使用 ngrok 來介接 https 當作 webhook。實際 deploy 的時候，要使用 TLS 憑證。
