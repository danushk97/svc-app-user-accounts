import pytest

from user_accounts.infrastructure._unit_of_work import AbstractUnitOfWork


def test_abstract_unit_of_work_methods_raises_not_implemented_error():
    abs_uow = AbstractUnitOfWork()

    with pytest.raises(NotImplementedError):
        abs_uow.commit()

    with pytest.raises(NotImplementedError):
        abs_uow.rollback()

    with pytest.raises(NotImplementedError):
        abs_uow.end_session()
