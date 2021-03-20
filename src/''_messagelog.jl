# AUTO GENERATED FILE - DO NOT EDIT

export ''_messagelog

"""
    ''_messagelog(;kwargs...)

A MessageLog component.

Keyword arguments:
- `id` (String; optional)
- `log` (Array of Strings; required)
- `trigServLogUpdate` (Bool; optional)
"""
function ''_messagelog(; kwargs...)
        available_props = Symbol[:id, :log, :trigServLogUpdate]
        wild_props = Symbol[]
        return Component("''_messagelog", "MessageLog", "bindingtests", available_props, wild_props; kwargs...)
end

