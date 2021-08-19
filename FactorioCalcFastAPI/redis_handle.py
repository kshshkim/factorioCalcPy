from redis import Redis

REDIS_HOST = 'redistest'
REDIS_PORT = 16379
REDIS_DB = 0

rdc = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

