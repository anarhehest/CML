# Choice

This Python program analyzes decision trees defined in YAML format, calculating pros/cons for each option and determining the optimal choice based on scored results.
It handles arbitrarily nested structures and real-world data scenarios.

### Usage

```shell
git clone https://github.com/anarhehest/choice.git
cd choice
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m main examples/example.yml
```

### YML example:
```yaml
Чё надо?:
  Шоколада:
    pros:
      - Вкусно
      - Вкусненько
    cons:
      - Зубки
  Маринада:
    Почему?:
      Потому что:
        pros:
          - Потому что потому
        cons:
          - Да почему?!
      По качану:
        cons:
          - Не бейте
```

### Output example:
```plain
> Чё надо?::Шоколада (2 - 1 = 1)
> Чё надо?::Маринада::Почему?::Потому что (1 - 1 = 0)
> Чё надо?::Маринада::Почему?::По качану (0 - 1 = -1)
< Чё надо?::Шоколада (1)
```