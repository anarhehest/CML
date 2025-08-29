# Choice Markup Language

This Python program analyzes decision trees, calculating pros/cons for each option and determining the optimal choice based on scored results.
It handles arbitrarily nested structures and real-world data scenarios.

CML was born from the need for a decision-specific markup language that:

🔍 Mirrors human reasoning - Structure matches how people naturally outline options

✍️ Prioritizes readability - Easier to write/maintain than JSON/YAML for nested decisions

🧩 Enables extensibility - Built-in support for future decision-making constructs

    “Why create a new syntax? Existing formats force decision trees into data structures, while CML makes the decision itself the first-class citizen.”


### Supported formats:
**CML** (oneline and combined styles are supported)
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

**JSON**
```json
{
  "Чё надо?": {
    "Шоколада": {
      "pros": ["Вкусно", "Вкусненько"],
      "cons": ["Зубки"]
    },
    "Маринада": {
      "Почему?": {
        "Потому что": {
          "pros": ["Потому что потому"],
          "cons": ["Да почему?!"]
        },
        "По качану": {
          "cons": ["Не бейте"]
        }
      }
    }
  }
}
```

**YAML**
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

### Usage

**Example**
```shell
git clone https://github.com/anarhehest/choice.git
cd choice
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m main -f examples/cml/example.cml
```

**Output**
```plain
> Чё надо?::Шоколада (2 - 1 = 1)
> Чё надо?::Маринада::Почему?::Потому что (1 - 1 = 0)
> Чё надо?::Маринада::Почему?::По качану (0 - 1 = -1)
< Чё надо?::Шоколада (1)
```