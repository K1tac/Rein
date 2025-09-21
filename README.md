# Rein

**Rein** is a lightweight, customizable command-line interface inspired by the Linux terminal.

```bash
<user>-<path>@rein:~#
```

Type `help` inside Rein for a list of available commands.

---

## Installation

Clone the repository and run the main Python file:

```bash
git clone https://github.com/K1tac/Rein.git
cd Rein
python Rein.py
```

### Dependencies

Rein may require additional Python packages (e.g. `colorama`). Install them using:

```bash
pip install -r requirements.txt
```

---

## Troubleshooting

* If Rein is missing dependencies or the folder structure, re-install from the repository.
* Critical errors are often resolved by starting fresh.

---

## Creating Rein Distributions

Want to build your own distro of Rein?

* Fork this repository.
* Modify `Rein.py` and add dependencies if needed.
* Update the **Distribution** and **Author** values in the scripts or dependencies to reflect your version.
