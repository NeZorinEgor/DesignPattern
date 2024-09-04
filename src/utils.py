def singleton(class_):
    """ Декоратор, обеспечивающий создание только одного экземпляра класса """
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance
