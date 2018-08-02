## how to run `no_op.py`

### install ansible

### install python3 (any version should work)

### install virtualenv

### create hosts file

in `hosts`

```
[rabbitmq]
rabbitmq host ip

[rabbitmq:vars]
redis_host=<redis host url>
subnet_mask=<subnet mask for allowed sources>

[celery]
celery worker host ip

[celery:vars]
celery_broker_url=<rabbitmq host url>
```

`<subnet mask for allowed sources>` should have format `ip/number`

`<rabbitmq host url>` should have format `pyamqp://guest@host[:port]//`

There can be multiple celery worker host ips.

### run playbook
```
ansible-playbook -i hosts -u <user_name> no_op.yaml
```

### create virtualenv with python3
```
virtualenv -p python3 venv
```

### install dependencies
```
source venv/bin/activate
pip install redis celery
```

### clone this repo

### set env
```
export CELERY_BROKER_URL=<rabbitmq host url>
```

### run test
```
cd <repo>
python run.py <redis_host> <redis_port> <redis_db> <number tasks>
```

If successful, total time is printed in seconds.

