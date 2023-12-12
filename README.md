# anidb-animetitles-archive

---

> **NOTE:**
>
> This repository is getting quite large, and already surpasses 1GB on
> GitHub.
>
> Before I get a warning from GitHub, I'll have to either look for an
> alternative host, or remove old files and commits to reduce repository
> size.
>
> Tentatively, I might create a torrent file for each year, and have
> only current year information in the repository.

---

Daily updates of AniDB anime titles dumps.

The `latest.xml.gz` symlink points to the most recently download file,
and `latest.xml` is just a decompressed copy of `latest.xml.gz`.

## Source

<https://wiki.anidb.net/API>

Keep in mind that AniDB might:

* Block your IP address if you download the file more than once per day.
* Reject your HTTP requests if your `User-Agent` header is too generic.

  It might be polite to use a contact email address as your
  `User-Agent`, or even a URL pointing to your project where you're
  using the AniDB data (I've successfully used both for months and
  haven't had problems yet).

## License

AniDB data is licensed under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

See <https://anidb.net/policy> for more information about AniDB's
licensing.
