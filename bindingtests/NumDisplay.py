# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class NumDisplay(Component):
    """A NumDisplay component.


Keyword arguments:
- number (number; optional)
- id (string; optional)"""
    @_explicitize_args
    def __init__(self, number=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['number', 'id']
        self._type = 'NumDisplay'
        self._namespace = 'bindingtests'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['number', 'id']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(NumDisplay, self).__init__(**args)
