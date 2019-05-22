# Pemrograman Jaringan
Final Project Pemrograman Jaringan
Apache benchmarking

## How to use
### Case 1 (Async No LB)
* run py2 async_server.py 9001
* run Curl Get, Post, Head and Option
* run ab -n [Banyak Request] -c [Banyak Konkurensi] http://127.0.0.1:9001/ >> [output filename]

### Case 2 (Async With LB)
* run py2 lb.py
* run py2 async_server.py 9001 until 9005
* run Curl Get, Post, Head and Option
* run ab -n [Banyak Request] -c [Banyak Konkurensi] http://127.0.0.1:8885/ >> [output filename]

### Case 3 (Thread No LB)
* run py2 aserver_thread_http.py 9001
* run Curl Get, Post, Head and Option
* run ab -n [Banyak Request] -c [Banyak Konkurensi] http://127.0.0.1:9001/ >> [output filename]

### Case 4 (Thread With LB)
* run py2 lb.py
* run py2 aserver_thread_http.py 9001
* run Curl Get, Post, Head and Option
* run ab -n [Banyak Request] -c [Banyak Konkurensi] http://127.0.0.1:8885/ >> [output filename]

