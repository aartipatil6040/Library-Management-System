# Leaf & Lore — Library Management System (Web)

A mini-project implementation with an HTML/CSS/JavaScript frontend and a Java Spring Boot REST backend backed by SQLite.

## Technology stack
- Java 17
- Spring Boot 3.3.5 (REST API)
- HTML5, CSS3 and vanilla JavaScript
- SQLite database via JDBC driver
- Maven

## Features
- View/search books by title or author
- Add and delete books (issued books cannot be deleted)
- Register students and teachers
- Issue available books with a 14-day due date
- Return books and calculate overdue fines (student: ₹2/day; teacher: ₹1/day)
- Enforce borrowing limits (student: 3 active loans; teacher: 5)
- Persist records in `library.db` automatically
- Responsive dashboard with Books, Members, and Issue/Return sections

## Run locally
1. Install JDK 17+ and Maven 3.8+.
2. Open a terminal in this folder.
3. Run `mvn spring-boot:run`.
4. Open `http://localhost:8080` in a browser.

The SQLite file `library.db` is created in the working directory on first launch and seeded with sample records if the tables are empty. Internet is only needed on the first Maven dependency download. The Google Fonts import is optional; the page falls back to system fonts if offline.

## API overview
- `GET /api/books?q=keyword`
- `POST /api/books` with `{ "title": "...", "author": "...", "category": "..." }`
- `DELETE /api/books/{id}`
- `GET /api/members`, `POST /api/members`
- `GET /api/issues`
- `POST /api/issues` with `{ "bookId": 1, "memberId": 1 }`
- `POST /api/issues/{id}/return`

## Notes
This version is a web adaptation of the original Swing/file-serialization concept. The updated screenshots in the report illustrate the proposed web UI and should be replaced with live-run screenshots after launching the app for formal demonstration. Sample records are included to make the first launch easy to review.
