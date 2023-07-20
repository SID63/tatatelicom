import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Student } from './student.model';

@Injectable({
  providedIn: 'root'
})
export class StudentService {
  private baseUrl = 'http://your-backend-api-url'; // Replace this with your actual backend API URL

  constructor(private http: HttpClient) {}

  // Function to add a new student
  addStudent(student: Student): Observable<any> {
    const url = `${this.baseUrl}/add-student`; // Replace 'add-student' with your backend API endpoint to add a student
    return this.http.post(url, student);
  }

  // Function to update an existing student
  updateStudent(student: Student): Observable<any> {
    const url = `${this.baseUrl}/update-student`; // Replace 'update-student' with your backend API endpoint to update a student
    return this.http.put(url, student);
  }
}
