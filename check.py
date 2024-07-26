#!/usr/bin/env python

import json
import os

import pydantic


FILE = os.path.abspath(__file__)
HERE = os.path.dirname(FILE)

INPUT_FILE = os.path.join(HERE, "data", "animetitles.json")


class AnimeTitle(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(strict=True, extra="forbid")

    language: str
    type: str
    title: str


class Anime(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(strict=True, extra="forbid")

    id: int
    titles: list[AnimeTitle]


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            raw_json = line.strip()
            if not raw_json:
                continue

            item = json.loads(raw_json)

            # Let Pydantic validate `item`.
            #
            # This raises an exception on invalid types.
            Anime(**item)


if __name__ == "__main__":
    main()
