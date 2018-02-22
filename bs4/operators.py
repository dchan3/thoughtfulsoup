OPERATORS = {
    "=": lambda el, attribute, value: el._attr_value_as_string(attribute) == value, # string representation of `attribute` is equal to `value`
    "~": lambda el, attribute, value: value in el.get(attribute, []) if isinstance(el.get(attribute, []), list) else value in el.get(attribute, []).split(), # space-separated list representation of `attribute` contains `value`
    "^": lambda el, attribute, value: el._attr_value_as_string(attribute, '').startswith(value), # string representation of `attribute` starts with `value`
    "$": lambda el, attribute, value: el._attr_value_as_string(attribute, '').endswith(value), # string representation of `attribute` ends with `value`
    "*": lambda el, attribute, value: value in el._attr_value_as_string(attribute, ''), # string representation of `attribute` contains `value`
    "|": lambda el, attribute, value: el._attr_value_as_string(attribute, '') == value or el._attr_value_as_string(attribute, '').startswith(value + '-'),     # string representation of `attribute` is either exactly `value` or starts with `value` and then a dash.
    "def": lambda el, attribute, value: el.has_attr(attribute)
}
