import pytest

from user_accounts.infrastructure._unit_of_work import AbstractUnitOfWork


@pytest.fixture
def unit_of_work():
    class UnitOfWork(AbstractUnitOfWork):
        def commit(self):
            return super().commit()

        def rollback(self):
            return super().rollback()

        def end_session(self):
            return super().end_session()

    return UnitOfWork()

def test_unit_of_work_methods_raises_not_implemented_error(unit_of_work):
    with pytest.raises(NotImplementedError):
        unit_of_work.commit()

    with pytest.raises(NotImplementedError):
        unit_of_work.rollback()

    with pytest.raises(NotImplementedError):
        unit_of_work.end_session()
