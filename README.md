# Ex Libris

A personal library in Markdown: one file per book and a [simple index](index.md).

- `books/` — book details and notes.
- `index.md` — a table linking to each book.
- `images/inbox/` — photographs of books to add.

To add a book, create `books/title-of-book.md` using this example, then add a
row to the index. Edit both directly or ask an agent to do it. No setup required.

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

To add books from photos, put the images in `images/inbox/` and ask an agent:

> Identify the books in these photographs. Check for existing entries, create
> a Markdown file for each new book, and update the index. Leave uncertain
> details blank and tell me what needs checking.

Review the changes before committing. A spine may identify a title and author;
leave any uncertain details blank.
