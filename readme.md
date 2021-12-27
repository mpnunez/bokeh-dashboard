# Bokeh Dashboard template

This is an example of a project that uses a bokeh dashboard.

See [Running a bokeh server](https://docs.bokeh.org/en/latest/docs/user_guide/server.html)

To get started, clone the repository and create the virtual environment.

```
git clone git@github.com:mpnunez/bokeh-dashboard.git
cd bokeh-dashboard
python3 -m venv .venv
./.venv/bin/pip install --upgrade pip
./.venv/bin/pip install -r requirements.txt
```

Then, launch the dashboard.

```
./.venv/bin/bokeh serve --show myapp
```

Go to the address in a web browser.
