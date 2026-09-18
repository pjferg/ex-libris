# Maintaining the library

- Keep this repository simple: one Markdown file per book in `books/` and a
  table in `index.md`. Follow the example in `README.md`.
- After adding or updating books, run `python3 index_books.py` to refresh the
  index. Do not edit index rows manually. Keep indexed metadata on single lines
  as shown in `README.md`.
- Preserve the owner's notes and reading and lending history.
- Check for existing books before adding entries. Ask when a title is ambiguous.
- For photographs in `images/inbox/`, inspect the images, enter only details you
  can identify, and tell the owner what is uncertain. Leave unknown fields blank;
  do not invent reading history, ratings, or loans.
- Do not add tooling, dependencies, or automated workflows unless requested.
