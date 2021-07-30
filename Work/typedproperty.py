from typing import Any, Type


def typedproperty(name: str, expected_type: Type) -> property:
    private_name = f'_{name}'

    @property
    def prop(self) -> Any:
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value: Any) -> Any:
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop
