import pytest
from app.api.models import WorkIn, WorkOut

workers = WorkIn(
    name='Юлия Иванова',
    phone='+7143658769',
    pay='10000',
    genre='Женщина'
)


def test_create_client(workers: WorkIn = workers):
    assert dict(workers) == {'name': workers.name,
                              'phone': workers.phone,
                              'pay': workers.pay,
                              'genre': workers.genre
                              }


def test_update_client_age(workers: WorkIn = workers):
    workers_upd = WorkOut(
        name='Юлия Иванова',
        phone='+7143658769',
        pay='10000',
        genre='Женщина',
        id=1
    )
    assert dict(workers_upd) == {'name': workers.name,
                              'phone': workers.phone,
                              'pay': workers.pay,
                              'genre': workers.genre,
                              'id': workers_upd.id
                              }


def test_update_client_genre(workers: WorkIn = workers):
    workers_upd = WorkOut(
        name='Юлия Иванова',
        phone='+7143658769',
        pay='10000',
        genre='Женщина',
        id=1
    )
    assert dict(workers_upd) == {'name': workers.name,
                              'phone': workers.phone,
                              'pay': workers.pay,
                              'genre': workers.genre,
                              'id': workers_upd.id
                              }
