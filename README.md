# anidb-animetitles-archive

> [!NOTE]
>
> Automatic updates temporarily paused.
>
> I'm changing things in the backend. I'll resume the automatic updates
> after everything is stable on my side.

Daily updates of AniDB anime titles dumps.

For flexibility, I'm downloading their daily titles dump to a VPS,
processing it there, and then using GitHub Actions to download the
result from that VPS.

To avoid triggering any GitHub repository limits, I'm only pushing the
final JSON file. This should reduce the size of commits (after `git gc`
or `git repack` runs, at least).

I might trim the history of this repository if it gets too large, so you
should assume a force-push will happen eventually.

## Files

| Path | Description |
|---|---|
| [`data/animetitles.json`](https://raw.githubusercontent.com/c032/anidb-animetitles-archive/main/data/animetitles.json) | Newline-delimited JSON. Each line contains one anime with all its titles. |

## Source

<https://wiki.anidb.net/API>

## License

AniDB data is licensed under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

See <https://anidb.net/policy> for more information about AniDB's
licensing.
