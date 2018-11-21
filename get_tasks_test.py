import pytest
from get_tasks import parse_args

def test_raises_exception_on_arguments_that_arent_four_args():
    with pytest.raises(NameError):
        parse_args('foo')



