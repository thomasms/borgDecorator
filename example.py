from functools import wraps


class FilterBorg:
    __shared_state = {'filters': {}}

    def __init__(self):
        self.__dict__ = self.__shared_state


def register_filter(filter_type):
    def decorator(cls):
        borg = FilterBorg()
        borg.filters[filter_type] = cls
    return decorator


@register_filter("Dummy")
class DummyFilter:
    pass



@register_filter("Dummy2")
class DummyAgainFilter:
    pass


borg = FilterBorg()
for n, f in borg.filters.items():
    print(n, f, f())
