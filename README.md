<p align="center">
  <img src="assets/ship-header.webp" alt="Парусник в бирюзовом море" width="100%">
</p>

<p align="center">
  <strong>Ваш надёжный DevOps капитан в море ИИ разработки.</strong>
</p>

<p align="center">
  <a href="https://t.me/proffessor_it"><strong>Связаться в Telegram ↗</strong></a> &nbsp; · &nbsp;
  <a href="https://welcome.professorit.ru/"><strong>Professor IT ↗</strong></a> &nbsp; · &nbsp;
  <a href="#избранные-проекты"><strong>Посмотреть проекты ↓</strong></a>
</p>

### Разрабатываю, автоматизирую, объясняю.

Linux, воспроизводимые системы и события безопасности — в коде и открытых проектах. Мой подход: **описать систему → автоматизировать изменения → проверить поведение → контролировать состояние**.

## Технологии в проектах

<p>
  <a href="https://github.com/alphaserver777/NixOS"><img src="assets/skills-systems.svg?v=ocean-1" alt="Системы: Linux, NixOS, Ubuntu, systemd" width="400"></a>
  <a href="https://github.com/alphaserver777/hashgraph/tree/main/deploy"><img src="assets/skills-delivery.svg?v=ocean-1" alt="Автоматизация: Docker, Kubernetes, Git, Bash" width="400"></a>
</p>
<p>
  <a href="https://github.com/alphaserver777/Docker/tree/main/monitoring/grafana-deploy"><img src="assets/skills-observability.svg?v=ocean-1" alt="Контроль состояния: Prometheus, Grafana, Loki, Python" width="400"></a>
  <a href="https://github.com/alphaserver777/hashgraph/tree/main/tests"><img src="assets/skills-security.svg?v=ocean-1" alt="Безопасность: sops-nix, SSH, HMAC, pytest" width="400"></a>
</p>

<details>
<summary><strong>Как применяю эти инструменты</strong></summary>

| Направление | Примеры в открытом коде |
| :--- | :--- |
| Воспроизводимость | [Nix Flakes и Home Manager](https://github.com/alphaserver777/NixOS/tree/main/nixos-config): общие модули и настройки отдельных машин |
| Развёртывание | [Docker Compose и конфигурации Kubernetes](https://github.com/alphaserver777/hashgraph/tree/main/deploy) в исследовательском MDRJ-DAG |
| Показатели и журналы | [Стенд Prometheus, Grafana и Loki](https://github.com/alphaserver777/Docker/tree/main/monitoring/grafana-deploy), пересылка событий через rsyslog |
| Секреты и доступ | sops-nix в конфигурации NixOS, [уведомления о событиях SSH](https://github.com/alphaserver777/Ubuntu/tree/main/security) |
| Проверка решений | [Проверка подлинности запросов и тесты MDRJ-DAG](https://github.com/alphaserver777/hashgraph/tree/main/tests), сценарии разделения сети и восстановления обмена |

</details>

## Избранные проекты

<p>
  <a href="https://github.com/alphaserver777/hashgraph"><img src="assets/project-hashgraph.svg?v=ocean-1" alt="MDRJ-DAG — исследовательский прототип распределённого журнала событий безопасности. Python, SQLite, Docker." width="400"></a>
  <a href="https://github.com/alphaserver777/NixOS"><img src="assets/project-nixos.svg?v=ocean-1" alt="NixOS — личная инфраструктура как код. Nix Flakes, Home Manager, sops-nix." width="400"></a>
</p>
<p>
  <a href="https://github.com/alphaserver777/Docker/tree/main/monitoring/grafana-deploy"><img src="assets/project-monitoring.svg?v=ocean-1" alt="Контроль сервисов — стенд сбора показателей и журналов. Prometheus, Grafana, Loki." width="400"></a>
  <a href="https://github.com/alphaserver777/Ubuntu/tree/main/security"><img src="assets/project-ssh.svg?v=ocean-1" alt="SSH-события — автоматизация уведомлений о доступе к Linux. Python, SSH, systemd." width="400"></a>
</p>

<details>
<summary><strong>Технические детали и документация</strong></summary>

**MDRJ-DAG.** Исследовательский прототип обмена событиями безопасности между узлами без выделенного ведущего узла. Причинные связи между событиями, приоритетная передача и локальное хранение в SQLite. [Архитектура](https://github.com/alphaserver777/hashgraph/tree/main/docs/architecture) · [Проверки](https://github.com/alphaserver777/hashgraph/tree/main/tests).

**NixOS.** Личная конфигурация систем с общими модулями, Home Manager, подключением sops-nix и пересылкой важных событий через rsyslog. [Конфигурация](https://github.com/alphaserver777/NixOS/tree/main/nixos-config) · [Руководства](https://github.com/alphaserver777/NixOS/tree/main/guides).

**Контроль сервисов.** Стенд с веб-приложением, Prometheus, Grafana и Loki. Состав сервисов описан в Docker Compose, есть пример панели и нагрузочные запросы с разными ответами и задержками. [Состав сервисов](https://github.com/alphaserver777/Docker/blob/main/monitoring/grafana-deploy/docker-compose.yml) · [Панель Grafana](https://github.com/alphaserver777/Docker/blob/main/monitoring/grafana-deploy/grafana/example-dashboard.json).

**SSH-события.** Чтение журналов авторизации и отправка уведомлений в Telegram. Настройка через переменные окружения, пример запуска и перезапуска службы через systemd. [Код и инструкция](https://github.com/alphaserver777/Ubuntu/tree/main/security).

</details>

## Активность на GitHub

<a href="https://github.com/alphaserver777?tab=overview"><img src="assets/github-activity.svg?v=ocean-1" alt="Открытая статистика GitHub: число репозиториев, год регистрации и календарь активности за последние 365 дней. Дата обновления указана на карточке." width="100%"></a>

## Передаю инженерный опыт

Развиваю **[Professor IT](https://welcome.professorit.ru/)** и публикую **[практические задания](https://github.com/alphaserver777/DevOps_professor_it)** по эксплуатации, автоматизации, контролю состояния систем и нагрузочному тестированию. Объясняю решения через практику, код и разбор поведения системы.

---

<p align="center">
  <strong>Обсудим инфраструктуру, безопасность или разработку надёжных систем.</strong><br><br>
  <a href="https://t.me/proffessor_it">Telegram ↗</a> &nbsp; · &nbsp; <a href="https://welcome.professorit.ru/">Professor IT ↗</a>
</p>

<p align="center">
  <img src="assets/ocean-footer-trimmed.svg" alt="Бирюзовые морские волны" width="100%">
</p>
