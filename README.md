# 417 · educational community

Сайт-визитка проекта 417: конспекты, тыки и билеты к коллоквиумам по анатомии и истории России.
Покупка — в Telegram-боте [@of417r_bot](https://t.me/of417r_bot).

Статичный сайт без сборки: `index.html` + папка `assets`. 3D — three.js, анимации — GSAP + Lenis (подключаются с CDN).

## Публикация на GitHub Pages

1. Создай на GitHub новый публичный репозиторий, например `417-site`, без README.
2. В папке сайта выполни (подставь свой логин):

   ```bash
   git remote add origin https://github.com/ЛОГИН/417-site.git
   git push -u origin main
   ```

3. В репозитории: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, ветка `main`, папка `/ (root)` → **Save**.
4. Через 1–2 минуты сайт откроется по адресу `https://ЛОГИН.github.io/417-site/`.

## Что где править

| Что | Где |
|---|---|
| Бот, каталог, цены, превью PDF | блок `window.SITE` в `index.html` |
| 3D-объект на главной | `assets/video/hero.webm` (WebM с прозрачностью); размер и яркость — `SIZE` и `LIFT` в `index.html` |
| Бегущий текст на фоне | `assets/bgtext.js` |
| Страницы превью PDF | `assets/pdf/<материал>/pNN.jpg` |
| Картинки в «Медиа» | `assets/img/` |
| Интервью | раздел `<!-- INTERVIEW -->` в `index.html`, оригинал — `assets/interview-417.pdf` |

## Цифры продаж

Счётчики берут данные из `stats.js`. Сейчас там `null`, поэтому показываются цифры каталога.
Чтобы подставить реальные продажи из базы бота (только итоговые числа, без личных данных):

```bash
DATABASE_URL="postgres://..." python3 tools/stats.py
```

Потом закоммить и запушь обновлённый `stats.js`.
