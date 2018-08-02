### install ansible

### install python3 (any version should work)

### install virtualenv

### create hosts file

in `hosts`

```
[rabbitmq]
rabbitmq host

[rabbitmq:vars]
redis_host=<redis host url>
subnet_mask=<subnet mask for allowed sources>

[celery]
celery worker host

[celery:vars]
celery_broker_url=<rabbitmq host url>
```

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
after cloning

```
cd <repo>
```

### set env
```
export CELERY_BROKER_URL=<rabbitmq host url>
```

### run test
```
python run.py <redis_host> <redis_port> <redis_db> <number tasks>
```

If successful, total time is printed in seconds.

