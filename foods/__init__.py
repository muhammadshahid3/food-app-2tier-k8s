"""Food catalog application."""

# PyMySQL provides the MySQLdb-compatible driver Django's MySQL backend uses.
try:
    import pymysql

    pymysql.install_as_MySQLdb()
except ImportError:
    # SQLite remains usable when optional MySQL dependencies are not installed.
    pass
