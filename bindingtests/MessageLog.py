# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MessageLog(Component):
    """A MessageLog component.


Keyword arguments:
- id (string; optional)
- log (list of strings; required)
- trigServLogUpdate (boolean; default False)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, log=Component.REQUIRED, trigServLogUpdate=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'log', 'trigServLogUpdate']
        self._type = 'MessageLog'
        self._namespace = 'bindingtests'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'log', 'trigServLogUpdate']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['log']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(MessageLog, self).__init__(**args)
