# 📒 FastAPI + Python — Complete Beginner Notes

> These notes are based on your **INotes** project (Code With Harry tutorial).
> Every concept is explained line-by-line so you can use this as a reference.

---

## Table of Contents

1. [What is FastAPI?](#1--what-is-fastapi)
2. [Setting Up the Project (Virtual Environment, pip, etc.)](#2--setting-up-the-project)
3. [Project Structure Explained](#3--project-structure-explained)
4. [Pip Packages — What Was Installed & Why](#4--pip-packages--what-was-installed--why)
5. [File-by-File Breakdown](#5--file-by-file-breakdown)
   - [index.py — The Main App Entry Point](#51-indexpy--the-main-app-entry-point)
   - [config/db.py — Database Connection](#52-configdbpy--database-connection)
   - [models/note.py — The Pydantic Model](#53-modelsnote py--the-pydantic-model)
   - [schemas/note.py — MongoDB Data Converters](#54-schemasnote py--mongodb-data-converters)
   - [routes/note.py — API Routes (The Heart of the App)](#55-routesnotepy--api-routes)
   - [templates/index.html — The Frontend (Jinja2 + Bootstrap)](#56-templatesindexhtml--the-frontend)
   - [static/style.css — Custom Styles](#57-staticstylecss--custom-styles)
   - [main.py — Old/Commented Out Code](#58-mainpy--old-code)
   - [tempCodeRunnerFile.py — Pydantic Practice](#59-tempcoderunnerfilepy--pydantic-practice)
6. [Key Python Concepts Used](#6--key-python-concepts-used)
7. [How to Run This Project](#7--how-to-run-this-project)
8. [Quick Reference Cheat Sheet](#8--quick-reference-cheat-sheet)

---

## 1. 🚀 What is FastAPI?

FastAPI is a **modern, fast Python web framework** for building APIs (Application Programming Interfaces).

| Feature | Explanation |
|---------|-------------|
| **Fast** | One of the fastest Python frameworks (built on top of Starlette & Pydantic) |
| **Easy** | Designed to be easy to learn and use |
| **Auto Docs** | Automatically generates API documentation at `/docs` (Swagger UI) and `/redoc` |
| **Type Hints** | Uses Python type hints for validation — catches errors before they happen |
| **Async Support** | Supports `async/await` for handling many requests at once |

> **Think of it like this:** FastAPI is like Express.js (for Node.js) or Flask (for Python), but faster and with built-in data validation.

---

## 2. 🛠️ Setting Up the Project

### 2.1 What is a Virtual Environment (`.venv`)?

A virtual environment is an **isolated Python environment** for your project. It keeps your project's packages separate from other projects on your computer.

**Why use it?**
- Project A might need `fastapi==0.100.0`, Project B might need `fastapi==0.141.1`
- Without `.venv`, they'd conflict. With `.venv`, each project has its own packages.

**How was it created in your project?**

```bash
# Open terminal in your project folder, then run:
python -m venv .venv
```

| Part | Meaning |
|------|---------|
| `python` | Calls the Python interpreter |
| `-m venv` | Runs the built-in `venv` **m**odule |
| `.venv` | Name of the folder to create (`.venv` is the convention, the dot makes it hidden) |

Your `.venv` was created with **Python 3.14.7** (from `pyvenv.cfg`).

### 2.2 Activating the Virtual Environment

```bash
# On Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

# On Windows (CMD):
.\.venv\Scripts\activate.bat

# On Mac/Linux:
source .venv/bin/activate
```

> When activated, you'll see `(.venv)` at the start of your terminal prompt. This means all `pip install` commands will install packages ONLY inside `.venv`.

### 2.3 What is `pip`?

`pip` = **P**ackage **I**nstaller for **P**ython. It downloads and installs Python packages from [pypi.org](https://pypi.org).

```bash
# Install a single package:
pip install fastapi

# Install multiple packages:
pip install fastapi uvicorn pymongo jinja2 python-multipart
```

### 2.4 The `.venv` Folder Structure

```
.venv/
├── Include/          # C header files (for compiling C extensions)
├── Lib/              # All installed packages live here
│   └── site-packages/
│       ├── fastapi/
│       ├── pymongo/
│       ├── pydantic/
│       └── ... (all your pip packages)
├── Scripts/          # Executable scripts (python.exe, pip.exe, uvicorn.exe)
├── pyvenv.cfg        # Config file — records which Python version created this venv
└── .gitignore        # Tells Git to ignore .venv contents
```

> [!IMPORTANT]
> **Never commit `.venv` to Git!** It's large and machine-specific. Instead, use a `requirements.txt` file (your project is missing one — see the tip below).

> [!TIP]
> **Create a requirements.txt** to save your installed packages:
> ```bash
> pip freeze > requirements.txt
> ```
> Then anyone can recreate your environment with:
> ```bash
> pip install -r requirements.txt
> ```

---

## 3. 📁 Project Structure Explained

```
FastAPITutorial/
├── .venv/                    # Virtual environment (DO NOT EDIT)
├── __pycache__/              # Python's compiled bytecode cache (auto-generated, ignore)
│
├── config/                   # ⚙️ Configuration files
│   └── db.py                 #    Database connection setup
│
├── models/                   # 📦 Data models (Pydantic)
│   └── note.py               #    Defines what a "Note" looks like
│
├── schemas/                  # 🔄 Data converters/serializers
│   └── note.py               #    Converts MongoDB documents to Python dicts
│
├── routes/                   # 🛣️ API route handlers
│   └── note.py               #    All the URL endpoints (/get, /post, etc.)
│
├── templates/                # 🖥️ HTML templates (Jinja2)
│   └── index.html            #    The main webpage
│
├── static/                   # 🎨 Static files (CSS, JS, images)
│   └── style.css             #    Custom CSS styles (currently empty)
│
├── index.py                  # 🚀 MAIN APP FILE — starts the FastAPI app
├── main.py                   # 📝 Old/commented out code (not used)
└── tempCodeRunnerFile.py     # 🧪 Pydantic practice file (not used by app)
```

### Why this structure?

This follows a **modular pattern** — separating concerns into different folders:

| Folder | Responsibility | Real-World Analogy |
|--------|---------------|-------------------|
| `config/` | Database connection | The phone number to call the database |
| `models/` | Data shape/structure | A form template — "what fields does a Note have?" |
| `schemas/` | Data transformation | A translator between MongoDB format and Python format |
| `routes/` | Request handling | The receptionist — "what should I do when someone visits `/`?" |
| `templates/` | HTML views | The actual webpage the user sees |
| `static/` | CSS/JS/images | The design and decoration of the webpage |

---

## 4. 📦 Pip Packages — What Was Installed & Why

Here are all the packages installed in your `.venv`:

### Packages YOU Directly Installed

| Package | Version | What It Does | Install Command |
|---------|---------|-------------|-----------------|
| **fastapi** | 0.141.1 | The web framework itself | `pip install fastapi` |
| **uvicorn** | 0.52.4 | The ASGI server that **runs** your FastAPI app | `pip install uvicorn` |
| **pymongo** | 4.17.0 | Python driver to talk to **MongoDB** database | `pip install pymongo` |
| **jinja2** | 3.1.6 | Template engine — lets you put Python variables inside HTML | `pip install jinja2` |
| **python-multipart** | 0.0.32 | Needed for handling **form data** (`Form(...)` in routes) | `pip install python-multipart` |

### Packages Installed AUTOMATICALLY (Dependencies)

These were installed automatically because the above packages depend on them:

| Package | Why It Was Installed |
|---------|---------------------|
| **pydantic** (2.13.4) | FastAPI uses it for data validation. When you write `class Note(BaseModel)`, that's Pydantic |
| **starlette** (1.6.0) | FastAPI is built on top of Starlette (handles HTTP requests under the hood) |
| **anyio** (4.14.2) | Async I/O library used by Starlette |
| **click** (8.4.2) | Used by Uvicorn for command-line argument parsing |
| **h11** (0.16.0) | HTTP/1.1 protocol parser used by Uvicorn |
| **httptools** (0.8.0) | Fast HTTP parser for Uvicorn |
| **idna** (3.19) | Handles international domain names |
| **MarkupSafe** (3.0.3) | Used by Jinja2 to prevent XSS attacks in HTML |
| **dnspython** (2.8.0) | Used by PyMongo for DNS-based MongoDB connection strings (`mongodb+srv://`) |
| **colorama** (0.4.6) | Colors in the terminal (Windows) |
| **python-dotenv** (1.2.3) | Loads `.env` files (environment variables) |
| **typing_extensions** (4.16.0) | Backports newer Python typing features |
| **watchfiles** (1.2.0) | Used by Uvicorn's `--reload` to detect file changes |
| **websockets** (17.0.1) | WebSocket support for Uvicorn |
| **pydantic_core** (2.46.4) | The fast Rust core of Pydantic |
| **annotated-types** (0.8.0) | Type annotation utilities for Pydantic |
| **PyYAML** (6.0.3) | YAML parser (used internally) |

> [!NOTE]
> **You don't need to memorize the auto-installed packages.** Just know the 5 you installed directly. The rest come along for the ride!

---

## 5. 📄 File-by-File Breakdown

---

### 5.1 [index.py](file:///e:/FastAPITutorial/index.py) — The Main App Entry Point

This is the **heart of your application** — the file you run to start the server.

```python
from fastapi import FastAPI                    # Line 1
from fastapi.staticfiles import StaticFiles    # Line 2

from routes.note import note                   # Line 4

app = FastAPI()                                # Line 7
app.mount("/static", StaticFiles(directory="static"), name="static")  # Line 8

app.include_router(note)                       # Line 11
```

#### Line-by-Line Explanation:

---

**Line 1:** `from fastapi import FastAPI`

```
from fastapi    →  Go into the "fastapi" package (installed via pip)
import FastAPI  →  Grab the "FastAPI" class from it
```

| Part | What It Is |
|------|-----------|
| `fastapi` | The package name (lowercase) |
| `FastAPI` | The class name (PascalCase) — this is the main application class |

> **Analogy:** `FastAPI` is like a blueprint for your web application. You need to create an instance of it to use it.

---

**Line 2:** `from fastapi.staticfiles import StaticFiles`

```
from fastapi.staticfiles  →  Go into the "staticfiles" module inside fastapi
import StaticFiles        →  Grab the "StaticFiles" class
```

`StaticFiles` lets you serve **static files** (CSS, JavaScript, images) that don't change.

---

**Line 4:** `from routes.note import note`

```
from routes.note  →  Go to the file: routes/note.py
import note       →  Import the "note" variable (which is an APIRouter)
```

This imports your route handler from the `routes` folder.

---

**Line 7:** `app = FastAPI()`

```python
app = FastAPI()
```

| Part | Meaning |
|------|---------|
| `app` | Variable name — you can call it anything, but `app` is the convention |
| `FastAPI()` | Creates a **new instance** of the FastAPI application |
| `()` | The parentheses **call** the class (like calling a function) to create an object |

> **Analogy:** This is like turning on your web server. `app` is now your running application that can handle web requests.

> [!NOTE]
> This `app` variable is what **uvicorn** looks for when you run `uvicorn index:app`. The format is `filename:variable_name`.

---

**Line 8:** `app.mount("/static", StaticFiles(directory="static"), name="static")`

```python
app.mount("/static", StaticFiles(directory="static"), name="static")
```

| Part | Meaning |
|------|---------|
| `app.mount(...)` | Attach a sub-application to a specific URL path |
| `"/static"` | URL path — files will be accessible at `http://localhost:8000/static/...` |
| `StaticFiles(directory="static")` | Look for files in the `static/` folder on disk |
| `name="static"` | Internal name for this mount (used for URL generation) |

**Example:** If you have `static/style.css`, it's accessible at `http://localhost:8000/static/style.css`

---

**Line 11:** `app.include_router(note)`

```python
app.include_router(note)
```

| Part | Meaning |
|------|---------|
| `app.include_router(...)` | Connect a set of routes to the main app |
| `note` | The APIRouter imported from `routes/note.py` |

> **Analogy:** Think of `app` as the main highway, and `note` as an on-ramp. `include_router` connects the on-ramp to the highway so traffic (requests) can flow through.

> **Why use routers?** To keep code organized! Instead of putting ALL your routes in one file, you split them into separate files (one for notes, one for users, etc.)

---

### 5.2 [config/db.py](file:///e:/FastAPITutorial/config/db.py) — Database Connection

This file sets up the connection to your **MongoDB Atlas** (cloud) database.

```python
from pymongo import MongoClient                                                # Line 1

Mongo_URI = (                                                                  # Line 3
    "mongodb+srv://shubhamcoding77_db_user:Shubham@fastapilearning.1888c7p.mongodb.net"
)

conn = MongoClient(Mongo_URI)                                                  # Line 8
```

#### Line-by-Line Explanation:

---

**Line 1:** `from pymongo import MongoClient`

```
from pymongo      →  The pymongo package (MongoDB driver for Python)
import MongoClient →  The class that creates a connection to MongoDB
```

---

**Lines 3-5:** `Mongo_URI = "mongodb+srv://..."`

This is a **connection string** — like a phone number + password for your database.

```
mongodb+srv://         →  Protocol (use MongoDB's SRV DNS-based connection)
shubhamcoding77_db_user →  Username
:Shubham               →  Password
@fastapilearning.1888c7p.mongodb.net  →  Cluster address (MongoDB Atlas)
```

> [!WARNING]
> **Security Risk!** The database password is hardcoded in the source code. In a real project, you should use **environment variables**:
> ```python
> import os
> Mongo_URI = os.getenv("MONGO_URI")
> ```
> And store the actual URI in a `.env` file (which you add to `.gitignore`).

---

**Line 8:** `conn = MongoClient(Mongo_URI)`

```python
conn = MongoClient(Mongo_URI)
```

| Part | Meaning |
|------|---------|
| `conn` | Variable holding the database connection |
| `MongoClient(...)` | Creates a connection to MongoDB using the URI |

Now `conn` can be imported in other files to talk to the database.

---

### 5.3 [models/note.py](file:///e:/FastAPITutorial/models/note.py) — The Pydantic Model

This file defines the **shape/structure** of a Note using Pydantic.

```python
from pydantic import BaseModel     # Line 1

class Note(BaseModel):             # Line 4
    title: str                     # Line 5
    description: str               # Line 6
    important: bool = False        # Line 7
```

#### Line-by-Line Explanation:

---

**Line 1:** `from pydantic import BaseModel`

```
from pydantic    →  Pydantic is a data validation library
import BaseModel →  BaseModel is the parent class that gives your model superpowers
```

**What is Pydantic?** It automatically validates data. If someone sends `title: 123` instead of `title: "hello"`, Pydantic will raise an error because `123` is not a `str`.

---

**Lines 4-7:** The `Note` class

```python
class Note(BaseModel):
    title: str
    description: str
    important: bool = False
```

| Part | Meaning |
|------|---------|
| `class Note` | Defines a new class called `Note` |
| `(BaseModel)` | `Note` **inherits** from `BaseModel` — gets all Pydantic features |
| `title: str` | A field called `title` that MUST be a string |
| `description: str` | A field called `description` that MUST be a string |
| `important: bool = False` | A field called `important` that is a boolean, **defaults to** `False` |

**What does `: str` mean?** This is a Python **type hint**. It tells Python (and Pydantic) what type of data this field should hold.

| Type Hint | Means | Examples |
|-----------|-------|---------|
| `str` | String (text) | `"Hello"`, `"My Note"` |
| `int` | Integer (whole number) | `1`, `42`, `-5` |
| `float` | Decimal number | `3.14`, `0.5` |
| `bool` | Boolean (True/False) | `True`, `False` |
| `list` | List/Array | `[1, 2, 3]` |

**What does `= False` mean?** It's a **default value**. If the user doesn't provide `important`, it automatically becomes `False`.

---

### 5.4 [schemas/note.py](file:///e:/FastAPITutorial/schemas/note.py) — MongoDB Data Converters

This file converts **MongoDB documents** (which have `_id` as an ObjectId) into **regular Python dictionaries**.

```python
def noteConverter(item) -> dict:             # Line 1
    return {                                  # Line 2
        "id": str(item["_id"]),              # Line 3
        "title": item["title"],              # Line 4
        "description": item["description"],  # Line 5
        "important": item["important"],      # Line 6
    }                                         # Line 7

def noteListConverter(items) -> list:        # Line 11
    return [noteConverter(item) for item in items]  # Line 12
```

#### Line-by-Line Explanation:

---

**Line 1:** `def noteConverter(item) -> dict:`

| Part | Meaning |
|------|---------|
| `def` | Keyword to **define a function** |
| `noteConverter` | Function name |
| `(item)` | Takes one parameter — a single MongoDB document |
| `-> dict` | **Return type hint** — this function returns a dictionary |
| `:` | Starts the function body |

---

**Line 3:** `"id": str(item["_id"])`

MongoDB stores IDs as `ObjectId("66abc123...")` — a special type. `str(...)` converts it to a regular string `"66abc123..."` so it can be used in JSON/HTML.

---

**Lines 11-12:** `noteListConverter`

```python
def noteListConverter(items) -> list:
    return [noteConverter(item) for item in items]
```

This is a **list comprehension** — a shorthand for looping:

```python
# This one-liner:
[noteConverter(item) for item in items]

# Is the same as:
result = []
for item in items:
    result.append(noteConverter(item))
```

It takes a **list of MongoDB documents** and converts each one using `noteConverter`.

> [!NOTE]
> In your current [routes/note.py](file:///e:/FastAPITutorial/routes/note.py), these converter functions are **imported but not actually used** — the conversion is done manually inline. These functions are a cleaner alternative that could replace the manual loop.

---

### 5.5 [routes/note.py](file:///e:/FastAPITutorial/routes/note.py) — API Routes (The Heart of the App)

This is the most important file — it defines **what happens when someone visits your website**.

```python
from models.note import Note                              # Line 1
from fastapi import APIRouter, Request, Form              # Line 2
from fastapi.responses import HTMLResponse                # Line 3
from config.db import conn                                # Line 4
from fastapi.templating import Jinja2Templates            # Line 5

from schemas.note import noteConverter, noteListConverter  # Line 7

note = APIRouter()                                        # Line 9
templates = Jinja2Templates(directory="templates")        # Line 10
```

#### Imports Explained:

| Import | What It Is | Why We Need It |
|--------|-----------|----------------|
| `Note` from `models.note` | The Pydantic model | To validate note data |
| `APIRouter` from `fastapi` | A mini-app for grouping routes | To organize routes in separate files |
| `Request` from `fastapi` | Represents the incoming HTTP request | Needed by Jinja2 templates |
| `Form` from `fastapi` | Extracts data from HTML forms | To read form submissions |
| `HTMLResponse` from `fastapi.responses` | Tells FastAPI to return HTML (not JSON) | To serve web pages |
| `conn` from `config.db` | MongoDB connection | To read/write data |
| `Jinja2Templates` from `fastapi.templating` | Template rendering engine | To render HTML with dynamic data |
| `noteConverter`, `noteListConverter` from `schemas.note` | Data converters | To convert MongoDB docs (imported but unused) |

---

**Line 9:** `note = APIRouter()`

```python
note = APIRouter()
```

| Part | Meaning |
|------|---------|
| `note` | Variable name for this router |
| `APIRouter()` | Creates a new router — like a mini FastAPI app |

> **Why APIRouter instead of FastAPI?** You use `FastAPI()` for the main app (in `index.py`) and `APIRouter()` for sub-sections. Then connect them with `app.include_router(note)`.

---

**Line 10:** `templates = Jinja2Templates(directory="templates")`

```python
templates = Jinja2Templates(directory="templates")
```

Tells Jinja2 to look for HTML files in the `templates/` folder.

---

#### The GET Route — Display Notes

```python
@note.get("/", response_class=HTMLResponse)         # Line 13
async def read_item(request: Request):               # Line 14
    newDocs = []                                      # Line 15
    docs = conn.notes.notes.find()                   # Line 16
    for doc in docs:                                  # Line 17
        newDocs.append(                               # Line 18
            {                                         # Line 19
                "id": doc["_id"],                     # Line 20
                "title": doc["title"],                # Line 21
                "description": doc["description"],    # Line 22
                "important": doc["important"],        # Line 23
            }                                         # Line 24
        )                                             # Line 25

    return templates.TemplateResponse(                # Line 27
        request, "index.html", {"newDocs": newDocs}
    )
```

**Line 13:** `@note.get("/", response_class=HTMLResponse)`

This is a **decorator** — it "decorates" the function below it with extra behavior.

| Part | Meaning |
|------|---------|
| `@` | Decorator syntax — attaches this to the function below |
| `note` | The APIRouter we created |
| `.get` | This route responds to **GET** requests (when you visit a URL in the browser) |
| `"/"` | The URL path — this handles the **root** (homepage): `http://localhost:8000/` |
| `response_class=HTMLResponse` | Tell FastAPI the response is HTML, not JSON |

**HTTP Methods Explained:**

| Method | When It's Used | Example |
|--------|---------------|---------|
| `GET` | **Reading/fetching** data | Visiting a webpage, loading notes |
| `POST` | **Creating** new data | Submitting a form, adding a note |
| `PUT` | **Updating** existing data | Editing a note |
| `DELETE` | **Deleting** data | Removing a note |

---

**Line 14:** `async def read_item(request: Request):`

| Part | Meaning |
|------|---------|
| `async` | Makes this function **asynchronous** — can handle multiple requests efficiently |
| `def` | Defines a function |
| `read_item` | Function name (you can name it anything) |
| `request: Request` | Parameter — FastAPI automatically fills this with the incoming request data |
| `: Request` | Type hint — tells FastAPI this should be a `Request` object |

> **What is `async`?** Think of a restaurant. A **synchronous** waiter takes one order, waits in the kitchen, brings it, then takes the next order. An **async** waiter takes an order, sends it to the kitchen, takes the next order while food is being prepared. Much more efficient!

---

**Line 16:** `docs = conn.notes.notes.find()`

```python
conn.notes.notes.find()
```

| Part | Meaning |
|------|---------|
| `conn` | The MongoDB connection (from `config/db.py`) |
| `.notes` | The **database** name in MongoDB (first `.notes`) |
| `.notes` | The **collection** name (second `.notes`) — like a table in SQL |
| `.find()` | Get **all documents** from this collection |

> **MongoDB Hierarchy:** `Connection → Database → Collection → Document`
> It's like: `Server → Database → Table → Row` in SQL

---

**Lines 17-25:** Building the response list

```python
for doc in docs:
    newDocs.append({
        "id": doc["_id"],
        "title": doc["title"],
        "description": doc["description"],
        "important": doc["important"],
    })
```

This loops through each MongoDB document, extracts the fields, and puts them in a clean Python dictionary list.

---

**Line 27:** `return templates.TemplateResponse(request, "index.html", {"newDocs": newDocs})`

| Part | Meaning |
|------|---------|
| `templates.TemplateResponse(...)` | Render an HTML template and send it as the response |
| `request` | The original request (required by Jinja2) |
| `"index.html"` | Which HTML file to render (from `templates/` folder) |
| `{"newDocs": newDocs}` | **Context** — Python variables to pass INTO the HTML template |

> The `newDocs` list becomes available inside `index.html` as `{{ newDocs }}`.

---

#### The POST Route — Create a Note

```python
@note.post("/")                                                        # Line 30
async def create_note(request: Request,                                # Line 31
                      title: str = Form(...),
                      description: str = Form(...)):
    formDict = {"title": title, "description": description,            # Line 32
                "important": False}
    conn.notes.notes.insert_one(formDict)                              # Line 33
    return {"Success": True}                                           # Line 34
```

**Line 30:** `@note.post("/")`

Same URL path `/` but uses `POST` method. When the HTML form submits, it sends a POST request.

---

**Line 31:** `title: str = Form(...), description: str = Form(...)`

| Part | Meaning |
|------|---------|
| `title: str` | A parameter named `title` of type string |
| `= Form(...)` | Get this value from **form data** (not URL, not JSON) |
| `...` | The `Ellipsis` — means this field is **required** (no default value) |

> **Why `Form(...)` instead of just `title: str`?** Because HTML forms send data in a special format (`application/x-www-form-urlencoded`). `Form(...)` tells FastAPI to look for the data in that format. Without it, FastAPI would look for a query parameter in the URL instead.

---

**Line 33:** `conn.notes.notes.insert_one(formDict)`

| Part | Meaning |
|------|---------|
| `insert_one(...)` | Insert a single document into the MongoDB collection |
| `formDict` | The dictionary containing the note data |

---

**Line 34:** `return {"Success": True}`

Returns a **JSON response** confirming the note was created.

> [!NOTE]
> After submitting the form, the user sees `{"Success": True}` as raw JSON. A better approach would be to **redirect** back to the homepage:
> ```python
> from fastapi.responses import RedirectResponse
> return RedirectResponse(url="/", status_code=303)
> ```

---

### 5.6 [templates/index.html](file:///e:/FastAPITutorial/templates/index.html) — The Frontend

This is a **Jinja2 template** — HTML mixed with Python-like syntax.

#### Key Sections:

**Bootstrap CSS (Line 8-9):**
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" ...>
```
Loads **Bootstrap 5** from a CDN — gives you pre-built CSS classes for styling.

---

**Navigation Bar (Lines 13-37):**
```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
```
A Bootstrap navbar with "INotes" branding, Home/About links, and a search bar.

---

**The Form (Lines 42-54):**
```html
<form action='/' method="post">
    <input type="text" name="title" ...>
    <input type="text" name="description" ...>
    <button type="submit">Submit</button>
</form>
```

| Attribute | Meaning |
|-----------|---------|
| `action='/'` | Where to send the form data — the root URL |
| `method="post"` | Use HTTP POST method — matches `@note.post("/")` in Python |
| `name="title"` | This must match the parameter name `title: str = Form(...)` in the route |
| `name="description"` | Must match `description: str = Form(...)` |

> [!IMPORTANT]
> The `name` attribute on `<input>` tags MUST match the parameter names in your Python route function. If the input has `name="title"`, the route must have `title: str = Form(...)`.

---

**Jinja2 Template Syntax (Lines 64-77):**
```html
{% if newDocs is defined %}
    no notes to display
{% endif %}

{% for item in newDocs %}
<div class="card" style="width: 18rem;">
    <div class="card-body">
        <h5 class="card-title">{{ item.note }}</h5>
    </div>
</div>
{% endfor %}
```

**Jinja2 Syntax Cheat Sheet:**

| Syntax | What It Does | Example |
|--------|-------------|---------|
| `{{ variable }}` | **Print** a variable's value | `{{ item.title }}` → prints the title |
| `{% ... %}` | **Logic** — if/for/etc. | `{% for item in items %}` |
| `{# ... #}` | **Comments** — not shown in HTML | `{# This is a comment #}` |

> [!WARNING]
> **Bug in the template!** Line 73 uses `{{ item.note }}` but the data passed from Python has `title`, `description`, `id`, and `important` — there is no `note` key. It should probably be `{{ item.title }}` and `{{ item.description }}`.

> [!NOTE]
> **Logic Bug:** The `{% if newDocs is defined %}` block shows "no notes to display" when `newDocs` IS defined (which is always, since you pass it from Python). The logic should likely be:
> ```html
> {% if newDocs|length == 0 %}
>     No notes to display
> {% endif %}
> ```

---

### 5.7 [static/style.css](file:///e:/FastAPITutorial/static/style.css) — Custom Styles

This file is currently **empty**. It's where you'd add custom CSS styles.

The app currently relies entirely on Bootstrap for styling. You could add custom styles like:

```css
/* Example custom styles */
body {
    background-color: #f5f5f5;
}

.card {
    margin: 10px 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
```

---

### 5.8 [main.py](file:///e:/FastAPITutorial/main.py) — Old/Commented Out Code

```python
# from fastapi import FastAPI, Request
# from pymongo import MongoClient
# app = FastAPI()
# conn = MongoClient("mongodb+srv://...")
```

This was your **initial attempt** — everything in one file. You then **refactored** the code into the modular structure (separate folders for config, models, routes, etc.), and the main entry point moved to `index.py`.

> This file is no longer used and can be safely deleted.

---

### 5.9 [tempCodeRunnerFile.py](file:///e:/FastAPITutorial/tempCodeRunnerFile.py) — Pydantic Practice

```python
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'Shubham Tupe'
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, 2, "3"],
}

user = User(**external_data)
print(user)
```

This is a **practice file** for learning Pydantic. Let's break it down:

| Line | What It Shows |
|------|--------------|
| `id: int` | Even though `"123"` is a string, Pydantic auto-converts it to `int` → `123` |
| `name = 'Shubham Tupe'` | Default value (but NOT a type-hinted field — just a class attribute) |
| `signup_ts: datetime \| None = None` | Optional field — can be a `datetime` or `None` |
| `friends: list[int] = []` | A list of integers, defaults to empty list |
| `"friends": [1, 2, "3"]` | `"3"` (string) gets auto-converted to `3` (int) by Pydantic! |
| `**external_data` | **Unpacking** — spreads the dictionary as keyword arguments |

**What `**` (double star) does:**
```python
User(**external_data)
# Is the same as:
User(id="123", signup_ts="2017-06-01 12:22", friends=[1, 2, "3"])
```

> This file was auto-generated by VS Code's Code Runner extension and is not part of the app.

---

## 6. 🐍 Key Python Concepts Used

### 6.1 Imports

```python
from fastapi import FastAPI      # Import specific item from a package
import pymongo                    # Import the entire package
from config.db import conn       # Import from your own files (relative)
```

| Style | When to Use |
|-------|------------|
| `from X import Y` | When you only need specific things from a package |
| `import X` | When you need many things, use as `X.something` |
| `from folder.file import thing` | Import from your own project files |

### 6.2 Decorators (`@`)

```python
@note.get("/")
async def read_item(request: Request):
    ...
```

A **decorator** wraps a function with extra behavior. `@note.get("/")` says: "When someone makes a GET request to `/`, run this function."

### 6.3 Type Hints

```python
title: str              # This should be a string
important: bool = False # This should be a boolean, defaults to False
def func(x: int) -> str:  # Takes int, returns str
```

Type hints don't **enforce** types in plain Python, but FastAPI + Pydantic **use them** for validation.

### 6.4 `async` / `await`

```python
async def read_item(request: Request):
    ...
```

`async` makes functions non-blocking. FastAPI can handle other requests while waiting for slow operations (like database queries).

### 6.5 Dictionaries

```python
formDict = {"title": title, "description": description, "important": False}
```

A **dictionary** is a key-value data structure — like a JSON object.

### 6.6 List Comprehension

```python
[noteConverter(item) for item in items]
# Shorthand for a loop that builds a list
```

---

## 7. ▶️ How to Run This Project

### Step 1: Activate the virtual environment
```bash
.\.venv\Scripts\Activate.ps1
```

### Step 2: Run the server
```bash
uvicorn index:app --reload
```

| Part | Meaning |
|------|---------|
| `uvicorn` | The ASGI server |
| `index` | The Python file name (`index.py`, without `.py`) |
| `:app` | The variable name inside that file (`app = FastAPI()`) |
| `--reload` | Auto-restart when you save code changes (development only!) |

### Step 3: Open in browser
- **App:** http://localhost:8000
- **API Docs (Swagger):** http://localhost:8000/docs
- **API Docs (ReDoc):** http://localhost:8000/redoc

---

## 8. 📋 Quick Reference Cheat Sheet

### FastAPI Route Decorators

```python
@app.get("/path")           # Handle GET requests
@app.post("/path")          # Handle POST requests
@app.put("/path")           # Handle PUT requests
@app.delete("/path")        # Handle DELETE requests
@app.patch("/path")         # Handle PATCH requests
```

### FastAPI Response Types

```python
return {"key": "value"}                              # JSON response (default)
return HTMLResponse("<h1>Hello</h1>")                # HTML response
return templates.TemplateResponse(request, "file.html", {})  # Template response
return RedirectResponse(url="/", status_code=303)    # Redirect
```

### MongoDB with PyMongo

```python
conn.database_name.collection_name.find()            # Get all documents
conn.database_name.collection_name.find_one({"_id": id})  # Get one
conn.database_name.collection_name.insert_one({...}) # Insert one
conn.database_name.collection_name.update_one(       # Update one
    {"_id": id}, {"$set": {...}}
)
conn.database_name.collection_name.delete_one({"_id": id})  # Delete one
```

### Pydantic Model

```python
from pydantic import BaseModel

class MyModel(BaseModel):
    required_field: str             # Required (no default)
    optional_field: str = "default" # Optional (has default)
    nullable_field: str | None = None  # Can be None
```

### Jinja2 Template Syntax

```html
{{ variable }}                  <!-- Print a variable -->
{% for item in list %}          <!-- Loop -->
{% endfor %}
{% if condition %}              <!-- Conditional -->
{% elif other %}
{% else %}
{% endif %}
```

---

> [!TIP]
> **Next Steps to Level Up:**
> 1. Add `PUT` and `DELETE` routes to update and delete notes
> 2. Fix the template bugs (`item.note` → `item.title`)
> 3. Add a `requirements.txt` file (`pip freeze > requirements.txt`)
> 4. Move the MongoDB URI to a `.env` file for security
> 5. Add error handling with `try/except` blocks
> 6. Try building a REST API (JSON only, no HTML templates) — FastAPI shines here!

---

*Notes generated from your FastAPITutorial project — Code With Harry tutorial* ✨
