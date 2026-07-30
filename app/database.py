import sqlite3

def init_db():
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    cursor = conn.cursor()
    
    # Crear tabla de escaneos de Trivy simulados
    cursor.execute("""
        CREATE TABLE scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_name TEXT,
            vulnerability TEXT,
            severity TEXT,
            secret_data TEXT
        )
    """)
    
    # Insertar el registro con el secreto vulnerable
    cursor.execute("""
        INSERT INTO scans (image_name, vulnerability, severity, secret_data)
        VALUES ('backend-auth-service:v2', 'Hardcoded Secrets in Dockerfile', 'CRITICAL', 'AKIAIOSFODNN7EXAMPLE')
    """)
    
    conn.commit()
    return conn

db_conn = init_db()