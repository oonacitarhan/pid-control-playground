# Usage

Run from the repository root with Python 3.10 or newer. No runtime dependencies are required.

```sh
python3 -m controlbench examples/motor.json --csv /tmp/motor-trace.csv
python3 -m controlbench examples/loaded-motor.json
```

The CLI prints JSON so results can be archived or consumed by another tool. Use `--help` for options.
