![Banner](https://user-images.githubusercontent.com/79407681/221333383-d5167801-b4e9-418a-b40e-638ec175e953.png)


AIOGram Bot Template
====================

[![Telegram](https://img.shields.io/badge/-Contact-2f3136?style=for-the-badge&logo=telegram)](https://t.me/lantrik)

this is a **bot template** based on the aiogram module!

Installing
----------

Python 3.7 or higher is required.

``` sh
# Linux/macOS
python3 -m pip install -r requirements.txt
# Windows
py -3 -m pip install -r requirements.txt
```

<sup>if you do not install `requirements.txt`, then the bot may not start!</sup>

Starting
--------

- First, you should obtain token for your bot from [BotFather](https://t.me/BotFather).
- After you have to paste the bot token in the `config/privacy.py`.

if the `privacy.py` file does not exist, you must create it in the `config` directory.

<sup>The path to the file should be: `config/privacy.py`</sup>

The file `privacy.py` must contain a class with a bot token.

### Example

```py
class Privacy:
    bot: str = "BOT_TOKEN"
```

- For the bot to work, you must run the `__main__.py` file.

<br>
<p align="center">
    <a href="https://t.me/lantrik">Contact me</a>
    ⁕
    <a href="https://t.me/tiktok_downloader_example_bot">Bot Example</a>
</p>
<br>


Architecture
============

soon
