package com.example.library.controller;

import com.example.library.model.*;
import com.example.library.service.LibraryService;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
import java.util.*;

@RestController @RequestMapping("/api")
public class LibraryController {
    private final LibraryService service;
    public LibraryController(LibraryService service){this.service=service;}
    @GetMapping("/books") public List<Book> books(@RequestParam(defaultValue="") String q){return service.books(q);}
    @PostMapping("/books") public ResponseEntity<Book> addBook(@RequestBody Map<String,String> b){return ResponseEntity.status(HttpStatus.CREATED).body(service.addBook(b.get("title"),b.get("author"),b.get("category")));}
    @DeleteMapping("/books/{id}") public Map<String,String> deleteBook(@PathVariable long id){service.deleteBook(id);return Map.of("message","Book deleted.");}
    @GetMapping("/members") public List<Member> members(){return service.members();}
    @PostMapping("/members") public ResponseEntity<Member> addMember(@RequestBody Map<String,String> m){return ResponseEntity.status(HttpStatus.CREATED).body(service.addMember(m.get("name"),m.get("type"),m.get("email")));}
    @GetMapping("/issues") public List<IssueRecord> issues(){return service.issues();}
    @PostMapping("/issues") public ResponseEntity<IssueRecord> issue(@RequestBody Map<String,Long> b){return ResponseEntity.status(HttpStatus.CREATED).body(service.issue(b.getOrDefault("bookId",0L),b.getOrDefault("memberId",0L)));}
    @PostMapping("/issues/{id}/return") public IssueRecord returnBook(@PathVariable long id){return service.returnBook(id);}
    @ExceptionHandler({IllegalArgumentException.class}) public ResponseEntity<Map<String,String>> badRequest(RuntimeException e){return ResponseEntity.badRequest().body(Map.of("error",e.getMessage()==null?"Invalid request":e.getMessage()));}
    @ExceptionHandler({IllegalStateException.class}) public ResponseEntity<Map<String,String>> serverError(RuntimeException e){return ResponseEntity.status(500).body(Map.of("error","Storage error: "+e.getMessage()));}
}
