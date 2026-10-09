# ВКР Система поддержки принятия решений по техническому обслуживанию транспортных средств на основе анализа эксплуатационных данных.
 (когда актуализирую тему, пока так)

# Описание
Машины проходят техническое обслуживание согласно регламенту пройденного километража, в связи с чем появляются ситуации, когда техническое обслуживание проходят машины, не нуждающиеся в ремонте, либо машины выходят из строя во время рейса. \
**Цель проекта**: Построить прогнозную модель для оптимизации плана технического обслуживания, сокращая расходы на техническое обслуживание автопарка, уменьшает простой машин и риск возникновения неисправности во время рейса.

# Используемые технологии

# Архитектура

# Структура проекта

# Запуск
Клонировать репозиторий (github):
```shell
git clone https://github.com/Alwaline/predictive_maintenance.git
```

Клонировать репозиторий (kpfu.git):
```shell
git clone https://git.kpfu.ru/AGaniev/predictive_maintenance.git
```

Перейти в каталог репозитория:
```shell
cd predictive_maintenance
```

Запустить скрипт загрузки датасета:
```shell
python src/load.py
```

# Метрики

# Ноутбуки
- EDA [EDA.ipynb](notebooks/EDA.ipynb)
- Моделирование [modeling.ipynb](notebooks/modeling.ipynb)
- ~~- Baseline [crude_data.ipynb](notebooks/crude_data.ipynb)~~

# Источники
Lindgren, T., Steinert, O., Andersson Reyna, O., Kharazian, Z., & Magnússon, S. (2025). \
SCANIA Component X Dataset: A Real-World Multivariate Time Series Dataset for Predictive Maintenance (Version 3) [Dataset]. \
Scania CV AB. https://doi.org/10.5878/bnh5-ka77

Ссылка URL: https://researchdata.se/en/catalogue/dataset/2024-34

