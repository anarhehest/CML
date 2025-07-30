# Choice

This Python program analyzes decision trees, calculating pros/cons for each option and determining the optimal choice based on scored results.
It handles arbitrarily nested structures and real-world data scenarios.

**Supported formats**:
* CML (Choice Markdown Language)
* JSON
* YAML

### Usage

```shell
git clone https://github.com/anarhehest/choice.git
cd choice
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m main -f examples/cml/example.cml
```

### CML input example:
```plain
< Чё надо?
    < Шоколада
        + Вкусно
        + Вкусненько
        - Зубки спасибо не скажут
    >
    < Маринада
        < Почему?
            < Потому что
                + Потому что потому
                - Да почему?!
            >
            < По качану
                - Не бейте
            >
        >
    >
>
```

### Output example:
```plain
> Чё надо?::Шоколада (2 - 1 = 1)
> Чё надо?::Маринада::Почему?::Потому что (1 - 1 = 0)
> Чё надо?::Маринада::Почему?::По качану (0 - 1 = -1)
< Чё надо?::Шоколада (1)
```