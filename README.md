# BytesBump - Server List Extension
Link your bump bot with a server list!

## Features
- Beautiful. I think, at least.
- Responsive.
- Easy navigation.
- Soon-to-come updates.

## Made using
- Back-end
    - Flask
    - MongoDB
- Front-end
    - Pug.js
    - JavaScript
    - Markdown-it
    - Bootstrap

# Setting Up
**⚠️ YOU WILL NEED A MONGODB FOR IT, CHECK [THIS REPO](https://github.com/Nemika-Haj/BytesBump) ON HOW TO SET IT UP ⚠️**

📝 **Note: This server list supports only bots originating from [BytesBump](https://github.com/Nemika-Haj/BytesBump). However, if you are experienced enough, you can modify it to your own needs**

## **Configuring `settings.json`**
- First of all, rename `settings-example.json` to `settings.json`
- Replace its content with proper values.
### __Example__
```json
{
    "site_name": "BytesBump Server List",
    "mongo": "mongo-uri (same as the bot's)",
    "bot_token": "bump bot's token"
}
```
- Go to your **BytesBump** `settings.json`, and set `enable-serverlist` to `true` and change the `serverlist_url` to your website's URL. `http://127.0.0.1:5000/` is for when the website is hosted locally.

# Hosting
We do not include instructions on how to host the website. However, we have gathered a few resources;
- [How to deploy a Python (Flask) web app on a (PythonAnywhere) live server](https://www.youtube.com/watch?v=75-oCKUx3oU) - By [`PythonHow`](https://www.youtube.com/channel/UC1nNFFS_9m8uuHOfwz8AK0w)
- [Push Flask Apps To Heroku For Webhosting](https://www.youtube.com/watch?v=Li0Abz-KT78) - By [`Codemy.com`](https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw)
- [How to Deploy a Flask App to a Linux Server](https://www.youtube.com/watch?v=YFBRVJPhDGY) - By [`Tech With Tim`](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg)