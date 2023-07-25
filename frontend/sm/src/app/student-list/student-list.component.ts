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
  searchQuery = '';
  students: Student[] = []; // Update the type to Student[]
  constructor(private http: HttpClient) {}

  onViewStudentsClick(): void {
    this.http.get<any[]>('http://your-backend-api-url/students').subscribe(
      (response: any[]) => {
        this.students = response; // Store the fetched student data in the 'students' array
        this.showTable = true; // Show the table after data is fetched
      },
      (error: any) => {
        console.error('Error fetching students:', error);
        // You can handle the error here, e.g., display an error message to the user
      }
    );
    this.showTable = true;
  }

  // You can also define the "students" array here to hold the student data when fetched from the backend.
  // students: any[] = [];
}
