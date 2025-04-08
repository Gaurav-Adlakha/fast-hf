---
title: FastHTML Hello World
emoji: 🚀
colorFrom: blue
colorTo: indigo
sdk: docker
sdk_version: "3.10"
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# FastHTML Hello World

A simple Hello World web application using FastHTML and MonsterUI for Hugging Face Spaces.

## Features

- Clean, modern UI with MonsterUI styling
- Simple interactive button using HTMX
- Ready to deploy to Hugging Face Spaces

## Deployment

To deploy this application to Hugging Face Spaces:

1. Create a free account on [Hugging Face](https://huggingface.co)
2. Go to your account settings and create an access token with write access
3. Set the `HF_TOKEN` environment variable to that token
4. Run `fh_hf_deploy <space_name>` replacing `<space_name>` with your desired space name

## Local Development

To run this application locally:

```bash
pip install -r requirements.txt
python main.py
```

Then open your browser to [http://localhost:5001](http://localhost:5001) 