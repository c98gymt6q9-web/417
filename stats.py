"""Собирает цифры продаж из базы бота и пишет их в stats.js для сайта.

Только агрегаты (число заказов, покупателей, средняя оценка) — без имён и контактов.

Запуск:
    DATABASE_URL="postgres://..." python3 tools/stats.py      # база на хостинге (Neon)
    DB_PATH=~/shop-bot/shop.db python3 tools/stats.py          # локальный SQLite
"""
import datetime
import json
import os
import pathlib
import sqlite3

QUERIES = {
    "paid_orders": "SELECT COUNT(*) FROM orders WHERE status='paid'",
    "buyers": "SELECT COUNT(DISTINCT user_id) FROM orders WHERE status='paid'",
    "reviews": "SELECT COUNT(*) FROM reviews WHERE status='published'",
    "rating": "SELECT AVG(rating) FROM reviews WHERE status='published'",
}


def connect():
    url = os.getenv("DATABASE_URL")
    if url:
        import psycopg  # есть в .venv бота

        return psycopg.connect(url)
    path = os.path.expanduser(os.getenv("DB_PATH", "~/shop-bot/shop.db"))
    if not os.path.exists(path):
        raise SystemExit(f"Нет базы: {path}. Укажи DATABASE_URL или DB_PATH.")
    return sqlite3.connect(path)


def main():
    conn = connect()
    stats = {}
    for key, sql in QUERIES.items():
        cur = conn.cursor()
        cur.execute(sql)
        stats[key] = cur.fetchone()[0]
    conn.close()
    stats["rating"] = round(float(stats["rating"]), 1) if stats["rating"] else None
    stats["updated"] = datetime.date.today().strftime("%d.%m.%Y")

    out = pathlib.Path(__file__).resolve().parent.parent / "stats.js"
    out.write_text(
        "// Создано tools/stats.py — не правь вручную\n"
        f"window.STATS_417 = {json.dumps(stats, ensure_ascii=False)};\n",
        encoding="utf-8",
    )
    print(f"Готово: {out}\n{stats}")


if __name__ == "__main__":
    main()
