## ex00

```bash
python3 ex00/fight.py
```

## ex01

### run server
```bash
python3 ex01/server.py
```
### client
```bash
 python3 ex01/crawl.py \
 http://21-school.ru/ http://21-school.ru/qwerty/ \
 http://yandex.ru/qwerty/ http://example.com/old-page/
 
```

## ex02

### run server
```bash
python3 ex02/server_cached.py
```
### client
```bash
 python3 ex01/crawl.py \
 http://21-school.ru/ http://21-school.ru/qwerty/ \
 http://yandex.ru/qwerty/ http://example.com/old-page/
```

### redis-cli
```bash
redis-cli -h localhost -p 6379
KEY *
HGETALL status
GET counter:yandex.ru
```
