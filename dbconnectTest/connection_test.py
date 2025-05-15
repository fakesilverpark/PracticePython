import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from test import DATABASE_URL

async def test_connection():
    engine = create_async_engine(DATABASE_URL, echo=True)
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT * FROM board"))
            rows = result.fetchall()
            for row in rows:
                print(row)
        print("✅ DB 연결 성공")
    except Exception as e:
        print("❌ DB 연결 실패:", e)

if __name__ == "__main__":
    asyncio.run(test_connection())