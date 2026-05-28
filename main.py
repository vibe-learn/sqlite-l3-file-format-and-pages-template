"""Homework scaffold — sqlite lesson `l3_file_format_and_pages` (Vibe Learn).

Задача: мини-инспектор формата файла: read_header (первые 100 байт), is_sqlite, bloat_ratio, demo_vacuum.

Реализуй функции ниже — сигнатуры и тестовая поверхность фиксированы;
CI (.github/workflows/ci.yml) ставит зависимости и гоняет `pytest`.
Подробности и критерии приёмки — в README.md.

SQLite встроена в Python через stdlib `sqlite3` — никакого драйвера ставить
не нужно, сервера нет. БД это файл (DATABASE_PATH) или ":memory:" в тестах.
"""

import os
import sqlite3


def database_path() -> str:
    """Путь к файлу БД из env. Дефолт ":memory:" — БД живёт в процессе."""
    return os.environ.get("DATABASE_PATH", ":memory:")


def connect(path: str | None = None) -> sqlite3.Connection:
    """Открыть соединение sqlite3 (по умолчанию из database_path())."""
    return sqlite3.connect(path if path is not None else database_path())


# ----- TODO #1: read_header -----
def read_header(path: str) -> dict:
    """распарсить {magic, page_size (BE [16:18]), page_count ([28:32]), freelist_count ([36:40])} из первых 100 байт"""
    raise NotImplementedError("read_header: реализуй меня")


# ----- TODO #2: is_sqlite -----
def is_sqlite(path: str) -> bool:
    """проверить магическую строку 'SQLite format 3\x00' в [0:16]"""
    raise NotImplementedError("is_sqlite: реализуй меня")


# ----- TODO #3: bloat_ratio -----
def bloat_ratio(conn) -> float:
    """оценка фрагментации: PRAGMA freelist_count / PRAGMA page_count"""
    raise NotImplementedError("bloat_ratio: реализуй меня")


# ----- TODO #4: demo_vacuum -----
def demo_vacuum(conn) -> tuple[int, int]:
    """размер файла до и после VACUUM"""
    raise NotImplementedError("demo_vacuum: реализуй меня")



def main() -> None:
    """Точка входа: подключиться и напомнить, что реализовать.

    Замени тело на демонстрацию реализованных функций.
    """
    print("Vibe Learn — sqlite lesson scaffold up")
    print(f"DATABASE_PATH: {database_path()} (stdlib sqlite3, no server)")
    print("Реализуй TODO-функции, затем `pytest`. README.md содержит задачу.")


if __name__ == "__main__":
    main()
