# coding: utf-8


def make_decrease_celery_app():
	from celery import Celery
	from kombu import Exchange, Queue

	app = Celery(
		"decrease",
		broker="redis://127.0.0.1:6379/1",
	)
	CELERY_TASK_SERIALIZER = "json"
	inventory_exchange = Exchange('promotion_decrease_inventory', type='direct')

	CELERY_QUEUES = (
		Queue('inventory', inventory_exchange, routing_key='decrease_inventory'),

	)

	CELERY_ROUTES = {
		'commodity.tasks.add_pink_doi.hello_world': {
			'queue': 'promotion_decrease_inventory',
			'routing_key': 'decrease_inventory'
		},
	}
	app.conf.update({"CELERY_QUEUES": CELERY_QUEUES})
	app.conf.update({"CELERY_ROUTES": CELERY_ROUTES})
	app.conf.update({"CELERY_TASK_SERIALIZER": CELERY_TASK_SERIALIZER})
	return app


def handle():
	app = make_decrease_celery_app()
	app.send_task(
		"commodity.tasks.add_pink_doi.hello_world",
		kwargs=dict(
				settlement_id=1,
	            commodity_promotion_number=[{"number": 1, "commodity_id": "10736", "promotion_id": 428}],
	            user_id=23727389273
			),
		result_cls=app.AsyncResult
	)
	app.close()


if __name__ == "__main__":
	handle()
