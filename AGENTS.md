# AGENTS.md

## Cursor Cloud specific instructions

### Project overview

Windows Credential Manager desktop GUI app built with PySide6 and pywin32. See `README.md` for full details.

### Linux development (Cloud VM)

This is a Windows-only app (`win32cred`, `pythoncom`). On Linux, stub modules in `stubs/` provide in-memory replacements. Always include stubs on the Python path:

```
export PYTHONPATH=/workspace/stubs:/workspace/src
```

### Running the app

```bash
source /workspace/.venv/bin/activate
export DISPLAY=:1
export PYTHONPATH=/workspace/stubs:/workspace/src
python -m src.main
```

The Desktop pane uses display `:1`. For headless (no GUI) testing, use `DISPLAY=:99` with Xvfb or `QT_QPA_PLATFORM=offscreen`.

### System libraries required for PySide6

These must be installed once (already present in the snapshot):

```
libegl1 libgl1 libopengl0 libxcb-cursor0 libxcb-xinerama0 libxcb-randr0 libxcb-shape0 libxcb-xfixes0 libxcb-render-util0 libxcb-keysyms1 libxcb-icccm4 libxkbcommon-x11-0
```

### Linting

```bash
source /workspace/.venv/bin/activate
ruff check src/ tests/
```

### Testing

```bash
source /workspace/.venv/bin/activate
PYTHONPATH=/workspace/stubs:/workspace/src pytest tests/ -v
```

Note: test files (`tests/test_validators.py`, `tests/test_credential_manager.py`) exist but are currently empty.

### Key gotchas

- `pywin32` cannot be installed on Linux; the `stubs/` directory provides `win32cred` and `pythoncom` with in-memory credential storage.
- Credentials stored via stubs are ephemeral (in-memory only, lost on process restart).
- The `toggle_password_visibility` method uses `Qt.Checked` enum comparison, which works on Windows with the real Qt bindings. On PySide6 on Linux, the checkbox `stateChanged` signal passes an integer (2 for checked, 0 for unchecked) which still compares correctly against `Qt.CheckState.Checked`.
