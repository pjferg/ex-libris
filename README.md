# Ex Libris

A personal library in Markdown: one file per book and a [simple index](index.md).

- `books/` — book details and notes.
- `index.md` — a table linking to each book.
- `images/inbox/` — photographs of books to add.

To add a book, create `books/title-of-book.md` using this example.

```markdown
---
title: "The Mythical Man-Month"
author: "Frederick P. Brooks Jr."
status: unread
date_read:
rating:
location:
lent_to:
lent_date:
tags: []
---

# The Mythical Man-Month

## Thoughts

## Reading history

## Lending history
```

Leave unknown fields blank. Use `unread`, `reading`, or `read` for status,
`YYYY-MM-DD` (or just `YYYY-MM`) for dates, and a rating out of five.
Record rereads and past loans in the history sections. When a book is returned,
clear `lent_to` and `lent_date` and note the return in its lending history.

To update the index automatically, leave this running while you edit:

```sh
python3 index_books.py --watch
```

It updates `index.md` when books are added, edited, renamed, or removed. Stop
with Ctrl-C. For a one-off update, run `python3 index_books.py`. Requires Python
3 and no extra packages. Edit book files rather than the generated index.

Keep indexed metadata (`title`, `author`, `status`, `rating`, `lent_to`) on one
line per field, using plain text or quoted strings as above. The script reads
these simple fields, not the full YAML format. Leave comments in the Markdown
body. If a file has incomplete metadata while you edit, the watcher keeps the
previous index and retries.

To add books from photos, put the images in `images/inbox/` and ask an agent:

> Identify the books in these photographs. Check for existing entries, create
> a Markdown file for each new book, and update the index. Leave uncertain
> details blank and tell me what needs checking.

Review the changes before committing. A spine may identify a title and author;
leave any uncertain details blank.
