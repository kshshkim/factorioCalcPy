from redis import Redis

REDIS_HOST = '172.18.0.1'
REDIS_PORT = 16379
REDIS_DB = 0

rdc = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

