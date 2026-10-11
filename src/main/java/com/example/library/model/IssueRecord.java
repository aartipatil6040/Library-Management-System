package com.example.library.model;

public record IssueRecord(long id, long bookId, String bookTitle, long memberId, String memberName,
                          String issueDate, String dueDate, String returnDate, double fine, String status) {}
