import httpx


async def get_random_questions(questions_num: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://jservice.io/api/random?count={questions_num}"
        )
        response.raise_for_status()
        data = response.json()
        return data

async def get_random_question():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jservice.io/api/random?count={1}")
        response.raise_for_status()
        data = response.json()
        return data[0]
