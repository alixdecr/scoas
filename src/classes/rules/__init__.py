import importlib, inspect, pkgutil


RULES = []

package_name = __name__

for _, module_name, _ in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f"{package_name}.{module_name}")

    for _, obj in inspect.getmembers(module, inspect.isclass):
        # only collect classes defined in this module
        if obj.__module__ == module.__name__ and obj.__name__ != "Rule":
            RULES.append(obj)