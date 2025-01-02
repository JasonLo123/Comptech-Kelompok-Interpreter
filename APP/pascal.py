import sys
sys.path.insert(0, "../..")

import paslex
import pasparse
import pasinterp

# If a filename has been specified, we try to run it.
# If a runtime error occurs, we bail out and enter
# interactive mode below
if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
        data = f.read()
    prog = pasparse.parse(data)
    if not prog:
        raise SystemExit
    b = pasinterp.PascalInterpreter(prog)
    try:
        b.run()
        raise SystemExit
    except RuntimeError:
        pass
else:
    b = pasinterp.PascalInterpreter({})