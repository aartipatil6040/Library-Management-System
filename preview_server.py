from http.server import SimpleHTTPRequestHandler, HTTPServer
import json, os
BOOKS=[{"id":1,"title":"Atomic Habits","author":"James Clear","category":"Personal Growth","status":"Available"},{"id":2,"title":"The Alchemist","author":"Paulo Coelho","category":"Fiction","status":"Available"},{"id":3,"title":"Clean Code","author":"Robert C. Martin","category":"Technology","status":"Issued"},{"id":4,"title":"Wings of Fire","author":"A. P. J. Abdul Kalam","category":"Biography","status":"Available"},{"id":5,"title":"Ikigai","author":"Héctor García","category":"Wellness","status":"Available"},{"id":6,"title":"The Pragmatic Programmer","author":"Andrew Hunt","category":"Technology","status":"Available"}]
MEMBERS=[{"id":1,"name":"Aarav Sharma","type":"Student","email":"aarav@example.com"},{"id":2,"name":"Mira Patel","type":"Student","email":"mira@example.com"},{"id":3,"name":"Dr. Neha Rao","type":"Teacher","email":"neha.rao@example.com"}]
ISSUES=[{"id":1,"bookId":3,"bookTitle":"Clean Code","memberId":1,"memberName":"Aarav Sharma","issueDate":"2026-10-01","dueDate":"2026-10-15","returnDate":None,"fine":0,"status":"Issued"},{"id":2,"bookId":4,"bookTitle":"Wings of Fire","memberId":2,"memberName":"Mira Patel","issueDate":"2026-09-12","dueDate":"2026-09-26","returnDate":"2026-09-29","fine":6,"status":"Returned"}]
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*args,**kwargs): super().__init__(*args,directory='/mnt/data/LibraryManagementWeb/preview',**kwargs)
 def do_GET(self):
  if self.path.startswith('/api/books'): self.sendjson(BOOKS)
  elif self.path.startswith('/api/members'): self.sendjson(MEMBERS)
  elif self.path.startswith('/api/issues'): self.sendjson(ISSUES)
  else: super().do_GET()
 def sendjson(self,obj):
  b=json.dumps(obj).encode(); self.send_response(200); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(b))); self.end_headers(); self.wfile.write(b)
HTTPServer(('127.0.0.1',8765),Handler).serve_forever()
