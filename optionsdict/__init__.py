# optionsdict: The tiny parser


def string_to_python(sval):
    if sval is None:
        return None
    if sval == 'true':
        return True
    if sval == 'false':
        return False


def parse(args, defaults={}):
    """Converts a list of 'key=value' command line arguments to a
       dictionary.

       The Python values True, False, and None may be set
       case-insensitively. To delete a key foo, use the syntax
       'foo=' with no value. One standalone argument may be given
       without the '=' separator, and this argument will be
       mapped to the key named _arg. If more than one standalone
       argument is given, the last one wins.

       Values that convert to integer without error are stored
       as integers.

       Returns the result of applying supplied arguments to a
       dictionary of default values.
    """
    parsed = defaults.copy()
    if args is None:
        return parsed
    for i in range(len(args)):
        head, sep, tail = args[i].partition('=')
        if not sep:
            key = '_arg'
            parsed[key] = head
            continue
        if not tail:
            if head in parsed:
                del parsed[head]
            continue
        ltail = tail.lower()
        if ltail in ['true', 'false', 'none']:
            parsed[head] = string_to_python(ltail)
            continue
        try:
            tail = int(tail)
        except ValueError:
            pass
        parsed[head] = tail
    return parsed
