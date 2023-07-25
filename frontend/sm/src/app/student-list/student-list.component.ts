import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Student } from '../student.model';

@Component({
  selector: 'app-student-list',
  templateUrl: './student-list.component.html',
  styleUrls: ['./student-list.component.css']
})
export class StudentListComponent {
  showTable: boolean = false;
  students: Student[] = [];
  baseUrl = 'http://localhost:5000'; // Update the base URL to your backend's URL

  constructor(private http: HttpClient) {}

  onViewStudentsClick(): void {
    this.http.get<Student[]>(`${this.baseUrl}/view-students`).subscribe(
      (response: Student[]) => {
        this.students = response;
        this.showTable = true;
      },
      (error: any) => {
        console.error('Error fetching students:', error);
        // You can handle the error here, e.g., display an error message to the user
      }
    );
  }
}
