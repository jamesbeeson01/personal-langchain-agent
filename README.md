## Personal LangChain Agent

Simple LangChain agent for my personal use and exploration.

## Setup (one time)

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
2. Create a `.env` file in this folder with your API key:

   ```
   GOOGLE_API_KEY=your-key-here
   ```

3. From this folder, install the `agent` command:

   ```
   uv tool install --editable .
   uv tool update-shell
   ```

4. Close and reopen your terminal.

## Run it

Open any terminal and type:

```
agent
```

Type `exit` to quit.

Because the install is *editable*, changes you make to the code show up the
next time you run `agent`. There's no need to reinstall.

If you add a new dependency to `pyproject.toml`, run this again from this folder:

```
uv tool install --editable . --reinstall
```
