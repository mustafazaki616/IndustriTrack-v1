import asyncio
from app.database.seeds.seed_data import main

if __name__ == "__main__":
    print("Starting database seeding...")
    asyncio.run(main())
    print("Seeding complete.")
