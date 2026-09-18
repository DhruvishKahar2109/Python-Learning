from sqlalchemy import create_engine,text

engine = create_engine(
    "mysql+pymysql://root:@localhost/python_db"
)

with engine.connect() as connection:
    connection.execute(text("DROP TABLE pages"))

    connection.execute(text("""
    CREATE TABLE pages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255)
    )
    """))


    connection.execute(text("""
                            INSERT INTO pages (name, email) VALUES('Dhruvish','dhruvish@gmail.com')
                            """))

    result = connection.execute(text("""
            SELECT * FROM pages
                """))

    for row in result:
        print(row)

    connection.commit()


print("MySQL Connected")