import requests
import pytest
from src.generators.player_localization import PlayerLocalization

@pytest.mark.parametrize('status',[
    'ACTIVE',
    'BANNED',
    'DELETED',
    'INACTIVE'
])
def test_status(status, get_player_generator):  # разные статусы
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize('balance_value',[
    '100',
    '0',
    '-10',
    'fsdff'
])
def test_balance(balance_value, get_player_generator):  # разное значение баланса валидное не валидное
    print(get_player_generator.set_status(balance_value).build())


@pytest.mark.parametrize('delete_key',[
    'account_status',
    'balance',
    'localize',
    'avatar'
])
def test_balance(delete_key, get_player_generator):  #как поведет себя бекенд если какогото поля нету
    object_to_send =(get_player_generator.build())
    del object_to_send[delete_key]
    print(object_to_send)


@pytest.mark.parametrize('localizations, loc', [
    ("fr", "fr_FR")
])
def test_change_localize(get_player_generator, localizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', 'localizations'],
        PlayerLocalization(loc).set_number(15).build()
    ).build()
    print(object_to_send)