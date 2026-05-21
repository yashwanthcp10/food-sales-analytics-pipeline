from src.utils.helpers import (
    generate_batch_id
)


def test_generate_batch_id():

    batch_id = generate_batch_id()

    assert batch_id is not None